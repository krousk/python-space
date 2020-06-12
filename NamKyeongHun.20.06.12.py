#예제
numbers=[1,2,3,4,5]
square=[]

for i in numbers:
    square.append(i**2)
print(square)

square=[i**2 for i in numbers]
print(square)

numbers=[1,2,3,4,5]
square=[]
for i in numbers:
    if i >=3:
        square.append(i**2)
print(square)

square=[i**2 for i in numbers if i>=3]
print(square)

#f=open('filetest.txt','t')
#file_text=f.read()
#f.close()
#print(filetest)

f=open('two_times_table.txt','w')
for num in range(1,6):
    format_string="2x{0}={1}\n".format(num,2*num)
    f.write(format_string)
f.close()

#!type two_times_table.txt

f=open("two_times_table.txt")
line1=f.readline()
line2=f.readline()
f.close()
print(line1,end="")
print(line2, end="")

f=open("two_times_table.txt")
line=f.readline()
while line:
    print(line,end="")
    line=f.readline()
f.close()

f=open("two_times_table.txt")
lines=f.readlines()
f.close()
print(lines)

f=open("two_times_table.txt")
lines=f.readlines()
f.close()
for line in lines:
    print(lines, end="")

f=open("two_times_table.txt")
for line in f.readlines():
    print(line, end="")
f.close()

f=open("two_times_table.txt")
for line in f:
    print(line, end="")
f.close()

f=open('two_times_table.txt','w')
f.write('File write/read test.')
f.close()

f=open('two_times_table.txt','r')
test=f.read()
f.close()
print(test)

#문1
for i in [[i,j,i*j] for i in range(1,10,1) for j in range(1,10,1)]:
    print(i[0],'*',i[1],'=',i[2])
#answer: 구구단은 기본적으로 중첩해야. 왜냐하면 단이 곱해지니까.
#안쪽의 i를 바깥쪽 j의 횟수만큼 반복하기.

#문2###

#answer:
int(input("input data1: "))
int(input("input data2: "))
int(input("input data3: "))
int(input("input data4: "))
int(input("input data5: "))
int(input("input data6: -99999"))


#%10d는  %d 사이에 10이 들어간 모양입니다. 10진수의 정수를 출력하는 서식이고 10의 의미는 10칸이라는 의미입니다.
#총 □□□□□□□□□□ 10칸에  해당 숫자를 넣겠다는 뜻입니다.
#print("%5d" %123)라 했을때 출력은
#□□123이 됩니다.
#많이 하던 유형

#문3##
str=['두통','119','himdleda']
for index, value in enumerate(str):
    print('[{:2d}]{:<20s}'.format(index,value))

n=['이름','전화번호','e-mail']
for index, value in enumerate(zip(str,n)):
    print('[{:2d}]{}'.format(n,str))

#dict을 쓸거면 key를 결정해야 함. dict은 키로 검색하는 것을 목적으로 해야 한다. key에 나머지
#내용이 나오는 식으로 할 것.