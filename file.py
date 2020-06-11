#file 처리
#   : 메모리 내용을 보조 기억장치의 파일에 보관하거나
#    보조기억 장치에 저장된 파일 내용을 메모리에 저장하는 모든 처리
#
#file 처리 절차
#1. 파일 open
#2. 파일 처리(파일에서 읽기/파일에 쓰기)
#3. 파일 close(그렇지 않으면 파일이 깨질 수도 있음)
#
#파일 종류(저장되는 값의 형태에 따른 구분)
#1. Text file: ASCII 형태로 저장, 파일 끝을 의미하는 EOF가 저장됨. 데이터 양이 적고, 보안이 중요하지 않은 경우. 메모장으로도 볼 수 있으니까.
#2. Binary file: 메모리 내용(2진수 형태)그대로 저장. 파일의 끝을 의미하는 값이 저장되지 않음. 데이터 양이 많고, 보안이 중요한 경우.
#
#파일 종류(한번에 저장되는 data 형식에 따른 구분)
#*record: 파일에 대해 한번에 읽기/쓰기 하는 단위
#1. 고정 길이 레코드: 레코드 길이가 일정하다. 검색이 쉬움.
#2. 가변 길이 레코드: 레코드 길이가 일정하지 않다. 저장공간을 적게 차지한다.
#
#파일 종류(검색 방식에 따른 분류)
#1. 순차파일: record를 순차적으로 저장, 검색 시 오래 걸림. 구현하기 쉬움.
#2. 색인파일: record 저장 파일과 index(색인) 저장 파일로 저장. 검색이 빠름.
#3. 직접파일: record를 임의 위치에 저장, 검색 빠름, 구현 어려움.
#104, 105표 참고.
#XML(eXtended,Markup,Language)이나 JSON(Java Script object, Notation)
print('파일 쓰기')
#f=open('filetest.txt','w') #a로 하면 계속 내용이 추가됨.
with open('filetest.txt','a')as f:
  f.write('Python is great!!!') #이게 한 레코드.
  f.write('\n')#위의 것과 길이가 다르니 가변길이 레코드.
#f.close()
#이 프로젝트 디렉토리에 생성됨. 경로를 지정안했으니. 해당 파일을 노트패드로 열어볼 시에, 끝에 crlf라는 게 생김.
#CR(Carrige Return): home 위치로 이동.\n
#LF(Line Feed): 다음 줄로 이동.\r

#파일 읽기
print('파일 읽기')
#f=open('filetest.txt','r')
with open('filetest.txt','r') as f:
  text=f.read()
  print('filetest.txt로 부터 읽는 내용:{}'.format(text))
#f.close()
#p105~107 내용

#107~110
#111 with문 사용법. 자동으로 close를 해주는 것.