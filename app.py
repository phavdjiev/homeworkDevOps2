import os
import redis
from flask import Flask, jsonify

app = Flask(__name__)

# Load Redis configuration from environment variables
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.route('/')
def home():
    return "Welcome to my DevOps app!"

@app.route('/visit')
def visit():
    try:
        visits = redis_client.incr('visit_count')
        return f"Number of visists: (visits)"
    except redis.RedisError as e:
        return f"Redis error: {e}", 500

@app.route('/health')
def healt():
    try:
        redis_client.ping()
        return "Redis connection ready", 200
    except redis.RedisError:
        return "Redis connection failed", 500

if __name__ == 'main':
    app.run(host='0.0.0.0', port=5000)
