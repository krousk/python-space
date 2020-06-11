#앞부분 첫 한시간 놓침.


#
#list comprehension(list 내장)
#   : comprehension (내장) 기능은 별도의 제어문을 사용하지 않고 반복기능을 활용하여 list에 값을 저장하는 방법.
#for 문을 이용하여 list에 1~10까지 값을 저장.
l=[]
for i in range(1,11):
    l.append(i)
print('l:{}({})\n'.format(l,len(l)))

#list comprehension 이용하여 list에 1~10까지 값을 저장. 가능한 별도의 제어문 안쓰고 하는 게 파이썬 스러운 것.
l2=[i for i in range(1,11)]
print('l2: {}({})\n'.format(l2,len(l2)))
#p.92

#짝수만 갖겠다.
l=[]
for i in range(1,11):
    if i % 2==0:
        l.append(i)
print('l:{}({})\n'.format(l,len(l)))

l2=[i for i in range(1,11) if i%2==0]
print('l2:{}({})\n'.format(l2,len(l2)))

#1부터 1000 사이의 3의 배수이거나 5의 배수를 list comprehension을 통해 기억시켜라.
l3=[i for i in range(1,1001) if i % 3==0 or i % 5==0]
print('l3:{}({})\n'.format(l3,len(l3)))
#별도의 for문을(제어문)을 쓰지 않더라도 리스트에 원하는 값을 한줄로 채워넣을 수 있음.

#list에 양수/음수/짝수/홀수를 10개 적어서 저장한 후, list comprehension을 이용하여 양수/음수, 양수일 때 짝수/홀수 갯수를 출력하라.
l4=[5,-9,7,4,10,-17,12,0,24,-77]
positive=[value for value in l4 if value>0]
negative=[value for value in l4 if value<0]
print('positive:{}({})'.format(positive,len(positive)))
print('negative:{}({})'.format(negative,len(negative)))

even=[value for value in positive if value %2==0]
odd=[value for value in positive if value %2 !=0]
print('even:{}({})\n'.format(even,len(even)))
print(('odd:{}({})\n'.format(odd,len(odd))))

even=[value for value in l4 if value >0 and value %2==0]
print('even:{}({})\n'.format(even, len(even)))

#중첩 반복을 이용한 list comprehension
str1='hello'
str2='world'
l=[v1+v2 for v1 in str1 for v2 in str2]
print('l:{}({})\n'.format(l, len(l)))

for v1 in str1:
    for v2 in str2:
        l.append(v1+v2)
print('l:{}({})\n'.format(l,len(l)))

l=[v1+v2 for v1 in str1 for v2 in str2]
print('l:{}({})\n'.format(l,len(l)))

#list comprehension을 이용한 1~9까지 구구단표 만들기.
multiple_table=[i*j for i in range(1,10) for j in range(1,10)]
print(multiple_table)
count=1
for value in multiple_table:
    print('{:3d}'.format(value),end='')
    count+=1
    if count>9:
        print()
        count=1

#list comprehension을 이용한 2차원 list
multiple_table=[[i * j for i in range(1,10)] for j in range(1,10)]
print('\nmultiple_table: {}({})\n'.format(multiple_table, len(multiple_table)))
#단을 구별.
for multiple in multiple_table:
    for value in multiple:
        print('{:3d}'.format(value),end='')
    print()

words='The quick brown fox jumps over the lazy dog'.split() #단어의 리스트.
print('words: {}({})\n'.format(words, len(words)))
stuff=[[w.upper(),w.lower(),len(w)]for w in words] #[[]]면 2차원 구조를 만들 수 있다. [] 하나만 더 넣어주면 2차원이 된다는 것.
print('stuff:{}'.format(stuff))

for word in stuff:
    print(word)

str1=['A','B','C']
str2=['D','E','F']
l1=[i+j for i in str1 for j in str2]
l2=[[i+j for i in str1]for j in str2]
print('\nl1:{}({})'.format(l1,len(l1)))
print('l2:{}({})'.format(l2,len(l2)))
#저장된 모양과 길이에서 차이. l1은 1차원, l2는 2차원. 2차원은 행열의 집합, 1차원은 열의 집합.
#p92~94