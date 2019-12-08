def add(*args):
    total = 0
    for val in args:
        total += val
    return total

if __name__ =='__main__':

    print(add())
    print(add(1))
    print(add(1,2,3))
