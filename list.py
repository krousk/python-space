#list
#   :수정 가능한 데이터 집합(튜플과의 차이점), 데이터 저장. 반드시 [] 필요. 없으면 튜플이 됨.
#   :sequence 자료형(순서가 존재한다.)
#   :인덱싱, 슬라이싱, 결합, 반복, 멤버 검사, 길이 계산의 sequence 자료형
#   :공통연산을 적용할 수 있다. 자료형이 달라도 된다.
#   :r에서와는 다르게 다른 자료형끼리도 묶는 것이 가능.
#list 생성
l=[]#빈 list
print('l:{}\tlen(l):{}'.format(l,len(l)))

l=[1,2, 'python']
print('l:{}\tlen(l):{}'.format(l,len(l)))

colors=['red','blue','green']
print('colors: {}\tlen(colors): {}'.format(colors, len(colors)),'\n')

#생성(변환) 함수 이용한 list 생성
l=list(range(10))
print('l:{}\tlen(l):{}'.format(l,len(l)))
#0부터 발생, 9까지(길이-1)
l=list(range(1,11,2))
print('l:{}\tlen(l):{}'.format(l,len(l)),'\n')
#11은 제외. 역시 길이-1

#list 내용 포함 확인
print("red" in colors)
print("purple" in colors, '\n')

#list 인덱싱
print(colors[0])
print(colors[2])
print(colors[-2],'\n')

#list 슬라이싱
print(colors[0:3])
print(colors[1:3])
print(colors[2:])
print(colors[:2])
print(colors[::2],'\n')

#list 결합
print(colors+colors,'\n')

#list 반복
print(colors*3,'\n')

#기존 str과 tuple에 없는 내용들.
#list 내용 변경
#list 일부 값 변경
l=['spam','eggs',100,2020]
print('l:{}\tlen(l):{}'.format(l,len(l)))
l[2]=l[2]+59
print('l:{}\tlen(l):{}'.format(l, len(l)))

#list 일부 값 치환
l[0:2]=[1,12]
print('l:{}\tlen(l):{}'.format(l, len(l)))

l[0:2]=[1]
print('l:{}\tlen(l):{}'.format(l, len(l)),'\n')

#list 일부 값 삭제
l=[1,12,123,1234]
print('l:{}\tlen(l):{}'.format(l,len(l)))
l[0:2]=[]
print('l:{}\tlen(l):{}'.format(l, len(l)),'\n')

#list 일부 값 추가
l=[123,1234]
print('l:{}\tlen(l):{}'.format(l,len(l)))
l[1:1]= ['spam','ham']
print('l:{}\tlen(l):{}'.format(l, len(l)),'\n')
#삽입하는 효과(insert)가 난다.

#del 명령을 이용한 삭제
del l[0]
print('l:{}\tlen(l):{}\n'.format(l, len(l)))

del l[1:]
print('l:{}\tlen(l):{}\n'.format(l, len(l)))

l=list(range(4))
print('l:{}\tlen(l):{}'.format(l, len(l)))
l[ ::2 ]
print('l:{}\tlen(l):{}'.format(l[ ::2 ], len(l)))
del l[ ::2 ]
print('l:{}\tlen(l):{}\n'.format(l, len(l)))

#list 함수
print('colors:{}\tlen(colors):{}'.format(colors,len(colors)))

colors.append('white')
print('colors:{}\tlen(colors):{}'.format(colors,len(colors)))

colors.extend(['black','yellow'])
print('colors:{}\tlen(colors):{}'.format(colors,len(colors)))

colors.insert(3,'purple')
print('colors:{}\tlen(colors):{}'.format(colors,len(colors)))

colors.insert(0,'orange')
print('colors:{}\tlen(colors):{}'.format(colors,len(colors)))

colors.append('white')
print(colors.count('white'))
print(colors.index('white'),'\n')
#5번째에 화이트가 있다.

