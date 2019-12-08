#有序列表tuple，一经初始化就不能修改。
#定义一个元素的tuple，要t=(2,)
t=(1,2)
print(t,t[1])
s=(2,)
print(s)
#可变tuple
w=(1,2,['x','y'])
print(w)
w[2][0] = 'a'
print(w)
