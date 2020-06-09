"""
    파이썬 자료형
    *원시 자료형
    숫자형: int, float, complex
    논리형: bool 참/거짓.
    바이트형: byte, 1바이트 문자.

    *집합 자료형
    문자형: str
    배열: list
    배열(수정불가): tuple
    배열(key:value 형식): dict
    집합: set #값의 중복을 허용하지 않음.
"""
#자료형(data type): memory 모양, 크기, 저장방식, 값의 범위 결정.

#원시 자료형
intNumber1=10
intNumber2=5
floatNumber1=12.9; floatNumber2=3.2
boolVariable=True
variable=None
byteVariable=b'python'

print(intNumber1, '\t', intNumber2)
print(type(intNumber1), '\t', type(intNumber2))
print(floatNumber1, '\t', floatNumber2)
print(type(floatNumber1), '\t', type(floatNumber2))
print(boolVariable)
print(type(boolVariable))
print(variable)
print(type(variable))
print(byteVariable)
print(type(byteVariable))

#\t는 제어문자. 실제로 출력은 안되나 tab 간격으로 띄워서 출력하라는 뜻.
#none type은 결정되지 않은 자료형을 뜻함.
#바이트는 뭐였는지 모르겠다.
#알과의 공통점. 동적 타이핑. 차이점. -> 안 쓰고 =를 씀. 알에서는 원시 자료형 중 바이트형, 복소수형 없음.


print()
#정수형
number=23 #10진 정수
print(number, '\t', type(number))
binary=0b1101      #2진 정수
octal=0o23         #8진 정수
hexa=0x23          #16진 정수
print(number, '\t', binary, '\t', octal, '\t', hexa)
print(2**1024) #정수 범위에는 제한이 없다.

#정수 형변환
print()
print(int('23',8))                #문자열을 정수로 변환, 문자열이 8진수
print(int('123'))                 #문자열을 정소로 변환
print(int(2.9))                   #실수를 정수로 변환
print(int(float('123.45')))       #문자열을 실수로 변환한 후 다시 정수로 변환

print()
print(bin(23))                    #2진수로 변환
print(oct(23))                    #8진수로 변환
print((hex(23)))                  #16진수로 변환

#실수
fnumber=1.2
print(fnumber, '\t', type(fnumber))
fnumber2=3e+3                           #지수표현, 과학적 표기법
print(fnumber2, '\t', type(fnumber2))

print()
print(round(1.2))                       #반올림
print(round(1.0))

#무한대 표현
print(float('inf'))
print(float('-inf'))
infinity=float('inf')
print(infinity/1000)

#실수 연산에서 파이썬은 오차가 좀 있으니 감안할 것.

#논리형
print()
number=1
print(number<0)
print(number>0)

print(True+True)
print(True+False)
print()

print(bool(1))
print(bool(0), '\t', bool(None), '\t', bool('')) #공백도 문자라서 스페이스 바 넣은 거로 true가 될 수 있다. 주의할 것.

#byte형
byteVariable=b'python'
print(byteVariable, '\n', type(byteVariable))
print(byteVariable>0)

print()
s='홍길동'
#b=b'홍길동'
#error의 종류 4개.