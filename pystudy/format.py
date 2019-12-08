#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('100+200 = ', 100+200)
#name = input('pls input your name \n')
#print('hello, ', name)
print("I'm OK") #when you have a ',use "".
print("\"I\'m OK\"")#when you have ' and ",use \
print(r"i'm ok \n") #用r''表示''内部的字符串默认不转义
print('''line1
line2
line3''') #用'''...'''的格式表示多行内容
if(5>3 and 2>1):
    if(2>1 or 1>2):
        if(not False):
            print('true')


a='abc'
b=a
a='123'
print('a=',a,'b=',b)


print(10/3, 10//3, 10%3) #/的结果是浮点数，//的结果是整数


#编码规则
#ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('中'))
print(chr(25991))
print('\u4e2d\u6587')#知道字符的整数编码可用十六进制写
y='ABC'
x=b'ABC'#内容显示一样，但bytes的每个字符只占用一个字节。 

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))#以Unicode表示的str通过encode()可编码为的bytes
print(b'ABC'.decode('ascii'))#从网络或磁盘读取字节流为bytes，把bytes变为str，就需要用decode()方法

#len()函数计算str的字符数，如果换成bytes，len()函数就计算字节数
print(len('ABC'))
print(len('中文'.encode('utf-8')))

#格式化输出
print('hello,%s' % 'tangxin')#一个%？可不用括号
print('hi,%s, you have $%d.' % ('tx',100000))
print('%5d-%05d' % (3, 1))#%5d5位数不补0，后面一个补0
print('%.2f' % 3.1415926)#2位小数
print('growth rate: %d %%' % 7)
#format()
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
