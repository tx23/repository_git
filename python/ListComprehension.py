#列表生成器
import os 
print([d for d in os.listdir('.')])#列出当前目录的文件

print([m + n for m in 'ABC' for n in 'XYZ'])#生成全排列

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])#使用两个变量生成list：x=A 

