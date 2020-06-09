#교과서 예제 실습
#
#문자열
#"이나 '로 지정.
print("market garden",'\n')

var1="market"
var2='garden'
print(var1)
print(var2)
print(var1,var2,'\n')
print(type(var1),'\n')

var3='summer "day" come'
print(var3,'\n')

var4='''아 먹고살자 장사하자
방실방실 대한민국'''
print(var4,'\n')
#따옴표, 큰따옴표니 주의.

a='python '
b='big data'
c=a+b
print(c)
print(a * 4,'\n')
#띄어쓰기 유의

#리스트 만들기
#쉼표,[]
score=[10,9,7,10]
print(score)
print(type(score),'\n')

print(score[1])
print(score[-2])
score[1]=99
print(score)

ap=['AP', 'HEAT', 'HE']
print(ap[2])
print(ap[-1])

mix=[1,99,4.87,'male',False, ap]
print(mix)


#리스트 더하기
list1=[1,2,3,4]
list2=[5,6,7,8]
list_sum=list1+list2
print(list_sum,'\n')

#리스트 곱하기
list_mul=list1*3
print(list_mul,'\n')

#리스트 일부 항목 가져오기
list=[0,1,2,3,4,5,6,7,8,9]
print(list[7])
#0부터 시작해서 7번째 위치의 값. 인덱싱.
print(list[0:10])
#0부터 (전체-1)
print(list[2:])
#2번째부터 시작해서 끝까지. 0부터 시작이니까 3번쩨 부터 시작하라는 뜻.
print(list[::4])
#처음부터, 즉 0부터 4간격으로 끝까지.
print(list[:3],'\n')
#0부터 2까지. 즉 처음부터 3번째까지.

#리스트에서 항목 삭제하기
print(list)
del list[5]
print(list)
#5번째 값이 제거됨.

#리스트에서 항목 존재 여부 파악
print(10 in list)
print(9 in list,'\n')
#논리.

#리스트 메소드 연습
#변수명.insert(들어갈 인덱스 번호, 들어갈 값)
#append와 extend 차이는 하나 추가냐 여러개 추가냐.

#튜플
tp=(1,2,3)
print(tp)
#표기는 ( , , )
print(type(tp),'\n')
tp2=(9,)
tp3=9,
print(tp2)
print(tp3,'\n')

tp4=(1,2,3,4,5,6)
print(tp4.index(4))
tp5=('a','b','d','e')
print(tp5.index('b'))

#문제1
"홍길동01012345678"
qv1="홍길동"
qv2="010"
qv3="1234"
qv4="5678"
print(qv1+'('+qv2+'-'+qv3+'-'+qv4+')','\n')

#너무 복잡하게 생각한 경우.
#print(q1[0:3],q1[3:6],'\t',q1[6:10],'\t',q1[10:14])
#q1v1=[q1[0:3],q1[3:6],q1[6:10],q1[10:14]]
#q1.insert(2,'(')

#문제2
q2="홍길동 01012345678 hong@korea.com"
q2v1=q2.split()
q2v1[1]='010-1234-5678'
print(q2v1)

print('이름:{}\n전화번호:{}\ne-mail:{}')

#문제3
q3l1=[int(input("정수: "))]
q3l2=[int(input("정수: "))]
q3sum=q3l1+q3l2
print(q3sum)
print(int(q3sum[0])+int(q3sum[1]))
q3mean=(int(q3sum[0])+int(q3sum[1]))/2
print(q3mean)

#문제4


#문제5
q5v1=['hong',50,50,50]
q5v2=['kim',90,90,90]
q5v3=['lee',70,70,70]

q5t=q5v1+q5v2+q5v3
print(q5t)
