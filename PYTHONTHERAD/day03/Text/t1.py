def generate(numRows):
    r = [[1]]
    for i in range(1,numRows):
        r.append(list(map(lambda x,y:x+y, [0]+r[-1],r[-1]+[0])))
    return r[:numRows]

if __name__=='__main__':
    a=generate(10)
    for i in a:
        print(i)
# ————————————————
# 版权声明：本文为CSDN博主「超级大黄狗Shawn」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_41084236/article/details/81564963