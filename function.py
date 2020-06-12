#
#함수(function)
#   : 단위 기능(하나의 기능)을 수행하는 코드집합(코드 블록). 함수는 하나의 기능만 수행하게 해야 한다.
#       중복되는 처리를 수행하는 코드블록을 별도로 작성한 후
#       필요시 호출해서 사용한다.
#
#함수 사용을 통해 얻을 수 있는 점
#1. 중복 코드 방지를 통한 유지 보수성 향상
#2. 특정 기능에 대하여 별도로 구현하지 않고 호출하여 사용
#3. 팀 작업을 수행할 때 팀원들은 함수 중심으로 작성함여 차후 통합을 수월하게 할 수 있다.
#
#함수는 함수 정의, 함수 호출 두 부분으로 구성되어 있으며 파이썬에서는 반드시 함수 정의가 함수 호출보다 먼저 수행되어야 한다.
#
#객체에 소속된 함수는 메서드(method)라고 부른다.
#
#함수 정의 형식
#def <함수 이름> ([인수 목록]):   통상 함수 이름은 동사,동사구. []표시는 필요하면 생략가능하다는 뜻.
#함수 내용
#[return < 값>] return도 생략가능. []니까.
#
#함수유형
#1. 인수 없고, return값 없는 유형
def myprint():
    print('welcome python world!!!')

#2. 인수 없고, return값 있는 유형->희박한 형태.
def myprint2():
    print('welcome python world!!!')
    return True
#3. 인수 있고, return값 없는 유형
def myAdd(number1, number2):
    result=number1+number2
    print('{}+{}={}'.format(number1,number2,result))
#4. 인수 있고, return값 있는 유형
def myAdd2(number1, number2):
    result=number1+number2
    return result
#

#함수 호출
myprint()
myprint2()
print(myprint2())
myAdd(10,5)
print('{}+{}={}'.format(10,5,myAdd2(10,5)))

#
#함수의 return 값은 한개만 가능하다.
#
def calculate(number1, number2):
    add=number1+number2
    substract=number1+number2
    multiple=number1+number2
    divide=number1/number2
    remainder=number1%number2
    return  add, substract, multiple, divide, remainder

number1, number2=10,5
result=calculate(number1, number2)
print('{:3d}+{:3d}={:5d}'.format(number1,number2, result[0]))
print('{:3d}-{:3d}={:5d}'.format(number1,number2, result[1]))
print('{:3d}*{:3d}={:5d}'.format(number1,number2, result[2]))
print('{:3d}/{:3d}={:5.2f}'.format(number1,number2, result[3]))
print('{:3d}%{:3d}={:5d}'.format(number1,number2, result[4]))
#return 값은 수정이 되어서는 안되기 때문에 튜플로 고정해야 한다.

#
#문)값을 입력 받아 한계를 return 하는 함수
#
#함수정의
#1. 합계 저장하는 변수 생성, 0으로 초기화.
#2. 인수(numbers)만큼 반복
#   2.1 합계 저장 변수에 numbers의 내용 하나를 누적
#3. 합계 return
def mysum(numbers):
    sum=0#1 이거는 맞음.
    for value in numbers:#2 value가 뭘 뜻하는지 파악할 것.
        sum+=value#2.1 +=는 뭔 기호여?
        return sum#3 return 다시 확인. 뭔 소리야...            왜 15가 안 나오는지 확인.

#
#문) 인수를 전달받아 최고값을 return 하는 함수
#1. 최고값 저장 변수 생성
#2. 인수 길이만큼 반복
#   2.1 최고값 파악
#3.최고값 return
def mymax(numbers):
    high=numbers[0]#1 맞음.
    for value in numbers:#2 이걸 몰랐다.
      if high<value:
         high=value#2.1
    return high#3

#
# 문)인수를 전달받아 최저값을 return 하는 함수
def mymin(numbers):
    low=numbers[0]
    for value in numbers:
        if low >value:
            low=value
    return low

#
#문)인수를 전달받아 평균을 return 하는 함수
def mymean(numbers):
    sum=0
    for value in numbers:
        sum+=value
    count=len(numbers)
    mean=sum/count
    return mean
#return mysum(numbers)/len(numbers)

#
#문)인수를 전달바아 최대값과 최소값을 return하는 함수
def mymaxandmin(numbers):
    return mymax(numbers), mymin(numbers)

#
#문)인수를 전달받아 편차를 return 하는 함수
def mydeviation(numbers):
    mean= mymean(numbers)
    return tuple([value-mean for value in numbers])



#
#문) 인수를 전달받아 편차 제곱을 return 하는 함수
def mydeviationsequared(numbers):
    return tuple([value**2 for value in numbers])




#
#문) 인수를 전달받아 분산값을 return하는 함수    평균, 편차, 편차제곱
def myvariance(numbers):
    #return mymean(numbers)
    #pc=numbers-mymean(numbers)
    #pc2=pc**2
    #var=pc2/count
    #return var
    count=len(numbers)
    mean=mymean(numbers)
    deviations=[value-mean for value in numbers]
    deviation_squareds=[value**2 for value in deviations]
    variance=mysum(deviation_squareds)/count
    return variance

#
#문) 다음과 같이 출력되는 mysummary() 정의
#변량
#최대값
#최소값
#평균값
#편차
#분산
def mysummary(numbers):
    print('변량:')
    line_count=1 #??
    for value in numbers:
        print('{:8d}'.format(value),end='')
        line_count=1
        if line_count>10:
           line_count=1; print()
    print('\n최대값:{}'.format(mymax(numbers)))
    print('최소값:{}'.format(mymin(numbers)))
    mean=mymean(numbers)
    print('평균값:{:.2f}',format(mean))
    print('편차: ')
    line_count=1
    for value in list( mydeviation(numbers,mean)):
        print('{:8.2f}'.format(value),end='')
        line_count +=1
        if line_count>10:
            line_count=1;print()
    print('\n분산:{:.2f}'.format(myvariance(numbers)))


#핸재 모듈의 이름이 '__manim__'이면 True
#현재 모듈을 단독으로 실행할 때 __name__이 '__main__'이 된다.
#이와 같은 조건을 부여하면 import 할 때는 실행되지 않고, 단독으로 모듈을 실행할 때만 작동한다.

if __name__ =='__main__':
    #함수호출
    numbers=[5,3,1,4,2]
    sum=mysum(numbers)
    print('sum: {}'.format(mysum(numbers)))
    print('max: {}'.format(mymax(numbers)))
    print('min: {}'.format(mymin(numbers)))
    print('mean: {}'.format(mymean(numbers)))
    print(mymaxandmin(numbers))
    print('variance: {:.2f}'.format(myvariance([177,175,179,181,183])))
    print('dv: {}'.format(mydeviation(numbers)))
    print('mds: {}'.format(mydeviationsequared(numbers)))

    mysummary([177,175,179,181,183])








#115120,125134,179
















#원하는 것, 구현하고 싶은 것 쓰면서 논리화 진행하기.