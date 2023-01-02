#coding= utf-8

from flask import *
import time
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': ' --API_andre Successfully loaded page HOME', 'Timestamp' : time.time()}
    json_ = json.dumps(data_set)

    return json_


@app.route('/user/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user'))
    data_set = {'Page': 'Request', 'Message': f' --API_andre Successfully got request {user_query}', 'Timestamp': time.time()}
    json_ = json.dumps(data_set)

    return json_

if __name__ == '__main__':
    app.run(port=7777)


