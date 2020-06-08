#1

number1= int(input("input number1: "))
number2= int(input("input number2: "))

result1=number1+number2

print('{0:10}+{1:10}={0:20}'.format(number1, number2, result1))
print(result1/2)

#2
number1= int(input("input number1: "))
number2= int(input("input number2: "))
number3=int(input("input number3: "))
number4=int(input("input number4: "))
number5=int(input("input number5: "))

result2=number1+number2+number3+number4+number5
result3=result2/5

print('{0:10}+{0:10}+{0:10}+{0:10}+{0:10}={0:100}'.format(result2/5))
