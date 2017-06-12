from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
container_name = os.environ['HOSTNAME']
@app.route('/counter')
def hello():

    redis.incr('hits')
    return 'Hello World! I have been seen %s times. I am %s' % (redis.get('hits'), container_name)

@app.route('/')
def gatetes():
    return '<CENTER>GATETES!<BR><img src="http://thecatapi.com/api/images/get?format=src&type=gif"><BR>Server Id: ' + container_name

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
