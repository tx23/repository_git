#排序
l = [2, 4, -3, 1, 9, -5]
s=sorted(l, key=abs)
print(s)
#忽略大小写，倒序
print(sorted(['bob', 'about', 'Zoo'], key=str.lower, reverse=True))

#自定义排序
def by_name(t):
    return t[0:-1][0]
def by_score(t):
    return t[1]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score)
print(L2)
print(L3)
