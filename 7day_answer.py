#!/usr/bin/env python
# coding: utf-8

# 실습과제
# 1. 제공 되는 'Floating_Population_2004.csv' 파일을 파이썬 파일 처리 읽기 기능을 이용하여 읽어온 후 NumPy 배열로 생성하고 NumPy가 제공하는 함수를 활용하여 데이터를 분석한 스크립트를 제출한다.

# # 서울시 유동인구 분석

# ## 0. NumPy import

# In[1]:


import numpy as np


# ## 1. 파일 내용 저장 파이썬 리스트 변수 선언

# In[2]:


# data 저장 list
date_list = []
time_list = []
age_list = []
gender_list = []
gu_list = []
population_list = []


# ## 2. 파일에서 전체 데이터 읽어서 데이터 확인( 'Floating_Population_2004.csv.csv )

# In[3]:


with open( 'Floating_Population_2004.csv', 'r', encoding = 'utf-8' ) as f:
    line = f.readline()
    while line:
        print( line )
        data = line.split( ',' )
        line = f.readline()


# ## 3. 파일에서 전체 필요 데이터 읽어서 list에 저장( 'Floating_Population_2004.csv.csv )

# In[5]:


with open( 'Floating_Population_2004.csv', 'r', encoding = 'utf-8' ) as f:
    line = f.readline() # 제목줄 제거
    line = f.readline()
    while line:
        data = line.split( ',' )
        
        # 날짜 list에 추가
        date_temp = data[ 0 ].split( '"' )
        date_list.append( date_temp[ 1 ] )
        
        # 시간 list에 추가
        time_temp = data[ 1 ].split( '"')
        time_list.append( time_temp[ 1 ] )
        
        # 연령 list에 추가
        age_temp = data[ 2 ].split( '"' )
        age_list.append( age_temp[ 1 ] )
        
        # 성별 list에 추가
        gender_temp = data[ 3 ].split( '"' )
        gender_list.append( gender_temp[ 1 ] )
        
        # 구 list에 추가
        gu_temp = data[ 5 ].split( '"' )
        gu_list.append( gu_temp[ 1 ] )
        
        # 유동인구 list에 추가
        population_temp = data[ 6 ].split( '"' )
        population_list.append( int( population_temp[ 1 ] ) )
        
        line = f.readline()


# ## 4. 읽은 데이터 확인( 처음 5개, 마지막 5개 )

# In[6]:


date_list[ :5 ], date_list[ len( date_list ) - 5 : ]


# In[7]:


time_list[ :5 ], time_list[ len( time_list ) - 5 : ]


# In[8]:


age_list[ :5 ], age_list[ len( age_list ) - 5 : ]


# In[9]:


gender_list[ :5 ], gender_list[ len( gender_list ) - 5: ]


# In[10]:


gu_list[ :5 ], gu_list[ len( gu_list ) - 5: ]


# In[11]:


population_list[ :5 ], population_list[ len( population_list ) - 5: ]


# ## 5. NumPy 배열 생성

# ### 5.1 전체 날짜/시간

# In[12]:


date_array = np.array( date_list )
date_array[ :10 ], date_array[ date_array.size - 10: ]


# In[13]:


date_array.ndim, date_array.shape, date_array.size, date_array.dtype


# In[14]:


time_array = np.array( time_list )
time_array[ :10 ], time_array[ time_array.size - 10: ]


# In[15]:


time_array.ndim, time_array.shape, time_array.size, time_array.dtype


# ### 5.2 전체 연령대

# In[16]:


age_array = np.array( age_list )
age_array[ :10 ], age_array[ age_array.size - 10 : ]


# In[17]:


age_array.ndim, age_array.shape, age_array.size, age_array.dtype


# ### 5.3 전체 성별

# In[18]:


gender_array = np.array( gender_list )
gender_array[ :10 ], gender_array[ gender_array.size - 10: ]


# In[19]:


gender_array.ndim, gender_array.shape, gender_array.size, gender_array.dtype


# ### 5.4 전체 구

# In[20]:


gu_array = np.array( gu_list )
gu_array[ :10 ], gu_array[ gu_array.size - 10: ]


# In[21]:


gu_array.ndim, gu_array.shape, gu_array.size, gu_array.dtype


# ### 5.5 전체 유동 인구수

# In[22]:


population_array = np.array( population_list )
population_array[ :10 ], population_array[ population_array.size - 10: ]


# In[23]:


population_array.ndim, population_array.shape, population_array.size, population_array.dtype


# ## 6. 데이터에 대한 통계 / 집계 출력

