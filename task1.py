# a = int(input('enter three-digit number: '))
# result = 0
# if a > 999 or a < 100:
#     print('entered number is not three digit')
# else:
#     for i in range(3):
#         result += a % 10
#         a //= 10
#     print('digit sum: ' ,result)

a = int(input('enter three-digit number'))
n1 = a % 10
n2 = a // 10 % 10
n3 = a // 100
print(n1 + n2 + n3)