#for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['tx', 'xt', 'txx', 'xxt']
for x in names:
    print(x)

#range(n)函数,生成一个小于n的整数序列
s=list(range(100))
sum = 0
for n in s:
    sum = sum + n
print(sum)

#while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#break 退出循环
n = 1
while n < 100:
    if n > 9:
        break 
    print(n) 
    n = n + 1
print ('end')

#continue 跳过当前循环，开始下次循环
n = 0
while n < 10:
    n=n+1
    if n%2 == 0:
        continue 
    print (n)
