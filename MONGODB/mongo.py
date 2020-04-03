from pymongo import MongoClient

#1.创建数据库连接
conn=MongoClient('localhost',27017)

#２．创建数据库对象
db=conn.stu
#db=conn['stu']

#３．创建集合对象
myset=db.class4

#4.数据操作
# print(dir(myset))

# myset.insert({'name':'张铁林','King':"乾隆"})
# myset.insert([{'name':'张国立','King':'康熙'},\
#     {'name':'陈道明','King':'康熙'}])
# myset.insert_many([{'name':'唐国强','King':'雍正'},\
#     {'name':'陈建斌','King':'雍正'}])

# myset.insert_one({'name':'郑少秋','King':'乾隆'})
# myset.save({'_id':1,'name':'聂远','King':'乾隆'})
# myset.save({'_id':1,'name':'吴奇隆','King':'四爷'})

#查找
# cursor=myset.find({},{'_id':0})

# print(cursor)

# for i in cursor:
#     print(i['name'],'---',i['King'])

# dic=myset.find_one({},{'_id':0})
# print(dic)

#操作符使用
myset1=db.class0

# cursor=myset1.find({'age':{'$gt':16}},{'_id':0})

# for i in cursor:
#     print(i)
#获取下一条
# print(cursor.next())
# print(cursor.next())

# for i in cursor.skip(1).limit(3):
#     print(i)

# for i in cursor.sort([('age',1),('name',-1)]):
#     print(i)

# query={'$and':[{'gender':'w'},{'age':{'$lt':19}}]}

# cursor=myset1.find(query,{'_id':0})
# for i in cursor:
#     print(i)

#修改
# myset1.update({'name':'Levi'},{'$unset':{'sex':''}})

#同时修改多条文档
# myset1.update({'name':'jams'},{'$set':{'age':21}},multi=True)

#如果匹配文档不存在则插入
# myset.update({'name':'梁家辉'},{'$set':{'King':'咸丰'}},upsert=True)

# myset.update_many({'King':'咸丰'},{'$set':{'name':'阿辉'}})

# myset.update_one({'King':'康熙'},{'$set':{'KingName':'玄烨'}})

#删除
# myset.remove({'King':'四爷'})
# myset.remove({'King':'咸丰'},multi=False)

# myset1.remove({'sex':{'$exists':False}})

#复合操作
#查找king=咸丰　并删除
print(myset.find_one_and_delete({'King':'咸丰'}))

#５．关闭连接
conn.close()