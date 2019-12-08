#递归函数
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#尾递归,函数返回的时候，调用自身，且return语句不能包含表达式
def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, pro):
    if num == 1:
        return pro 
    else:
        return fact_iter(num-1, pro*num)

print(fact(6))

#汉诺塔问题
def hanoi(n, a, b, c):#n个盘，从a移动到c
    if n==1:
        print(a, '--->', c)
    else:
        hanoi(n-1, a, c, b)#先将上面n-1个盘移动到b
        print(a, '--->', c)#再将最下面那个移动到c
        hanoi(n-1, b, a, c)#最后将上面n-1个盘从b移动到c
hanoi(3, 'a', 'b', 'c')
