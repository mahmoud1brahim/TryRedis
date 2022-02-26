#a method that publish to redis channel
def publish_to_redis(channel, message):
    from redis import Redis
    from redis.exceptions import ConnectionError
    from time import sleep

    #connect to redis
    redis_conn = Redis(host='127.0.0.1', port=6379)
    try:
        redis_conn.ping()
    except ConnectionError:
        print('Redis server not available')
        return
    redis_conn.publish(channel,message)
    sleep(2)
    print('message published to redis channel')

#publish_to_redis('MQAtHome','Hello')

#a method that subscribes to redis channel
def subscribe_to_redis(channel):
    from redis import Redis
    from redis.exceptions import ConnectionError
    from time import sleep

    #connect to redis
    redis_conn = Redis(host='127.0.0.1', port=6379)
    try:
        redis_conn.ping()
    except ConnectionError:
        print('Redis server not available')
        return
    redis_s = redis_conn.pubsub()
    redis_s.subscribe(channel)
    redis_s.get_message()
    messages = redis_s.get_message()['data']
    print(messages)
    sleep(2)
    print('subscribed to redis channel')

#subscribe_to_redis('MQAtHome')


#a method that suscribes to redis channel (the real deal)
def sub(channel):
    from redis import Redis
    from redis.exceptions import ConnectionError
    from time import sleep

        #connect to redis
    redis_conn = Redis(host='127.0.0.1', port=6379,charset="utf-8", decode_responses=True)
    try:
        redis_conn.ping()
    except ConnectionError:
        print('Redis server not available')
        return

    pubsub = redis_conn.pubsub()
    pubsub.subscribe(channel)

    #redis_conn.publish(channel,"sub/pub/inception")
    for message in pubsub.listen():
        if message.get("type") == "message":
            data = message.get("data")
            print(data)


from multiprocessing import Process

if __name__ == "__main__":
    Process(target=sub, args=("broadcast",)).start()