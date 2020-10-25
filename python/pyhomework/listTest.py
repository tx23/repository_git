#test how to input a list 
l = input("pls input a list:")
li = l.split(' ')
list1 = list(li)
total = 0

for i in range(3):
    total = total + int(list1[i])
print(li,total)

