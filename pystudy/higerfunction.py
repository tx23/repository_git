#高阶函数
#变量可以指向函数，函数名也是变量，传入函数参数
#高阶函数，就是让函数的参数能够接收别的函数
def addabs(a, b, f):
    return f(a)+f(b)
print(addabs(-10,3,abs))

#map将传入的函数依次作用到序列的每个元素并返回Iterator。
#可用list将iterator迭代出来
print(list(map(str,[1,2,3,4,5])))#接受参数：函数和Iterable

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，函数接收两个参数
#两个参数分别为上次计算的结果和序列的下一个元素做累积计算
from functools import reduce 
def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))#输出：13579


#把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    if name == '':
        return name 
    chr=name[0].upper()
    chr+=name[1:-1].lower()
    return chr
L0 = []
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


