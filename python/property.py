#面向对象高级编程，使得既可以简单调用又能限制属性
#原方法

class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value 

#使用起来不方便
stu=Student()
stu.set_score(60)
print(stu.get_score())

#property方法，加上width和height属性，以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
        return self._width 
    @width.setter 
    def width(self, value):
        self._width=value 

    @property
    def height(self):
        return self._height 
    @height.setter 
    def height(self, value):
        self._height=value 

    @property 
    def resolution(self):
        return self._width*self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')