colors.reverse()
print('colors:{}\tlen(colors):{}\n'.format(colors, len(colors)))
#리버스로 역전.

colors.sort()
print('colors:{}\tlen(colors):{}\n'.format(colors, len(colors)))
#정렬됨. 알파벳 순서(아스키 코드 순서)로 정려됨. 사전식 순서로 정렬됨. 즉, bl까지는 같았고, a하고 u로 달라진 시점에서 누가 더 큰지 비교. 그래서 black이 앞으로. 오름차순.
#글자수 길이로 판단하기도 하나, 통상 글자 하나하나 비교해서 결정.

colors.sort(reverse=True)
print('colors:{}\tlen(colors):{}\n'.format(colors, len(colors)))
#내림차순으로 정렬됨.

l='Python is a Programming Language'.split()
print('l:{}\tlen(l):{}\n'.format(l, len(l)))
l.sort()
print('l:{}\tlen(l):{}\n'.format(l, len(l)))
#소문자를 큰 것으로 보고 있음. 이후 대문자들끼리 알파벳 크기 비교. 실제로 아스키코드에서 소문자가 대문자보다 더 큼.
l.sort(key=str.lower)
print('l:{}\tlen(l):{}\n'.format(l, len(l)))

l=[1,6,3,8,6,2,9]
print('l: {}\tlen(l):{}'.format(l,len(l)))
l.sort()    #method 메소드
print('l: {}\tlen(l):{}\n'.format(l,len(l)))
#순서가 바뀜. 원래 위치를 모름. ***원본 순서가 중요한 경우에는 소트 메소드를 써서는 안됨.

l=[1,6,3,8,6,2,9]
new=sorted(l)   #function 함수
print('l: {}\tlen(l)'.format(l,len(l)))
print('new2:{}\tlen(new2):{}'.format(new,len(new)))
#l의 위치가 안 바뀜. 대신 new2에서 바뀐 위치가 적용됨. ***소티드 함수는 원본 순서를 바꾸지 않음.

#. 뒤에 나오는 함수는 메소드(method)라 호칭.
#. 없이 호출하면 함수라 호칭.

print('colors:{}\tlen(colors):{}\n'.format(colors, len(colors)))
colors.remove('red') #리무브 메소드 삭제.
print('colors:{}\tlen(colors):{}\n'.format(colors, len(colors)))

del colors[ : ]
print('colors:{}\tlen(colors):{}\n'.format(colors, len(colors)))

l=[]
l.append(5) #append는 항상 오른쪽, 그러니까 끝에서부터 추가함. 그래서 5, 10, 15 순으로.
print('l: {}\tlen(l){}\n'.format(l,len(l)))
l.append(10)
print('l: {}\tlen(l){}\n'.format(l,len(l)))
l.append(15)
print('l: {}\tlen(l){}\n'.format(l,len(l)))

print(l.pop()) #팝 메소드. 오른쪽, 그러니까 마지막에 있는 것부터 끄집어내서 리스트에서 삭제함. 그래서 진행이 append의 역순.
print('l: {}\tlen(l){}\n'.format(l,len(l)))
print(l.pop())
print('l: {}\tlen(l){}\n'.format(l,len(l)))
print(l.pop())
print('l: {}\tlen(l):{}\n'.format(l,len(l)))
#빈 리스트가 됨.
#이런 구조를 stack 구조, 즉 쌓아놓는 구조.(LIFO, Last In, First OUt. 후입선출법)

#중첩 list(2차원)
korScore=[59,99,79]
engScore=[57,97,77]
midterm=[korScore, engScore]
print('midterm:{}\nlen(midterm):{}'.format(midterm,len(midterm)))

print('\n',midterm[0])
print(midterm[0][1])
print(midterm[0][1:])

#list의 패킹/언패킹
t=[1,2,3]  #패킹
a,b,c=t    #언패킹
print(t)
print(a,b,c)

#51~54, 54 리스트 메소드 표, 45~58, 158~173