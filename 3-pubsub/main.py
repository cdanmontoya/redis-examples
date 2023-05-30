import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

consumer = r.pubsub()

consumer.subscribe('test')

for message in consumer.listen():
    print(message)
    r.publish('uppercase', str(message).upper())