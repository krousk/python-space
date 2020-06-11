#dictionary comprehension
#enumerate(): list에 대하여 (index, value) 형식으로 나열하는 함수.
str=['apple', 'banana', 'pinapple', 'melon']
for index, value in enumerate(str):
    print('[{:2d}]{:<20s}'.format(index,value))
#for문을 쓸 때, 리스트 안의 값이 필요할 때가 있고, 인덱스가 필요한 경우가 있는데 이 경우 인덱스가 필요한 경우.

#str의 index 사용
for index in range(len(str)): #list 길이를 이용하여 반복, index 사용
    print('[{:2d}]{:<20s}'.format(index, str[index]))
print()

for s in str: #list 자체를 이용하여 반복, list 요소(내용,값)
    print('{:<20s}'.format(s))
print()

for index, value in enumerate(str): #enumerate 항상 튜플로 인덱스 값을 줌. for index, 에 ,가 있으니까 튜플.
    print('[{:2d}]{:<20s}'.format(index,value))

for index, _ in enumerate(str): #13번과 같은 형식. _은 반복만 하고 싶을 때씀. 즉 값없이 반복만 시키고 싶을 때.
    print('[{:2d}]{:<20s}'.format(index,str[index]))

for _ in range(1,6):
    print('Hello!!!')

#zip(): 리스트(sequence형)값을 병렬로 묶는 함수. 서로의 길이가 동일해야 함. 즉 두개의 인덱스를 묶어주는 것.
l=[1,2,3]
str=['apple','banana','pineapple']
for index, value in zip (l,str):   #index라는 튜플로 넘김.
    print('[{:2d}]{:<10s}'.format(index,value))
print()

a,b,c=zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c,'\n')

str1=['a1','a2','a3']
str2=['b1','b2','b3']
for index, value in enumerate(zip(str1,str2)): #zip 먼저 한 다음, zip의 값을 인덱스, 벨류(값)을 분리해서 표기하라.
    print('[{:2d}]{}'.format(index,value))

#dictionary comprehension dictionary는 key와 value 형식으로 데이터 저장.
d={w:1 for w in 'abc'}
print(d)

str='abce'
t=(1,2,3,4)
d={k:v for k, v in zip(t,str)}
print(d)

d={k:v for k, v in [(1, 'one'),(2, 'two'), (3, 'three')]} #key값과 value 값.
print(d)

d={v:k+1 for k, v in enumerate(['one', 'two', 'three'])} #v를 인덱스, k를 value로 잡았음. 그래서 출력이 one:1 이렇게 되는 것.
print(d)

print(d.items())
d2={v:k for k, v in d.items()}
print(d2)

d={(k,v): k+v for k in range(3) for v in range(3)}
print(d)