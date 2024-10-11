from flask import Flask
import redis
import os
from pymongo import MongoClient

app = Flask(__name__)

# Redis setup
redis_url = os.environ.get('REDIS_URL')
redis_client = redis.Redis.from_url(redis_url)

# MongoDB setup
mongo_url = os.environ.get('MONGO_URL')
mongo_client = MongoClient(mongo_url)
mongo_db = mongo_client['mydatabase']
mongo_collection = mongo_db['mycollection']

@app.route('/')
def index():
    # Example usage of Redis
    redis_client.set('hello', 'world')
    redis_value = redis_client.get('hello')

    # Example usage of MongoDB
    mongo_collection.insert_one({'message': 'Hello from MongoDB!'})
    mongo_doc = mongo_collection.find_one({'message': 'Hello from MongoDB!'})

    return f"Redis says: {redis_value.decode('utf-8')}, MongoDB says: {mongo_doc['message']}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
