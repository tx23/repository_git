#dict的key必须是不可变对象。list不可作为key
d = {'tx':96, 'xt':90, 'ss':66}
print(d['xt'])
d['adam'] = 67
d['xt'] = 91#会把原先的value覆盖掉
#pop(key)删除一个key，同时删除对应的value
print(d)
d.pop('ss')
print(d)

#set不能重复
s = set([1,2,3,2,3,3,4,5])
print(s)
s.add(6)
print(s)
s.remove(1)
print(s)
s2 = set([3,7,8,9])
print(s & s2)
print(s | s2)

#str为不可变对象
a = 'abc'
print(a.replace('a','A'))
print(a)

