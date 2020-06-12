#
#mymodule
#
def myFunc():
    print('My Function->myFunc()')

def myPrint(values):
    column_count=1
    for value in values:
        print('{}\t'.format(value),end='')
        column_count+=1
        if column_count>10:
            print()
            column_count=1

if __name__=='__main__':
    myFunc()
    myPrint([1,2,'apple','banana',10.5,3,4,5,6,7,8,9,10])