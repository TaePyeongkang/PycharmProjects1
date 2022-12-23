# #51번 문제 리스트 생성
# movie_rank = ['닥터스트레인지', '스플릿', '럭키']
# print(movie_rank)
#
# #52번 문제 51번에 리스트에 배트맨 추가하기
# movie_rank.append('배트맨')
# print(movie_rank)
#
# #53번 문제 movie_rank 리스트에 "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하기
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1,'슈퍼맨')  #p.83 inset기본형 inset(a, b) a는 요소위치에, b를 삽입하는 함수이다.
# print(movie_rank)
#
# #54번 문제 movie_rank 리스트에서 '럭키'를 삭제하기.
# movie_rank = ['닥터스트레인지', '스플릿', '럭키']
# del movie_rank[2] #p.79 del기본형 del a[]//[]에 배열번호를 넣으면 그에 해당하는 요소값을 제거해준다.
# print(movie_rank)

#55번 문제 movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하기.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del movie_rank[2:4]
# print(movie_rank)

# #56번 문제 lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들기.
# lang1 = ['닥터스트레인지', '스플릿']
# lang2 = ['스플릿', '배트맨']
# print(lang1+lang2) #p.77 리스트 더하기 리스트 + 리스트

#57번 문제 리스트에서 최댓값과 최솟값을 출력하기.
# nums = [1, 2, 3, 4, 5, 6, 7]  #구글링 검색 최대값 구할때 함수 max(),최소값 구할때 함수 min()을 사용한다.
# max(nums)
# min(nums)
# print('최대값은? %d' %(max(nums)))
# print('최솟값은? %d' %(min(nums)))

# #58번 문제 리스트의 합을 출력하라.
# nums = [1, 2, 3, 4, 5] #구글링 검색 총합 구할때 총합을 저장할 변수 만들고 sum()함수를 사용
# sum_nums = sum(nums)
# print('리스트의 총합은 %d 입니다'% (sum_nums))

#59번 문제 리스트에 저장된 데이터의 개수를 화면에 구하기.
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# print(len(cook)) #p.78 리스트 길이 구하기 len() 함수를 사용한다

#60번 문제 리스트의 평균을 출력하기.
# nums = [1, 2, 3, 4, 5]
# sum_nums = sum(nums) #총합 구하고
# average = sum(nums)/len(nums) #총합에 개수를 나누기
# print(average)

#61번 문제 price 변수에 날짜 정보를 제외하고 가격 정보만을 출력하기.
# price = ['20180728', 100, 130, 140, 150, 160, 170] #날짜를 제외하고 출력해야하니 슬라이싱 쓰고 1번째 요소부터 출력
# # 기본형은 print(a[:])
# print(price[1:])

#62번 문제 슬라이싱을 사용해서 홀수만 출력하기.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nums_ = nums[0] + nums[2] + nums[4] + nums[6] + nums[8]#생각난대로 해봤으나 리스트들을 더하는게 되어버림
# print(nums_)  #[start:stop:step].step 수 만큼 점프를 해가면서 슬라이스를 하게 됨.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])# 시작점 0부터 끝까지 실라이싱을 하는 범위인데 step에 2가 들어가서 0,2,4,6,8까지 실라이싱이 진행된다.

#63번 문재 슬라이싱을 사용해서 짝수만 출력하기.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])

#64번 문제 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하가.
# nums = [1, 2, 3, 4, 5]
# nums.reverse()
# print(nums)

#65번 문제
# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0],interest[1],interest[2])

#66번 문제 join 메서드
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(' '.join(interest))

#67번 문제 join 메서드  /사용하기
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print('/'.join(interest))

#68번 문제 join 매서드 \n사용하기
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print('\n'.join(interest))

# #69번 문제 문자열 split 메서드
# string = "삼성전자/LG전자/Naver"
# interest = string.split('/')
# print(interest)

#70번 문제 리스트 정렬
# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)

#71번 문제 my_variable
# my_variable = ()
# print(type(my_variable))

#72번 문제