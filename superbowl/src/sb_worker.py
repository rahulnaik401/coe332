from sb_api_2 import get_data,q,rd2,rd
import time
import os
import json
import redis
import matplotlib.pyplot as plt



@q.worker
def execute_job(jobuuid):
	# jobid, status, start, end = rd2.hmget(generate_job_key(jid), 'id', 'status', 'start', 'end')
	data=rd2.hgetall(jobuuid)
	
	# update_job_status(jid, 'submitted')

	test1=get_data()
	#xdata=[int(x['point_difference']) for x in test1 if int(x['point_difference']) <=int(data[b'point_spread'].decode('utf-8'))]
	#ydata=[int(x['attendance']) for x in test1 if int(x['point_difference']) <=int(data[b'point_spread'].decode('utf-8'))]
	xdata=[int(x['point_difference']) for x in test1 if int(x['point_difference']) <=int(data[b'point_spread'].decode('utf-8'))]
	ydata=[int(x['attendance']) for x in test1 if int(x['point_difference']) <=int(data[b'point_spread'].decode('utf-8'))]
	plt.scatter(xdata,ydata)
	plt.xlabel('point_difference')
	plt.ylabel('attendance')
	
	plt.savefig('./output_image.png')
	
	with open ('./output_image.png', 'rb') as f:
		img=f.read()

	# update_job_status(jid, 'complete')
	rd2.hset(jobuuid, 'image', img)
	rd2.hset(jobuuid, 'status','finished')
	
	return

execute_job()
