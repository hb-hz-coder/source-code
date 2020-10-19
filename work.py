from redis import Redis

redis_conn = Redis()

# redis_conn.lpush("l1", *["a", "b", "c", "d", "e"])
# result = redis_conn.lrange("l1", 0, -1)
# print(result)
# redis_conn.ltrim("l1", 0, 2)
# result = redis_conn.lrange("l1", 0, -1)
# print(result)
result = redis_conn.llen("l1")
print(result)
