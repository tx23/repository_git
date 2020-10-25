class Count:
    def __init__ (self, count = 0):
        self.count = count 
def main():
    c = Count()
    times = 0
    for i in range(3):
        print("before: times id:", id(times), "times = ", times)
        print("count id:", id(c.count), "count = ", c.count)
        times+=1
        c.count+=1
        print("before: times id:", id(times), "times = ", times)
        print("count id:", id(c.count), "count = ", c.count)
#       increment(c, times)

    print("count is ", c.count)
    print("time is", times)

def increment(c, times):
    print("before: times id:", id(times), "times = ", times)
    print("count id:", id(c.count), "count = ", c.count)
    c.count += 1
    times += 1
    print("after:times id:", id(times), "times = ", times)
    print("count id:", id(c.count), "count = ", c.count)

main()
