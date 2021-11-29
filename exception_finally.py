
def func_01():
    pass
    return



if __name__ == '__main__':
    try:
        fh = open('./testfile.txt','w') #'../testfile.txt'
        fh.write('This is exception finally.')
        

    except Exception as e: 
        pass

    finally:
        fh.close()
    
    