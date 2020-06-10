#dict
#   : key와 value 형식으로 데이터를 저장하는 자료형
#   : mapping형(순서가 없이 저장)
#   : 순서가 없기 때문에 인덱스를 사용할 수 없고 key를 사용하여 데이터 접근
#   : 변경 가능한 자료형이다.
#
#dict
student_info={20140012:'Hong', 20140059:'Kim',20140058:'Lee'}
member={'basketball':5, 'soccer':11, 'baseball':9}
print('student_info:{}'.format(student_info))
print('member:{}\n'.format(member))

d={} #빈 딕 생성
print('d:{}\n'.format(d))

#dict 길이
print('student+info length: {}'.format(len(student_info)))
print('member length:{}'.format(len(member)))
print('d legty:{}\n'.format(len(d)))

#dict 인덱싱 (요소 접근)
print('student_info[20140012]:{}'.format(student_info[20140012]))
print('member[\'soccer\']:{}'.format(member['soccer']))

#dict에 데이터 추가/변경
student_info[20140012]='Park' #값 변형(수정)
student_info[20140039]='Nam'  #값 추가
member['vollyball']=6         #값 추가
print('student_info:{}({})'.format(student_info,len(student_info)))
print('member:{}({})\n'.format(member, len(member)))

#dict에서 key는 변경 불가능한 형태일 때만 사용가능하다.
student_info[(20140099, 20180010)]='Hong Gil Dong'
print('student_info:{}({})\n'.format(student_info,len(student_info)))

#dict에서 데이터 삭제
del student_info[(20140099,20180010)]
del member['basketball']
print('student_info:{}({})'.format(student_info,len(student_info)))
print('member{}:({})\n'.format(member,len(member)))

#dict에서 멤버 검사
print(20140010 in student_info)
print('baseball'in member, '\n')

d['str']='python'
d[1]=1004
d[('a',1)]='dict type'
print('d:{}({})\n'.format(d,len(d)))

#data는 key와 value 형식, key로 접근해야 하고 key는 변경불가능한 타입이어야 한다. 이것만 유지되면 key의 타입은 자유롭게 설정할 수 있다.

#dict 함수(메서드)
print('student_info.keys:{}'.format(student_info.keys()))
print('member keys:{}'.format(member.keys()))
print('d values: {}\n'.format(d.keys()))

print('student_info values:{}'.format(student_info.values()))
print('member values:{}'.format(member.values()))
print('d values:{}\n'.format(d.values()))

print('student_info items:{}'.format(student_info.items()))
print('member values:{}'.format(member.items()))
print('d values:{}\n'.format(d.items()))

#62

d2={1:'hong',2:'kim'}
d.update(d2)
print('d items:{}\n'.format(d.items))

