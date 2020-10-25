#定制类
class Student(object):
    def __init__(self, name):
        self.name=name
    def __str__(self):#类的实例调用str
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__#直接显示变量调用repr
print(Student('tx'))


#令一个类成为迭代对象，须实现一个__iter__()方法
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)


#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法

#调用类的方法或属性时，若不存在.通过__getattr__(self, 'score')来尝试获得属性
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__ 
#print(Chain().status)
print(Chain().status.user.timeline.list)


#已有的属性，比如name，不会在__getattr__中查找。

#__call__直接在实例本身上调用，如s()
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('tx')
s()#现可直接在实例上调用

