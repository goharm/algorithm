def func01() :
    func02()
    return

def func02() :
    func03
    return

def func03() :
    return


if __name__ == '__main__' :
    func01()

    pass