# ### 6.0 날짜, 시간, 성별, 연령대 목록 생성( 중복 data 배제 방법 )

# In[24]:


# 전체 날짜 목록 생성
date_unique = np.unique( date_array )
print( '데이터 수집일 : {}'.format( date_unique[ : ] ) )


# In[25]:


print( '데이터 수집 일수 : {}일'.format( date_unique.size ) )


# In[26]:


# 전체 시간 목록 생성
time_unique = np.unique( time_array )
print( '데이터 수집 시간대 : {}'.format( time_unique[ : ] ) )


# In[27]:


# 전체 성별 목록 생성
gender_unique = np.unique( gender_array )
print( '데이터 수집 성별 : {}'.format( gender_unique ) )


# In[28]:


age_unique = np.unique( age_array )
print( '데이터 수집 연령대 : {}'.format( age_unique ) )


# In[40]:


gu_unique = np.unique( gu_array )
print( '데이터 수집 구 : {}'.format( gu_unique ) )
print( '데이터 수집 구의 수 : {}개구'.format( gu_unique.size ) )


# ### 6.1 전체 데이터 수

# In[31]:


print( '총 data 수 : {}건'.format( date_array.size ) )


# ### 6.2 전체 유동 인구수

# In[32]:


print( '총 유동인구 수 : {}명'.format( population_array.sum() ) )


# ### 6.3 전체 유동 인구에 대한 평균 및 1사분위, 중앙값, 3사 분위수

# In[33]:


print( '평균 유동인구 수           : {:8.2f}명'.format( population_array.mean() ) )
print( "유동 인구에 대한 1사분위수 : {:8.2f}명".format( np.percentile( population_array, 25 ) ) )
print( "유동 인구에 대한 중앙값    : {:8.2f}명".format( np.median( population_array ) ) )
print( "유동 인구에 대한 3사분위수 : {:8.2f}명".format( np.percentile( population_array, 75 ) ) )


# ### 6.4 유동 인구에 대한 분산 및 표준편차

# In[34]:


print( '유동 인구에 대한 분산 : {:.2f}'.format( population_array.var() ) )
print( '유동 인구에 대한 표준편차 : {:.2f}'.format( population_array.std() ) )


# ### 6.5 유동 인구수가 가장 적은 날과 많은 날

# In[35]:


index = population_array.argmin()
print( '유동 인구수가 적은 날 : {}-{} {}대 {} {} {}'.format( date_array[ index ], time_array[ index ],
                                                             age_array[ index ], 
                                                             gender_array[ index ],
                                                             gu_array[ index ],
                                                             population_array[ index ] ) )
index = population_array.argmax()
print( '유동 인구수가 많은 날 : {}-{} {}대 {} {} {}'.format( date_array[ index ], time_array[ index ],
                                                       age_array[ index ], 
                                                       gender_array[ index ],
                                                       gu_array[ index ],
                                                       population_array[ index ] ) )


# ### 6.6 강남구 유동 인구 분석

# In[55]:


# 강남구 인덱스 추출
indexs = np.where( gu_unique[ 0 ] == gu_array )
indexs = indexs[ 0 ]
indexs


# In[56]:


print( '{} 전체 유동 인구수 : {:10d}명'.format( gu_unique[ 0 ], population_array[ indexs ].sum() ) )
print( '{} 평균 유동 인구수 : {:10.2f}명'.format( gu_unique[ 0 ], population_array[ indexs ].mean() ) )


# In[57]:


# 강남구 index 추출
total = 0
print( '{} 일자별 유동 인구 :'.format( gu_unique[ 0 ] ) )
for index in indexs:
    print( '{}-{} : {} {}명'.format( date_array[ index ], time_array[ index ], 
                                     gender_array[ index ], population_array[ index ] ) )


# In[58]:


# 중구 인덱스 추출
indexs = np.where( gu_unique[ 23 ] == gu_array )
indexs = indexs[ 0 ]
indexs


# In[59]:


print( '{} 전체 유동 인구수 : {:10d}명'.format( gu_unique[ 23 ], population_array[ indexs ].sum() ) )
print( '{} 평균 유동 인구수 : {:10.2f}명'.format( gu_unique[ 23 ], population_array[ indexs ].mean() ) )


# In[61]:


# 강남구 index 추출
total = 0
print( '{} 일자별 유동 인구 :'.format( gu_unique[ 23 ] ) )
for index in indexs:
    print( '{}-{} : {} {}명'.format( date_array[ index ], time_array[ index ], 
                                     gender_array[ index ], population_array[ index ] ) )


# In[ ]:




