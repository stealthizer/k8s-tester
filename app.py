from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')

def GetContainerName():
    try:
        for line in open("/proc/self/cgroup"):
    except:
        return "error"
    else:
        if 'docker' in line:
    return line

def hello():
    redis.incr('hits')
    container_name = GetContainerName()
    return 'Hello World! I have been seen %s times. I am %s' % (redis.get('hits'), container_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
