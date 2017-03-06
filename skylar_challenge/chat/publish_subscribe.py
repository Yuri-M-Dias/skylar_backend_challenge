from skylar_challenge.db.redis import redis_connection


# TODO: Strategy model
class ChatRedis:
    """
    Publish-Subscribe chat model using redis connection.
    """
    CHANNEL_NAME = 'chat'

    def __init__(self):
        self.redis_connection = redis_connection.RedisConnection().get_connection()
        self.pub_sub = self.redis_connection.pubsub(ignore_subscribe_messages=True)

    def send(self, message='Hello'):
        sended_to = self.redis_connection.publish(self.CHANNEL_NAME, message)
        return sended_to

    def receive(self, channel=CHANNEL_NAME):
        self.pub_sub.subscribe(channel)
        message = self.pub_sub.get_message(timeout=10)
        if message is not None:
            return message['data']
        return None
