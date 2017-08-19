__author__ = 'cc'

import redis

redis_cli = redis.StrictRedis()
redis_cli.incr("jobbole_count")  # 变量加一操作
