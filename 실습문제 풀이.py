#
# 선택 구조 실습
#
# 1. 정수 5개를 list에 기억시킨 후 가장 큰 수와 가장 작은수를
#    출력하는 파이썬 스크립트
numbers = [5, 2, 1, 3, 4]
print("numbers : {}( {} )".format(numbers, len(numbers)))
max = min = numbers[0]

if max < numbers[1]:
    max = numbers[1]
if max < numbers[2]:
    max = numbers[2]
if max < numbers[3]:
    max = numbers[3]
if max < numbers[4]:
    max = numbers[4]

if min > numbers[1]:
    min = numbers[1]
if min > numbers[2]:
    min = numbers[2]
if min > numbers[3]:
    min = numbers[3]
if min > numbers[4]:
    min = numbers[4]

print("max : {}\tmin : {}\n".format(max, min))

#
# 2. 3개의 정수를 각각의 변수에 기억시킨 후 큰수, 중간수, 작은수 순으로
#    출력하는 파이썬 스크립트
x = 1;
y = 2;
z = 3
# x = 1; y = 3; z = 2
# x = 2; y = 1; z = 3
# x = 2; y = 3; z = 1
# x = 3; y = 1; z = 2
# x = 3; y = 2; z = 1
print("x : {}\ty : {}\tz : {}".format(x, y, z))

# 중첩 선택 구조
if x > y:
    if x > z:
        max = x
        if y > z:
            mid = y
            min = z
        else:
            mid = z
            min = y
    elif z > y:
        max = z
        mid = x
        min = y
elif y > z:
    max = y
    if x > z:
        mid = x
        min = z
    else:
        mid = z
        min = x
else:
    max = z
    mid = y
    min = x

print('max : {}\tmid : {}\tmin : {}'.format(max, mid, min))