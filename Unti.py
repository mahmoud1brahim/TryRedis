#a method that saves image to redis
def save_image(image_url, image_name):
    import requests
    from PIL import Image
    from io import BytesIO
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

    #get the image
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    #save the image
    image.save(image_name)
    redis_conn.set(image_name, open(image_name, 'rb').read())
    sleep(2)
    print('Image saved to redis')

save_image('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png', 'google.png')

