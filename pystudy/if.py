#if语句从上往下判断，如果在某个判断True,
#把该判断对应的语句执行后，忽略掉剩下的elif和else
age = 60
if age < 12:
    print('teenager')
elif age > 18: 
    print('adult')#执行该句跳出循环
else:
    print('old')

#input输入的为string，判断时需转换相应格式
birth=input("birth:")
s = int(birth)
if s<2000:
    print('00前')
if s>2000:
    print('00后')
