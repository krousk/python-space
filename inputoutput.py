#표준 입/출력
result=None

number1=int(input("Input number1 : "))
number2=int(input("Input number2 : "))

result=number1+number2

print(number1, '\t', number2, '\t', result)
#%[전체 자리수]d: (Decimal number)-> 출력 형식
#python 2에서 사용하는 방식
print('%5d+%5d=%10d' % (number1, number2, result))  #d는 대시멀 넘버. 10진 정수.
#pythom 3에서 사용하는 방식
print('{0:5}+{1:5}={2:10}'.format(number1,
                                  number2,
                                  result))
#0, 1,2 는 함수 순서. 뒤에 5는 자릿수.
#input 함수는 기본적으로 문자로 인식. 때문에 형변환을 반드시 해야함.
#29~44페이지, 95~104페이지까지의 내용.

#0금일 학습 내용에 대한 교재 예제 실습
#1두 정수를 입력 받아, 합계, 평균을 출력하는 파이썬 스크립트
#2다섯 정수를 입력받아 평균, 편차, 편차제곱, 분산을 출력하는 파이썬 스크립트. 알에서 준 pdf 참고할 것. 2,3번 제출할 것.
#*결과 제출은 본인영문이름_날짜로 프로젝트 생성 후 프로젝트에 1,2번 파이선 스크립트를 작성한 후 프로젝트를 본인영문이름 날짜로 압축하여 제출.