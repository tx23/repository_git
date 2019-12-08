#可变参数,在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
   # print(numbers[0],numbers[1],numbers[2])
    for n in numbers:
        sum = sum + n*n
    return sum 
print(calc(1,2,3))

nums=[2,3,4]
print(calc(*nums))#已经有一个list时的调用


#关键字参数，在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:',name,'age:',age,'other:',kw)
person('tx', 22, city='gz')
extra={'city':'gz', 'job':'engineer'}
person('tom', 23, **extra)


#命名关键字参数，如无可变参数则要*做分割符，若无*则为位置参数
#可限制关键字参数的名字
def person(name, age, *, city, job):
    print(name, age, city, job)
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
arg=[1,2,3]
person('tangxin', 18,*arg, job='haha', city='gz')
#命名关键字参数须传入参数名，这和位置参数不同。
#如果没有传入参数名，调用将报错
#person('Jack', 24, 'Beijing', 'Engineer')报错

#参数顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用

