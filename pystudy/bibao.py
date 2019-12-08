#闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():       #函数并非立即执行，而i被保存下来
             return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()#函数并未执行，知道调用f()才执行
print(f1(),f2(),f3())#输出9 9 9
