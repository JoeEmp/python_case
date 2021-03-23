# 启动本地redis
docker run -d -p 6379:6379 --name case_redis redis redis-server --appendonly yes --requirepass '123456'