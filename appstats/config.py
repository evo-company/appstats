DEBUG = True
UDP_PORT = 9001
UDP_HOST = '127.0.0.1'

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB_NAME = 'appstats'

REDIS_KEYS_PREFIX = 'appstats'
FIELDS = ['cpu_time', 'real_time', 'sql', 'solr', 'redis', 'memcached', 'NUMBER']
