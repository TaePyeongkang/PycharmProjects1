a = '123456789'
# print(a[0])
# print(a[2])
# print(a[4])
# print(a[6])
# print(a[8])
hol = []
for i in range(0,len(a)):
    if int(a[i]) % 2 == 1:
        print(a[i])
        hol.append(a[i])
print(hol)
hol = list(map(int, hol))
hol_sum = sum(hol)
print(sum(hol))