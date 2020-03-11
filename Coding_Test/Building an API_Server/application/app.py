# App written by Arindam Banerjee #

from flask import Flask
from flask import Response
from flask import jsonify
from flask import request
from datetime import datetime
from flask import render_template
import sys
import os
import json



# Wrong Method Call error code 400
# Not Found error code 404
# Invalid Json error code 405

app = Flask(__name__)
startTime = datetime.now()
Resp = []
Foundlist = []
Updatelist = []
Deletelist = []

# Config route
# Get Method with /
@app.route("/")
def index():
    return render_template("index.html")

# GET Method with /health
@app.route( '/health', methods =['GET'])
def config_health():
    if request.method == 'GET':
        try:
            return Response ("Health Check Ok", status=200, mimetype='application/json')
        except Exception as e:
            print(e)
        finally:
            pass
    else:
        return Response ("Wrong Method Called", status=400 , mimetype='application/json')
# GET Method with /configs
@app.route( '/configs', methods =['GET'])
def config_get():
    if request.method == 'GET':
        try:
            return Response (json.dumps(Resp), status=200, mimetype='application/json')
        except Exception as e:
            print(e)
        finally:
            pass
    else:
        return Response ("Wrong Method Called", status=400 , mimetype='application/json')

# POST Method with /configs
@app.route( '/configs', methods = ['POST'])
def config_post():
    if request.method == 'POST':
        try:
            if request.is_json == True:
                req_json = request.get_json()
                Resp.append(req_json)
                return Response ("Added Data Successfully", status=200, mimetype='application/json')
            else :
                return Response ("Invalid Json", status=405, mimetype='application/json')
        except Exception as e:
            print(e)
        finally:
            pass
    else:
        return Response ("Wrong Method Called", status=400 , mimetype='application/json')

# GET Method with /configs{name}
@app.route( '/configs/<name>', methods = ['GET'])
def config_get_name(name):
    if request.method == 'GET':
        try:
            for item in Resp:
                if item['name'] == name:
                    return Response (json.dumps(item), status=200, mimetype='application/json')
                else:
                    Foundlist.append(item['name'])
                    print('Searching')
            if any(str(name) in s for s in Foundlist):
                print("Argument Found")
            else:
                return Response ("Not Found", status=404, mimetype='application/json')
        except Exception as e:
            print(e)
        finally:
            pass

    else:
        return Response ("Wrong Method Called", status=400 , mimetype='application/json')

# PUT and PATCH Method with /configs{name}
@app.route( '/configs/<name>', methods = ['PUT','PATCH'])
def config_put_name(name):
    if request.method == 'PUT' or request.method == 'PATCH':
        try:
            req_json = request.get_json()
            for item in Resp:
                if item['name'] == name:
                   item.update(req_json)
                   return Response ("Update Successful", status=200, mimetype='application/json')
                else:
                    print("Searching")
                    Updatelist.append(item['name'])
            if any(str(name) in s for s in Updatelist):
                print("Argument Found")
            else:
                return Response ("Not Found", status=404, mimetype='application/json')
        except Exception as e:
            print(e)
        finally:
            pass

    else:
        return Response ("Wrong Method Called", status=400 , mimetype='application/json')

# DELETE Method with /configs{name}
@app.route( '/configs/<name>', methods = ['DELETE'])
def config_delete_name(name):
    if request.method == 'DELETE':
        try:
            #using lambda
            #del_resp = list(filter(lambda i: i['name'] != name, Resp))
            for item in Resp:
                if item['name'] == name:
                    Resp.remove(item)
                    return Response ("Deleted Successful", status=200, mimetype='application/json')
                else:
                    Deletelist.append(item['name'])
            if any(str(name) in s for s in Deletelist):
                print("Argument Found")
            else:
                return Response ("Not Found", status=404, mimetype='application/json')
        except Exception as e:
            print(e)
        finally:
            pass

    else:
        return Response ("Wrong Method Called", status=400 , mimetype='application/json')

# GET Method with /search?metadata.key=value
@app.route( '/search', methods = ['GET'])
def config_get_search():
    if request.method == 'GET':
        try:
            query_byte = request.query_string
            query_str = query_byte.decode('utf-8')
            resp_list = string_manupulation(query_str, Resp)
            if len(resp_list) == 0:
                return Response("Not Found", status=404, mimetype='application/json')
            else:
                return Response (json.dumps(resp_list), status=200, mimetype='application/json')
        except Exception as e:
            print(e)
        finally:
            pass
    else:
        return Response ("Wrong Method Called", status=400 , mimetype='application/json')


def string_manupulation(query_str, response):
    # Local Vars
    final_string = ""
    value = ""
    sub_list = []
    final_resp_list = []
    for thing in query_str.split("="):
        if "." in thing:
          sub_list = thing.split(".")
        else:
          value = str(thing)
    for item in sub_list:
        final_string += "['{}']".format(item)
    command = "object"+final_string
    for object in response:
        if eval(command) == value:
           final_resp_list.append(object)
        else:
           pass
    return final_resp_list

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ['SERVE_PORT'], debug=True)
