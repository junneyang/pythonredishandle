#!/usr/bin/env python
# coding=utf-8

import redis

#创建连接池
pool=redis.ConnectionPool(host='localhost',port=16379,db=0)
r=redis.Redis(connection_pool=pool)
#创建pipeline，数据批量入库
pipeline=r.pipeline()

pipeline.set('ABC','ABC')
pipeline.execute_command('set','DEF','DEF')

pipeline. execute()

print r.keys('*')
print r.get('ABC')
print r.execute_command('get','ABC')

