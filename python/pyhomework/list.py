#返回二维列表中最大值的下标
def locateLargest():
    num = eval(input("Enter the number of row in the list:"))
    #边界判断
    if num <= 0:
        print("input illegal")
        return -1
    l = []
    for i in range(num):
        l.append([])
        list1 = input("enter a row:").split(" ")
        for j in range(len(list1)):
            l[i].append(eval(list1[j]))
    answer = [l[0][0], 0, 0]
    #输出
    for x1 in range(num):
        for x2 in range(len(l[num-1])):
            if l[x1][x2] > answer[0]:
                answer[0] = l[x1][x2]
                answer[1] = x1
                answer[2] = x2
    print("The location of the largest element is at (%d, %d)" %(answer[1],answer[2]))

locateLargest()
