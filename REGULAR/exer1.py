import re

f=open('test.txt')

# pattern=r'[A-Z]\w*' #以大写字母为开头

pattern=r'-?\d+\.?/?\d*%?'

l=[]

for line in f:
    l+=re.findall(pattern,line)

print(l)
