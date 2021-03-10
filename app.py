import json
from flask import Flask, request

app= Flask(__name__)

def getdata():
        with open("animals.json","r") as json_file:
                userdata=json.load(json_file)
        return userdata

@app.route('/animals', methods=['GET'])
def get_animals():

        return json.dumps(getdata())

@app.route('/animals/head/', methods=['GET'])
def get_animal_head():
        animal_dict=getdata()
        animalList=animal_dict['animals']
        head_type=request.args.get('head_type')
        output = [x for x in animalList if x['head'] == head_type]
        return json.dumps(output)

@app.route('/animals/legs/', methods=['GET'])
def get_animal_legs():
        animal_dict=getdata()
        animalList=animal_dict['animals']
        leg_num=request.args.get('leg_num')
        output=[x for x in animalList if x['legs'] == int(leg_num)]
        return json.dumps(output)

if __name__=='__main__':
        app.run(debug=True, host='0.0.0.0')
