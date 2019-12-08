#f = open('./function.py', 'r')
#print(f.read())
#f.close

#通过with不必调用close和错误检测
with open('./function2.py', 'r') as f:
    print(f.readline())
    print(f.readline())
with open('./test.txt', 'w') as f:#会新建一个文件,或覆盖原文件
    f.write('Hello, 唐鑫!')
