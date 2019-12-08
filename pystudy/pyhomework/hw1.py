#hw1：输入一个整数判断是否为回文数

num = int(input("Pls enter a three-digit integer："))
if (num < 100 or num > 999):
    print("sorry, you enter a invalid number.")
else:
    num = str(num)
    if(num[0] == num[-1]):
        print(num, "is a palindrome")
    else:
        print(num, "is not a palindrome")

