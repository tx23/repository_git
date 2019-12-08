#class类
class Student(object):
    def __init__(self, name, score, __name):
        self.name = name 
        self.score = score 
        self.__name = __name 
    def printn(self):
        print(self.__name)

bart = Student('tx','99', 'sanjin')
bart.gender='M'
bart.printn()
print(bart.name, bart.score, bart.gender)
#print(bart.__name)  __开头为类的私有成员，不能从外部直接调用
#实现的机制：改名，可能为Student__name了

#隐藏gender对象
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def set_gender(self, gender):
        if (gender != 'male' and  gender != 'female'):
            raise ValueError('Gender should be \'male\' or \'female\'')
        else:
            self.__gender = gender
    def get_gender(self):
        if (self.__gender != 'male' and  self.__gender != 'female'):
            raise ValueError('Gender should be \'male\' or \'female\'')
        else:
            return self.__gender 

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

#统计学生人数，可以给Student类增加一个类属性，
#每创建一个实例，该属性自动增加
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name 
        Student.count+=1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')


