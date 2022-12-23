# if 4 in [1,2,3,4]:print("4가 있습니다")
#
# languages = ['python', 'perl', 'c', 'java']
# for lang in languages:
#     if lang in ['python', 'perl']:
#         print('%6s need interpreter' % lang)
#     elif lang in ['c', 'java']:
#         print('%6s need compiler' % lang)
#     else:
#         print('should not reach here')
#
# a = 1
# b = 2
# print(a+b)
#
# a = 'Python'
# print(a)
#
# a = 3
# if a > 1:
#     print('a is greater than 1')
#
# for a in [1,2,3]:
#     print(a)
#
# i = 0
# while i < 3:
#     i += 1
#     print(i)
#
# def add(a,b):
#     return a+b
# print(add(3,4))
#
#
# a = 1
# b = 2
# print(a+b)
#
# a = 3
# b = 2.4
# print(a/b)
#
# a = 3
# b = 9
# print(a*b)
#
# num1 = 4.24E10
# print(num1)
#
# num2 = 4.24e-10
# print(num2)
#
# num2 = 4.24e-10
# print('%0.12f' % num2)
# print("%20.12f" % num2)
#
# num1 = 0o177
# print(num1)
#
# num2 = 0x8ff
# num3 = 0xABC
# print(num2)
# print(num3)

# num0 = input(print('숫자를 입력하세요:'))
# 2진수:0b  8진수:0o 16진수:0x

i=1
for i in range(1,11):
    B = bin(i)
    O = oct(i)
    H = hex(i)
    print(f'%d이 2진수로는 %s' f' %d이 8진수로는 %s' f' %d이 16진수로는 %s' % (i, B, i, O, i, H))
    i += 1