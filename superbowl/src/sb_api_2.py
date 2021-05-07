import json
from flask import Flask, request
#import jobs
from redis import StrictRedis
import os
from uuid import uuid4
from datetime import datetime
#from sb_jobs import add_job
from hotqueue import HotQueue

app = Flask(__name__)
rd= StrictRedis(host='10.104.140.94', port=6379, db=0)
#rd4= StrictRedis(host='10.104.140.94', port=6379, db=2)
rd2= StrictRedis(host='10.104.140.94', port=6379, db=3)
q= HotQueue('queue', host='10.104.140.94', port=6379, db=1)


@app.route('/set', methods=['GET'])
def set_data():
	with open("super-bowl-2.json","r") as f:
		sbgames  = json.load(f)
	rd.set('sbgames_key', json.dumps(sbgames))
	
	return 'data has been set \n'

@app.route('/read', methods=['GET'])
def read_data():
	return json.dumps(get_data(), indent=2)

def get_data():
	return json.loads(rd.get('sbgames_key').decode('utf-8'))


@app.route('/read/<sb>', methods=['GET'])
def get_game(sb):
	test = get_data()
	output = [x for x in test if x['sb'] == sb]
	return json.dumps(output, indent=2)

@app.route('/update/<uuid>', methods=['GET'])
def update_game(uuid):
	test=get_data()
	for x in test:
		if x['recordid']==uuid:
			attendance=x['attendance']
			x['attendance']=str('99999')
			break
	rd.set('sbgames_key', json.dumps(test))
	return json.dumps(test, indent=2)

@app.route('/delete/<uuid>', methods=['GET'])
def delete(uuid):
	sb_dict = get_data()
#	uuid = request.args.get('recordid') 
	for x in sb_dict:
		if x['recordid'] == uuid:
			sb_dict.remove(x)
	rd.set('sbgames_key', json.dumps(sb_dict))
	return json.dumps(sb_dict, indent=2)

@app.route('/create', methods=['GET'])
def create():
	sb_dict=get_data()
	this_game={}
	this_game['recordid']=str('1234')
	this_game['sb']=str('LVI')
	this_game['winner']=str('Dallas Cowboys')
	this_game['loser']=str('Philadelphia Eagles')
	this_game['attendance']=str('100000')
	this_game['point_difference']=str('50')

	sb_dict.append(this_game)
	rd.set('sbgames_key', json.dumps(sb_dict))
	return json.dumps(sb_dict, indent=2)

@app.route('/run', methods=['GET','POST'])
def run_job():
	if request.method == 'POST':
		this_uuid = str(uuid4()) 
		this_value= str(request.form['point_spread'])
		data= {'datetime': str(datetime.now()), 'status':'submitted', 'point_spread': this_value}
		rd2.hmset(this_uuid, data)
		q.put(this_uuid)
		return f'Job {this_uuid} submitted to the queue\n'
	else:
		return """
	curl -X POST -d "point_spread=20" 10.107.238.1:5000/run

"""

@app.route('/jobs', methods=['GET'])
def get_jobs():
	redis_dict = {}
	for key in rd2.keys():
		redis_dict[str(key.decode('utf-8'))] = {}
		redis_dict[str(key.decode('utf-8'))]['datetime'] = rd2.hget(key, 'datetime').decode('utf-8')
		redis_dict[str(key.decode('utf-8'))]['status'] = rd2.hget(key, 'status').decode('utf-8')
	return json.dumps(redis_dict, indent=4)

@app.route('/jobs/<jobuuid>', methods=['GET'])
def get_job_output(jobuuid):
	bytes_dict = rd2.hgetall(jobuuid)
	final_dict = {}
	for key, value in bytes_dict.items():
		if key.decode('utf-8') == 'image':
			final_dict[key.decode('utf-8')] = 'ready'
		else:
			final_dict[key.decode('utf-8')] = value.decode('utf-8')
	return json.dumps(final_dict, indent=4)

@app.route('/download/<jobuuid>', methods=['GET'])
def download(jobuuid):
	path = f'/sb_api_2/{jobuuid}.png'
	with open(path, 'wb') as f:
		f.write(rd2.hget(jobuuid, 'image'))
	return send_file(path, mimetype='image/png', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

