second = 50

def func01():
    first = 10
    func02()
    return

def func02():
    first = 20
    return

if __name__ == '__main__':
    first = 30
    func01()
    pass