list1=[1,2,3]
print(id(list1.sort()))
print(id(list1))
classmates = ['ming','karsa','uzi']
#classmates[-2]即倒数第二个
if('uzi' in classmates):
    print("uzi in classmates")
print(classmates, len(classmates), classmates[0], classmates[-2])
classmates.append('langx')#往list中追加元素到末尾
print(classmates)
import random
random.shuffle(classmates)
print("after random:", classmates)
classmates.insert(2,'xiaohu')#元素插入到指定的位置
print(classmates)
classmates.pop()#删除list末尾元素
classmates.pop(1)#删除指定位置元素
classmates[1]='mlxg'
print(classmates)
s = ['py', 520, ['php', 23], 'cpp']
print(s[2][1])#打印23

#切片操作，支持list和tuple
#正向切片
l = ['langx', 'karsa', 'xiaohu', 'uzi', 'xiaoming']
print(l[0:3]) #从l[0]开始到l[3],不包括l[3]
print(l[:3]) #其中0可省
print(l[1:3])
print(l[-2:])#倒数切片，-1可省略
#前5个数每2个取一个
print(l[:5:2])

#tuple,字符串也可进行切片操作
print((0, 1, 2, 3, 4, 5)[:3])
print('ABCDEFG'[:3])

#去除一个字符串首尾空格的函数
def trims(string):
    leng = len(string)
    lenge = leng
    if leng == 0:
        return string
    nx = 0
    ny = 0
    while leng > 0:
        if string[leng-1] == ' ':
            ny=ny+1
            leng = leng - 1
        else:
            break 
    string = string[0:lenge-ny]
    lenge = len(string)
    for i in string:
        if i == ' ':
            nx=nx+1
        else:
            break 
    return string[nx:lenge]
#简易版
def trim(string):
    while string[:1] == ' ':
        string=string[1:]
    while string[-1:] == ' ':
        string=string[:-1]
    return string


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
    

