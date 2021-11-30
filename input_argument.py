import argparse

args = argparse.ArgumentParser()
# '-'는 shortcut, '--'는 longcut
# required = True 는 뒤에 분명하게 값이 들어가지 않으면 에러가 난다.
args.add_argument('-x', '--xValue', required='True')
# args.add_argument('-z', '--zValue', required='False')

arg_var = vars(args.parse_args())

pass