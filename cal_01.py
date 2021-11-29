a = 50 
b = 20
c = 10
d = 0


def add(a,b):
    sum = a + b
    return sum

def mult(c,d):
    mul = c * d
    div = c / d
    return mul, div


if __name__ == '__main__':
    try:
        print(add(a,b))
        print(mult(c,d))
    except ZeroDivisionError: 
        d = 1
        print(add(a,b))
        print("변수 변경 => d = 1")
        print(mult(c,d))
        pass
    
    