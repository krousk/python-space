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

#문2###

#문3##
str=['두통','119','himdleda']
for index, value in enumerate(str):
    print('[{:2d}]{:<20s}'.format(index,value))

n=['이름','전화번호','e-mail']
for index, value in enumerate(zip(str,n)):
    print('[{:2d}]{}'.format(n,str))