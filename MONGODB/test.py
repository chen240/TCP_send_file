from pymongo import MongoClient
from random import randint

conn=MongoClient('localhost',27017)

db=conn.grade

myset=db.class1

cursor=myset.find()
for i in cursor:
    myset.update({'_id':i['_id']},\
            {'set':{'score':\
            {'chinese':randint(60,100),\
            'math':randint(60,100),\
            'english':randint(60,100)}}})

l1=([{'$group':{'_id':'$gender','num':{"$sum":1}}}])
l2=
cursor=myset.aggregate
conn.close()