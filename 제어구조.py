#번외:알고리즘 0개 이상입력,1개 이상 출력, 유한성(1회 이상 동작),유효한 표현, 효과적이어야 한다.


#제어구조
#:프로그램의 구조를 결정
#1.순차구조: 위에서 아래로 차례대로 명령을 실행하는 구조
#2.선택구조: 조건 판단의 결과에 따라 실행방향을 결정하는 구조
#3.반복구조: 정해진 횟수나 조건에 따라 일정한 명령집합(코드블록)을 반복해서 실행하는 구조
#
#프로그램을 자료형, 연산자, 제어문을 활용하여 문제어서 요구하는 사항을 해결하는 명령집합(코드블록)이다.
#
#선택구조(if~elif~else)
#if<조건식1>:
#   <명령문1> ->조건식1이 참일 때 수행
# [elif<조건식2>:]
#       <명령문2> ->조건식2가 참일 때 수행
# [else:]
#      <명령문3> ->모든 조건이 만족하지 않을 때 수행.
#선태구조 형태
#1.단순선택구조 ->if만 사용
#2.양자택일구조 ->if~else
#3.다중선택구조 ->if~[elif...]~else
#
number=10
if number>0:
    print("yes, sir!!!\n")

if number !=0 and number>0:
    print("yes, sir!!!")
    print("number:{}\n".format(number))

number=-10
if number !=0 and number>0:
    print("yes, sir!!!")
print("number:{}\n".format(number))

#3 다중선택
if number!=0 and number>0:
    print("positive")
elif number!=0 and number<0:
    print("Negative")
else:
    print("zero")
print("number:{}\n".format(number))

order='spagetti'
if order=='spam':
    price=500
elif order=='ham':
    price=700
elif order=='egg':
    price=100
elif order=='spagetti':
    price=1000
else:
    price=0
print("order:{}\nprice:{}\n".format(order,price))

#2.양자택일구조
lunch='먹는다'
if lunch=='먹는다':
    print("살찌겠군!!!\n")
else:
    print("몸 망가지겠군!!!\n")

#선택 구조 대신에 dict를 사용하는 것이 더 편리할 때도 있다.
#이 형태가 가장 파이썬수러운 코드.
order='spam'
menu={'spam':500, 'ham':700, 'egg':100, 'spagetti':1000}
price=menu.get(order,0)
print("order:{}\tprice:{}\n".format(order,price))

#삼항 연산자를 이용한 선택
if price>=500:
    message="VIP"
else:
    message="non VIP"
    print("order:{}\tprice:{}\t{}\n".format(order,price,message))

#삼항 연산자(양자택일일 경우에 사용)
#        참          조건          거짓
message="VIP" if price>=500 else "non VIP"
print("order:{}\tprice:{}\t{}\n".format(order,price,message))

#선택구조 실습
#1. 정수 5개를 list에 기억시킨 후 가장 큰 수와 가장 작은 수를 출력하는 파이썬 스크립트
#2. 3개의 정수를 각각의 변수로 입력한 후, 큰 수, 중간 수, 작은 수 순으로 출력하는 파이썬 스크립트

#1
numbers=[9,7,3,5,2]
print("numbers:{}({})".format(numbers,len(numbers)))
max=min=numbers[0]

if max<numbers[1]:
    max=numbers[1]
if max<numbers[2]:
     max=numbers[2]
if max<numbers[3]:
    max=numbers[3]
if max<numbers[4]:
    max=numbers[4]

if min > numbers[1]:
    min = numbers[1]
if min > numbers[2]:
    min = numbers[2]
if min > numbers[3]:
    min = numbers[3]
if min > numbers[4]:
    min = numbers[4]

print("max: {}\tmin: {}\t".format(max,min))


#2

#반복구조
#1.for문 : 반복 횟수가 일정한 경우 사용
#2.while문: 반복 횟수가 일정하지 않은 경우 사용

#1.for문
#for <반복제어변수> in <반복 횟수를 결정하는 객체(sequence형)>:
#   <반복 수행 내용>
#
l=['cat','cow','tiger']
print('l:{}({})\n'.format(l,len(l)))

for value in l:
    print('value: {}({})'.format(value,len(value)))

print()
for i in range(0, len(l),2):
    print(i,end='\t')
    print('value:{}({})'.format(l[i],len(l[i])))

print()
for i in range(1,11,1):
    print(i,end=' ')
print()

str='python is great!!!'
for value in str:
    print(value, end=' ')
print()

for i in range(len(str)):
    print(str[i],end= ' ')
print()
#같은 방법이지만 구현방법의 차이만 있을 뿐, 결과는 같다.

t=(100, 'hello',True,'Hong')
print('\nt: {}({})\n'.format(t, len(t)))

for value in t:
    print(value, end=' ')
print()

for i in range(len(t)):
    print(t[i], end=' ')
print()

#enumerate():요소의 값과 인덱스를 제공하는 함수
#            (인덱스,요소값)형식으로 tuple로 제공
for i, value in enumerate(l):
    print('i:{}\tvalue:{}'.format(i, value))
print()

#break: 반복을 탈출할 때 사용
#continue: 반복 조건 검사 수행
for i in range(1,101,1):
    if(i%10)==0:
        continue
    if(i>=20):
        break
    print('{:5d}'.format(i),end='')
#반복 횟수가가 결정된 경우 사용

#
#2.while문
#반복제어변수 초기화
#while  <반복탈출 조건>
#   <반복수행내용>
#   반복제어변수 변화
#
print()
i=1                            #반복제어 변수 초기화
while i <=10:                  #반복탈출 조건 검사
    print(i, end=' ')
    i +=1                       #반복 제어 변수 변화
print()

i=1
while True:
    if(i>10):
        break;
    print(i,end=' ')
    i += 1
print()
#가능한 이 방법은 안 쓰는 쪽으로.

#2-read 기법
i=1;
str=input('Input string(quit:"end"):')
while str.lower() !='end':
    print('[{:3d}]:{}'.format(i,str))
    i+=1
    str=input('Input string(quit: "end"):')

#69 91,80,84

#3. 정수 5개를 list에 기억시킨 후 가장 큰 수와 가장 작은 수를 출력하는 파이썬 스크립트
a=[1,2,3,4,5]
print(type(a))
#기준값 정해주기
max=min=a[0] #0은 이미 기준값으로 잡았으니 1부터 비교.
for i in range(1,len(a)):
    if max<a[i]:
        max=a[i]

    if min>a[i]:
        min=a[i]
print('max={}\tmin={}\t'.format(max,min))
#위에 나온 것과 같은 원리이나 훨씬 더 깔끔한 편. 다만 선택문을 어쩔 수 없이 쓴편? 193관련 이야기.