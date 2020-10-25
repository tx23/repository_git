d = {'a':1, 'b':2, 'c':3}
for k in d:#迭代key
    print(k)
for v in d.values():#迭代value
    print(v)
for k, v in d.items():#同时迭代key和value
    print(k, v)

#迭代字符串
for ch in "ABC":
    print(ch)

#如何判断迭代对象
#通过collections模块的Iterable类型判断
from collections.abc import Iterable
print(isinstance('abc', Iterable)) # str是否可迭代
print(isinstance(123, Iterable)) #123是否可迭代

#Python内置的enumerate函数可以把一个list变成索引-元素对
for i,v in enumerate([1,3,4,5,6]):
    print(i,v)
for x,y in enumerate([(1,1),(2,4),(3,6)]):
    print(x,y)

#通过迭代查找list的最小最大值，并返回一个tuple
def findMinAndMax (lists):
    if lists == []:
        return (None,None)
    mi = lists[0]
    ma = lists[0]
    for i in lists:
        if i < mi:
            mi = i
        if i > ma:
            ma = i
    return (mi, ma)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
