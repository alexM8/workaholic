from config import *
from flask import Flask, request, Response
from flask_restful import Api
from sqlalchemy import create_engine
import sys

db_connect = create_engine('mysql://%s:%s@%s/%s' % (user, password, host, dbname))
app = Flask(__name__)
api = Api(app)


@app.route(location + "/data", methods=['POST'])
def post():
    conn = db_connect.connect()
    try:
        working_type = int(request.form['kind'])
    except:
        sys.stderr.write("Working value transformation fail. Will be set to 0\n")
        working_type = 0
    if working_type > 1 or working_type < 0:
        sys.stderr.write("Working value out of bounds. Will be set to 0\n")
        working_type = 0
    conn.execute('insert into workaholic (working, timestamp) values (%s, NOW())' % str(working_type))
    return Response("{'status':'ok'}", status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(port)
