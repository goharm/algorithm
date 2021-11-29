


def add(a,b):
    sum = a + b
    return sum

def mult(c,d):
    mul = c * d
    div = c / d
    return mul, div


if __name__ == '__main__':
    try:
        a = 50 
        b = 20
        c = 10
        d = 0
        mul, div = mult(c,d)
        print(add(a,b))
        print(mul)
        print(int(div))

    except ZeroDivisionError: 
        d = 1
        print(add(a,b))
        print("변수 변경 => d = 1")
        mul, div = mult(c,d)
        print(add(a,b))
        print(mul)
        print(int(div))
        pass
    
    