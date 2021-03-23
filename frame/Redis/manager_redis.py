import redis

host = 'localhost'
port = 6379
password = '123456'

redis_db = redis.Redis(host=host, port=port,
                       password=password,
                       decode_responses=True)
# string
redis_db.set('foo', 'bar')
print("foo:", redis_db.get('foo'))
# print(redis_db.delete('foo'))

# hash
token_map = {'name': 'coco', "addr": "海珠", "phone": "135"}
redis_db.hmset("token", token_map)
name = redis_db.hget('token', 'name')

*ignore, addr, phone = redis_db.hmget('token', token_map.keys())

new_token_map = redis_db.hgetall('token')
print(new_token_map)
print("name:", name)
print("addr:", addr, "phone:", phone)

# list(stack)
cars = ['toyota', 'honda', 'coli', 'BMW', 'audi', 'benz']
redis_db.delete('cars')
redis_db.lpush('cars', cars[0])
redis_db.lpush('cars', *cars[1:])
new_list = redis_db.lrange('cars', 0, 2)
new_list1 = redis_db.lrange('cars', 3, 10)
print(new_list, new_list1)

# set
redis_db.sadd('color', 'red')
redis_db.sadd('color', 'red')
new_set = redis_db.smembers('color')
print(new_set)

# zset
redis_db.zadd('animal', {"panda": 0})
redis_db.zadd('animal', dict(white_cat=1, black_cat=2))
redis_db.zadd('animal', {'panda': 3})
new_zset = redis_db.zrange('animal', 0, 10)
print(new_zset)
new_zset = redis_db.zrange('animal', 0, 10, withscores=True)
print(new_zset)

# 事务
with redis_db.pipeline() as pipe:
    try:
        pipe.watch('key1')
        pipe.multi()
        pipe.set('key2', 2)
        pipe.incr('key1')   # +=1，仅对number的字符串有效
        pipe.set('key3', 3)
        pipe.execute()
    except redis.exceptions.WatchError as e:
        print('无法更新')
    except redis.ConnectionError as e:
        print('connect error.')
    except redis.TimeoutError as e:
        print('connect timeout. ')
