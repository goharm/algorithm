def func_callback(input, extend_input):
    print('func_callback sum : ', input)
    print('extend', extend_input)
    return

def func_call(one, two, f_callback):
    result = one + two
    f_callback(result)
    return


first = 10
second = 20
third = 30
func_call(first, second, func_call, third)