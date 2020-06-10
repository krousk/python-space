#set(집합)
#   : 순서없이, 중복없이 저장하는 set 자료형
#   : 변경 가능한 자료형
#
#set생성
s=set()
print("s:{}({})".format(s,len(s)))
s=set([1,2,3,1,2,3])
print("s:{}({})".format(s,len(s)))
s={1,2,3,1,2,3}
print("s:{}({})\n".format(s,len(s)))

s=set((1,2,3,1,2,3)) #튜플 이용해 set 생성
print("s:{}({})".format(s,len(s)))
s=set('hello')        #str을 이용한 set 생성
print("s:{}({})".format(s,len(s)))
s=set([1,2,3])        #list이용 set 생성
print("s:{}({})".format(s,len(s)))
s=set({'one':1,'two':2})   #dict 이용 set 생성
print("s: {}({})".format(s,len(s)))

l1=[1,2,3]
l2=[3,4,5]
#s={l1,l2}  #set의 원소에는 변경 불가능한 자료형만 가능
print("s: {}({})".format(s,len(s)))
#line24: TypeError: unhashable type: 'list' 변경 불가능한 타입이어야 한다는 것.

#set 함수(연산, 메서드)
s={1,2,3,1,2,3}
print("s:{}({})".format(s,len(s)))

s.add(1) #원소 추가
print("s:{}({})".format(s,len(s)))
s.add(5)
print("s:{}({})\n".format(s,len(s)))

s.remove(1) #원소 삭제
print("s:{}({})".format(s,len(s)))

s.update([1,4,5,6,7]) #해당 set에 대한 합집합
print("s:{}({})".format(s,len(s)))

s.discard(3) #해당 원소 제거, 해당 원소가 없으면 무시. remove와 같은 성격. 단, 삭제할 것이 없으면 그냥 통과됨. remove는 예외라는 오류가 발생.
print("s:{}({})".format(s,len(s)))
s.discard(3)
print("s:{}({})".format(s,len(s)))
#s.remove(3)  #해당 원소 제거, 해당 원소가 없으면 예외(exception) 발생. 이 에러는 불가항력 상황이라 경우에 따라 건너뛰는 상황이 발생.
print("s:{}({})\n".format(s,len(s)))

s.clear()
print("s:{}({})\n".format(s,len(s)))

#set 집합 연산
s1={1,2,3,4,5}
s2={3,4,5,6,7}

print("합집합")
print(s1.union(s2))
print(s1|s2,'\n')

print("교집합")
print(s1.intersection(s2))
print(s1&s2,'\n')

print("차집합")
print(s1.difference(s2))
print(s1-s2,'\n')

#*파이썬 자료형
#1.원시 자료형: 값 자체를 의미
#   정수(int)
#   실수(float)
#   복소수(complex)
#   byte
#2.데이터 집합 자료형: 값의 집합. 값을 여러개 모으겠다.
#   2.1sequence형
#       str(string)
#       tuple
#       lisg
#   2.2mapping형
#       dict
#   2.3set형
#       set