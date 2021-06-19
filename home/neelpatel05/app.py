from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('data.json') as f:
    data = json.load(f)

@app.route('/',methods=["GET","POST"])
def all():
    if request.method=="GET":
        return jsonify(data)
    else:
        message="method not allowed"
        return jsonify(message=message)

@app.route('/element/atomicnumber',methods=["GET","POST"])
def atomicnumber():
    if request.method == "GET":
        if 'atomicnumber' in request.args:
            atomicnumber = request.args['atomicnumber']
            for i in data:
                if atomicnumber == str(i['atomicNumber']):
                    return jsonify(i)
            else:
                message="does not exists"
                return jsonify(message=message)
        else:
            message="does not exists"
            return jsonify(message=message)
    else:
        message="method not allowed"
        return jsonify(message=message)
        

@app.route('/element/atomicname',methods=["GET","POST"])
def atomicname():
    if request.method == "GET":
        if 'atomicname' in request.args:
            atomicname = str(request.args['atomicname'])
            for i in data:
                if atomicname.lower() == str(i["name"].lower()):
                    return jsonify(i)
            else:
                message="does not exists"
                return jsonify(message=message)
        else:
            message="does not exists"
            return jsonify(message=message)
    else:
        message="method not allowed"
        return jsonify(message=message)


@app.route('/element/symbol',methods=["GET","POST"])
def atomicsymbol():
    if request.method == "GET":
        if 'symbol' in request.args:
            symbol = str(request.args['symbol'])
            for i in data:
                if symbol.lower() == str(i['symbol'].lower()):
                    return jsonify(i)
            else:
                message="does not exists"
                return jsonify(message=message)
        else:
            message="does not exists"
            return jsonify(message=message)
    else:
        message="method not allowed"
        return jsonify(message=message)


@app.route('/element/groupblock',methods=["GET","POST"])
def atomicgroupblock():
    if request.method == "GET":
        data1=[]
        if 'groupblock' in request.args:
            groupblock = str(request.args['groupblock'])
            for i in data:
                if groupblock.lower() == str(i['groupBlock'].lower()):
                    data1.append(i)
            if data1 == []:
                message="does not exists"
                return jsonify(message=message)

            return jsonify(data1)
        else:
            message="does not exists"
            return jsonify(message=message)
    else:
        message="method not allowed"
        return jsonify(message=message)

@app.route('/element/bondingtype',methods=["GET","POST"])
def atomicbondingtype():
    if request.method == "GET":
        data1=[]
        if 'bondingtype' in request.args:
            bondingtype = str(request.args['bondingtype'])
            for i in data:
                if bondingtype.lower() == str(i['bondingType'].lower()):
                    data1.append(i)
            if data1 == []:
                message="does not exists"
                return jsonify(message=message)
            return jsonify(data1)
        else:
            message="does not exists"
            return jsonify(message=message)
    else:
        message="method not allowed"
        return jsonify(message=message)

@app.route('/element/state',methods=["GET","POST"])
def atomicstate():
    if request.method == "GET":
        data1=[]
        if 'state' in request.args:
            state = str(request.args['state'])
            for i in data:
                if state.lower() == str(i['standardState'].lower()):
                    data1.append(i)
            if data1 == []:
                message="does not exists"
                return jsonify(message=message)       
            return jsonify(data1)
        else:
            message="does not exists"
            return jsonify(message=message)
    else:
        message="method not allowed"
        return jsonify(message=message)


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=8080,debug=True)
