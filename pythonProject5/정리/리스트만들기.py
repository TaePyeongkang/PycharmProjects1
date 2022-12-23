# print(' 출석부')
#
# attendance_list = ['1'' 강민영 ',
#         '2' ' 고연재 ',
#         '3' ' 김기태 ',
#         '4' ' 김명은 ',
#         '5' ' 김성일 ',
#         '6' ' 김연수 ',
#         '7' ' 김재일 ',
#         '8' ' 노도현 ',
#         '9' ' 류가미 ',
#         '10' ' 박규환 ',
#         '11' ' 박성빈 ',
#         '12' ' 박시형 ',
#         '13' ' 박의용 ',
#         '14' ' 오송화 ',
#         '15' ' 이범규 ',
#         '16' ' 이보라 ',
#         '17' ' 이소윤 ',
#         '18' ' 이여름 ',
#         '18' ' 이지혜 ',
#         '20' ' 이현도 ',
#         '21' ' 임성경 ',
#         '22' ' 임영효 ',
#         '23' ' 임홍선 ',
#         '24' ' 장은희 ',
#         '25' ' 정연우 ',
#         '26' ' 정철우 ',
#         '27' ' 주민석 ',
#         '28' ' 최지혁 ']
#
# for i in attendance_list:
#         print(attendance_list[i])
# list = ''
# print('출석부')
# print('------------------')
# list += '김기태'
# list += '이범규'
# list += '박의용'
# list += '임영효'
# list += '김재일'
#
# for i in list (1,28):
#         print(list)


# print('-----------------')
# print('\t  출석부')
# print('-----------------')
# a=''
# print(a)
# a += '김기태 '
# print(a)
# a += '이범규 '
# print(a)
# a += '박의용 '
# print(a)
# a += '임영효 '
# print(a)
# a += '김재일'
# print(a)

# print('-----------------')
# print('\t  출석부')
# print('-----------------')
# list = ['이범규 ','박의용 ','임영효 ','김재일 ']
# a = '김기태 '
# print(a)
# for i in range(0,4):
#     print(a+list[i])
#     a += list[i]

# print('-----------------')
# print('\t  출석부')
# print('-----------------')
# seat = {1:'김기태',2:'이범규',3:'박의용',4:'임영효',5:'김재일'}
# for key,value in seat.items():
#     print(key, value)

# print('-----------------')
# print('\t  출석부')
# print('-----------------')
# name_dict = dict()
# num_list = [2,1,3]
#
# idx = 0
#
# idx += 1
# name_dict[idx] = '고연재'
#
# idx += 1
# name_dict[idx] = '김기태'
#
# idx += 1
# name_dict[idx] = '강민영'
#
# print(name_dict)
# print(name_dict.keys())
# print(name_dict.values())
#
#
# idx = 0
# for i in range(3,0,-1):
#     idx += 1
#     print(f'{name_dict[num_list[i-1]]}님의 출석 번호는 {idx}이고, 가입 순서는 {num_list}')


#자리수 구하기
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
print(len(numbers)) #리스트안에 9개요소 len을 사용해서 알 수 있음 그럼 자리수를 알땐?

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# str(numbers) #문자열로 변경
# print(numbers)
# print(len(str(numbers)))
holzzak =['홀수','짝수']
# print(holzzak)
# print(len(holzzak))

for number in numbers: #numbers리스트 안에 하나의 number들이 들어가게되고
    print('{}는 {}입니다.' .format(number, holzzak[number % 2])) #첫번째{}는 numbers안에 있는 각각number가 들어가게되고 holzzak안에 number를 2을 나누고

