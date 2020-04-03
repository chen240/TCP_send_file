#小文见存储方案
#直接转换为二进制格式插入到数据库
from pymongo import MongoClient
import bson.binary

conn=MongoClient('localhost',27017)
db=conn.image
myset=db.MM

# #存储图片
# f=open('mm.jpeg','rb')

# #将图片内容转换为可存储的二进制格式

# content=bson.binary.Binary(f.read())

# #插入到文档
# myset.insert({'filename':'mm.jpeg','data':content})


#提取图片
img=myset.find_one({'filename':'mm.jpeg'})

#将内容写入到本地
with open('mm.jpeg','wb') as f:
    f.write(img['data'])

conn.close()
