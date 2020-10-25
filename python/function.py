import math
def quadratic(a, b, c):
    x1=math.sqrt(b*b - 4*a*c)
    nx = (-b+x1)/(2*a)
    ny = (-b-x1)/(2*a)
    return nx, ny
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


#默认参数
def power(x, n=2):
    y=1
    while n>0:
       y=y*x
       n=n-1
    return y
print(power(4), power(3,3))
#l为变量，[]为可变对象，将其设为默认参数时，
#l指向[]，若改变了[]的内容，默认参数的内容就改变了
def add_end(l=[]):
    l.append('end')
    return l
print(add_end())
print(add_end(['a']))
print(add_end())
print(add_end(['a']))
print(add_end())

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end2())
print(add_end2())

