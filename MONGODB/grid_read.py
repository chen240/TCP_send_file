#获取grid方案存放到数据库中的文件

from pymongo import MongoClient
import gridfs

conn=MongoClient('localhost',27017)
db=conn.grid

#获取grids对象
fs=gridfs.GridFS(db)

files=fs.find()

#分别取每一个文件
for file in files:
    #打印每个文件名称
    print(file.filename)
    if file.filename=="mm.jpeg":
        with open(file.filename,'wb') as f:
            #从数据库里面读取内容
            data=file.read()
            #写入到本地
            f.write(data)
conn.close()