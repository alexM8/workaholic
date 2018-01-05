from config import *
from flask import Flask, request
from flask_restful import Api
from sqlalchemy import create_engine
import sys

db_connect = create_engine('mysql://%s:%s@%s/%s' % (user, password, host, dbname))
app = Flask(__name__)
api = Api(app)


@app.route(location + "/data", methods=['POST'])
def post():
    conn = db_connect.connect()  # connect to database
    try:
        working_type = int(request.form['kind'])
    except:
        sys.stderr.write("Working transformation fail. Will set to 0")
        working_type = 0
    if working_type > 1 or working_type < 0:
        sys.stderr.write("Working value out of bounds. Will set to 0")
        working_type = 0
    sql = 'insert into workaholic (working, timestamp) values (%s, NOW())' % str(working_type)
    query = conn.execute(sql)
    if query:
        return 'ok'
    else:
        return 'not ok'


if __name__ == '__main__':
    app.run(port)
