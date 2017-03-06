import redis


class RedisConnection:

    def __init__(self):
        self.redis = self.create_connection()

    def create_connection(self):
        return redis.StrictRedis()

    def get_connection(self):
        return self.redis

