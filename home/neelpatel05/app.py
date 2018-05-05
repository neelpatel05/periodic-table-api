from flask import Flask
from flask import request
from flask import jsonify
import json
from pprint import pprint

app = Flask(__name__)

with open('data.json') as f:
    data = json.load(f)

pprint(data)

@app.route('/')
def all():
    return jsonify(data)

@app.route('/element/atomicnumber')
def atomicnumber():
    if 'atomicnumber' in request.args:
        atomicnumber = request.args['atomicnumber']
        for i in data:
            if atomicnumber == str(i['atomicNumber']):
                return jsonify(i)
        else:
            return jsonify({"message":"Does not exists"})
    else:
        return jsonify({"message":"Does not exists"})

@app.route('/element/atomicname')
def atomicname():
    if 'atomicname' in request.args:
        atomicname = str(request.args['atomicname'])
        for i in data:
            if atomicname.lower() == str(i["name"].lower()):
                return jsonify(i)
        else:
            return jsonify({"message":"Does not exists"})
    else:
        return jsonify({"message":"Does not exists"})


@app.route('/element/symbol')
def atomicsymbol():
    if 'symbol' in request.args:
        symbol = str(request.args['symbol'])
        for i in data:
            if symbol.lower() == str(i['symbol'].lower()):
                return jsonify(i)
        else:
            return jsonify({"message":"Does not exists"})
    else:
        return jsonify({"message":"Does not exists"})


@app.route('/element/groupblock')
def atomicgroupblock():
    data1=[]
    if 'groupblock' in request.args:
        groupblock = str(request.args['groupblock'])
        for i in data:
            if groupblock.lower() == str(i['groupBlock'].lower()):
                data1.append(i)
        else:
            data1.append({"message":"Does not exists"})

        return jsonify(data1)
    else:
        return jsonify({"message":"Does not exists"})

@app.route('/element/bondingtype')
def atomicbondingtype():
    data1=[]
    if 'bondingtype' in request.args:
        bondingtype = str(request.args['bondingtype'])
        for i in data:
            if bondingtype.lower() == str(i['bondingType'].lower()):
                data1.append(i)
        else:
            data1.append({"message":"Does not exists"})       
        return jsonify(data1)
    else:
        return jsonify({"message":"Does not exists"})

@app.route('/element/state')
def atomicstate():
    data1=[]
    if 'state' in request.args:
        state = str(request.args['state'])
        for i in data:
            if state.lower() == str(i['standardState'].lower()):
                data1.append(i)
        else:
            data1.append({"message":"Does not exists"})       
        return jsonify(data1)
    else:
        return jsonify({"message":"Does not exists"})


if __name__ == '__main__':
    app.run()
