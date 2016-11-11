from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    try:
        for line in open("/proc/self/cgroup"):
            if 'docker' in line:
                container_id = line.split('/')[2]
    except:
        print "error"
    redis.incr('hits')
    return 'Hello World! I have been seen %s times. I am %s' % (redis.get('hits'), container_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
