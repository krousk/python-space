#1.string
#2.tuple
#3.list
#4.dictionary
#5.set

#집합: 모여있는 것. 문자열: 문자가 모여있는 것. 숫자열과의 구분은 연산이 되는지로.

#direct형: 원시 데이터. 데이터에 직접 접근. sequence형: 순서가 있다는 것이 중요.
#변경 불가능형. 값은 안 바뀌고 주소만 바뀐다. 변수명을 주소로 바꾸는 것이(2진법화) 인터프린트.

#문자열(string)
#   : 문자집합
#   : sequence 자료형(순서가 존재)
#   : 인덱싱, 슬라이싱, 결합, 반복, 멤버 검사, 길이 계산의 sequence 자료형
#   : 공통연산을 적용할 수 있다.
#문자열 생성
str='' #빈 문자열 생성
str2='hello'
print('type(str): ', type(str), end='')
print('type(str2): ', type(str2))
print('str: {}\tstr2: {}\n'.format(str,str2))

str='Don\'t walk. "Run"'
print(str)

str='This is a rather long string \
containing back slash and new line.\nGood!'
print(str)

#한칸 띄우고 \ 넣기.

str= '''
python is great\nYes, it is.
'''
print(str,'\n')

str='This is a rather long string ' + \
'containing back slash and new line.\nGood!'
print(str,'\n')

#문자열 길이. length는 문자열의 길이를 계산. sequence 형 자료에 사용 가능.
str="Python is grate!!!"
print("str : {}\tlength : {}\n".format(str, len(str)))

#문자열 내용 포함 확인 in도 sequence 자료형의 공통 연산자.
print("P" in str)
print('p'in str)
print('Python'in str)
print('is'in str)
print('th'in str, '\n')

#문자열 인덱싱: 파이썬에서 인덱싱 시작은 [0]부터 마지막은 [길이-1]. 0부터 시작이니까 길이-1인 것. -는 뒤에서 부터 세라는 것. 즉 리버스, 역순. -1부터 시작.
#   ":문자열의 원하는 문자에 접근하는 방법
print(str[0])
print(str[7])
print(str[-1])
print(str[-8], '\n')

#문자열 슬라이싱: 문자열에 대하여 부분 문자를 지정할 때 사용
print(str[0:6])
#마지막 6은 포함이 안됨. 이하도 마찬가지, 마지막은 포함 안됨.
print(str[8:10])
print(str[7:12:3])
#3번째는 증가값. 즉, 시작위치, 끝위치, 증가값
print(str[:6])
#시작이 없으니 시작부터 6(5번째)까지 라는 것.
print(str[11:])
#11부터 시작해서 마지막까지.
print(str[::2])
#처음부터 2씩 증가.
print(str[::-1])
#끝에서부터 -1씩 증가.
print( str[ : ] )
#아무것도 안하고 전체.
print(str[-50:50], '\n')

#문자열은 변경불가자료형
#str[0]='p'
print(str, '\n')

#문자열 결합(+)
s1='first'
s2='second'
s3=s1+' ' +s2
print("s1:[{}]s2: [{}] s3: [{}]\n".format(s1,s2,s3))

#문자열 반복(*)
print(s1*3,'\n')

s='spam and egg'
print(s)
s=s[:5]+'cheese' +s[5:]
print(s)

#문자열 함수
str='i like programming. i like swimming'
print('\n'+str.upper())
#전부 대문자
print(str.lower())
#전부 소문자
print(str.capitalize())
#전체 문장의 첫글자 대문자
print(str.title())
#각 단어마다 첫글자 대문자
print(str.count('like'))
print(str.find('like'))
#앞에서부터 몇번째에 like가 있는가?
print(str.rfind('like'))
#오른쪽에서 왼쪽으로 따졌을 때 like의 위치

str='spam and egg'
print(str.strip())
#앞뒤공백 삭제
print(str.rstrip())
#오른쪽 공백을 없애라.
print(str.split())
#결과가 리스트로 나온 것. 공백 기준으로 잘라내겠다는 것.
print(str.split('and'), '\n')
#and 기준으로 split. 즉 잘라내는 기준으로 and를 사용. 그래서 출력 안된 것.

l=str.split()
print(':'.join(l))
#결합하겠다는 것. 사이사이에 :을 넣어서.
print('\n'.join(l),'\n')
#줄바꿈 넣어서 join.
print(str.center(60))
#전체 60칸에 가운데에 출력하라. 화면 가로폭의 최대는 80.
print(str.ljust(60))
#왼쪽으로 정렬, 60 기준으로.
print(str.rjust(60))
#오른쪽으로 정렬, 60기준으로.
print(str.center(60, '-'))
#가운데 정렬하되 빈칸 하이픈으로 채울 것.

print(ord('A'))
#해당 문자의 아스키 코드 값. 10진수로 출력.
print(chr(0x0041))
#실제 코드값의 문자. 0x는 16진수. 16진수 41번.
#45~48,158~173

