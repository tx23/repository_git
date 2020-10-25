from abstest import my_abs
print(my_abs(-10))

#如果没这个pass，会报错。 
if(True):
    pass
else:
    print("pass")

#isinstance()
name=input("pls input your name")
name=int(name)
if not isinstance(name, str):
    raise TypeError('bad operand type')
else:
    print("hello,", name)
