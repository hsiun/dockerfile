from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host="redis_1", port=6379)

@app.route('/')
def hello():
	redis.incr('hits')
	return 'Hello, I am in docker container! I have been seen (0) times'.format(redis.get('hits'))

if __name__ == "___main__":
	app.run(host="0.0.0.0", debug=True)

