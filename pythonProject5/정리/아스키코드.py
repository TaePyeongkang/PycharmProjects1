#아스키코드 16진수
a = ord(input('알파벳를 입력하세요'))
b = int(input('숫자를 입력하세여'))
c = a*b
print(str(c).zfill(8))