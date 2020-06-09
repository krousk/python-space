#tuple
#   : 수정 불가능한 데이터 집합, 데이터 저장. 바뀌면 안되는 데이터 지정에 용이.
#   : sequence자료형(순서가 존재한다.)
#   : 인덱싱, 슬라이싱, 결합, 반복, 멤버 검사, 길이 계산의 sequence 자료형
#   : 공통연산을 적용할 수 있다.
#tuple 생성. ()로 생성한다. ()가 있으면 튜플.
t=()
#빈 튜플
print('t:{}\tlen(t):{}'.format(t,len(t)))

t=(1,2,3)
print('t:{}\tlen(t):{}'.format(t,len(t)))

t=1,2,3
print('t:{}\tlen(t):{}'.format(t,len(t)))

t=(1,)
print('t:{}\tlen(t):{}'.format(t,len(t)))
#하나라도 콤마가 있어야 함.

t=1,
print('t:{}\tlen(t):{}\n'.format(t,len(t)))
#콤마가 있어서 튜플이 됨.

#튜플 내용 포함 확인
t=(1,2,3)
print(1 in t)
print(5 in t, '\n')

#튜플 인덱싱
print(t[0])
print(t[2])
print(t[-2],'\n')

#튜플 슬라이싱
print(t[0:3])
print(t[1:3])
print(t[2: ])
print(t[ ::2],'\n')

#튜플 결합
print(t+t,'\n')

#튜플 반복
print(t*2,'\n')

#튜플 함수
t=(1,2,3,2,5,1,4,3)
print(t.count(2))
print(t.index(2))
#처음부터 검색
print(t.index(2,2),'\n')
#검색을 시작하는 위치,

#튜플 중첩
t1=(1,2,3)
t2=("hello",2020,'world')
t=t1,t2
print(t,'\n')
#서로 다른 자료형을 담는 것이 가능.
print(t[0][1],'\n')
#튜플이 두개니까 튜플 0,1 중에 0 튜플 고르고, 거기서 1번째 요소. 간단하게 튜플이 두개니까 인덱싱 두번. 문이 두개라서 두번 여는 것.

t=(1,2,3),('hello',2020,'world'),10
#1,2 튜플, 10은 값.(,가 없으니까.)
print(t)
print(t[0])
print(t[0][ : 2 ])
print(t[2],'\n')

#튜플을 이용한 데이터 치환
x,y,z=1,2,3
#,가 있으니 튜플. 양쪽의 수가 같으니 차례대로 매칭됨.
print(x,y,z)
(x1,x2),(y1,y2)=(1,2),(3,4)
#구조가 같으니 같은 위치로 치환.
print(x1,x2,y1,y2,'\n')

#원칙적으로는 두 변수의 내용을 교환할 때는 이렇게 새 변수 하나 만들어서 교환해야 함. t를 x로 바꾸고, 비워진 x에 y를 넣어서 바꿈. 즉 t는 임시변수가 된 것.
x,y=1,2
print(x,y)
t=x
x=y
y=t
print(x,y,'\n')

x,y=1,2
print(x,y)
x,y=y,x
print(x,y)

#패킹(packing): 한 공간에 여러 개의 데이터를 넣는 행위
#언패킹(unpacking): 데이터 집합의 내용을 꺼내오는 행위. list에도 적용 가능함.
t=1,2, 'python' #패킹
print(t)
x,y,z=t #언패킹
print(x,y,z,'\n')

#확장된 언패킹. 언패킹은 rvalue
#확장된 언패킹에서 *의 의미는 전부라는 뜻
t=(1,2,3,4,5)
print(t)
a, *b=t
#변수의 개수가 2:5로 언패킹이 안되어야 하나, *로 가능해짐.
print(a,b)
*a, b=t
print(a,b)
a,b,*c=t
print(a,b,c)

#튜플이 활용되는 경우
#1. 함수에서 하나 이상의 값을 반환(return 값)할 때 활용
#2. 함수의 인수로 활용
#3. 파이썬 2형식의 print() 형식 지정 출력에 사용

#57,58