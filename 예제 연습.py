#교과서 예제 실습
#
#문자열
#"이나 '로 지정.
print("market garden")
var1='market'
var2='garden'





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
print(9 in list)
#논리.

#리스트 메소드 연습
