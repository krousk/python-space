#
#예외처리(excepton)
#스크립트 실행중 불가항력의 상황에 따라 스크립트 제어가 비정상 종료되는 상황을 정상적으로 종료할 수 있게 하는 제어문.
#

#*error 종류*
#syntax error: 문법 오류
#link error: 함수 오류
#run-time error: logic 오류. 가장 해결이 어려움.
#warning: error 가능성이 있다.

#예외상황
#a,b=5,0
#c=a/b
#c=a/b #zero diveison error: division by zero 라는 exception

#print(4+spam*3) $#ameError: name 'spam' is not defined. 즉 spam이라는 변수가 없다.

#print('2'+2 ) #type error: can only concatenate str(nor "int") to srt

#print("hello, world") link error

#print('hello) syntax error

#https://docs.python.org/3/library/exceptions.html?hierarchy
#object: 객체. 현실세계의 모든 것.
#class: object에 대한 template(틀)

'''
x=0
try:   #예외발생 가능성이 있는 코드 블록을 묶어주는 역활. try: 블록 안에 있는 코드에서 예외가 발생하면 해당 예외를 감지할 수 있다.
    print(1.0/x)
except ZeroDivisionError:   #예외가 감지되었을 때 수행되는 코드블록
    print('zero division exception')
    print('stop script')
'''
'''
try:
    print('2'+2)
except TypeError:
    print('연산시 자료형이 맞지 않습니다.')
    print('stop script')
'''
'''
name='filename'
try:
    f=open(name, 'r')
except IOError:   #예외가 발생했을 때 처리 내용
    print(name+'파일을 열 수 없습니다.')
    print('stop script')
else:  #예외가 발생하지 않았을 때 처리
    print(name, 'has', len(f.readline()), 'lines')
    f.close()
finally:  #예외가 발생하거나 발생하지 않거나 항상 수행되는 코드블록. 무조건 실행.
    print('예외와 상관없이 항상 수행하는 내용을 정의한다.')
'''

try:
    spam()
except NameError:
    print('Exception : NameError')
except TypeError:
    print('Exception : TypeError')
except IOError:
    print('Exception : IOError')
except:
    print('Exception 발생으로 스크립트 종료')
#except는 모든 예외를 감지하는 함수. 그래서 순서가 중요함. 제일 앞에 두면 나머지 것들은 의미가 없으니까.