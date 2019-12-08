#生成器
#1、把一个列表生成式的[]改成()，就创建了一个generator：
g = (x * (x+1) for x in range(10))
#print(g)无法打印出生成器，只能用next获得。调用时才计算值。
for n in g:
    print (n)


#2、yield返回，下次从前一个yield开始
#斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b#t=(b, a+b);a=t[0];b=t[1]
        n = n + 1
    return 'done'
for n in fib(6):
    print(n)

#杨辉三角
def triangles():
    l=[1]
    while True:
        yield l
        #要用range生成一个list才能迭代
        l=[l[i-1]+l[i] for i in range(len(l))] + [1]
        l[0] = 1
#测试
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

