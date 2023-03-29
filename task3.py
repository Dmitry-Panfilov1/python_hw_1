# a = str(input('enter six-digit number')) 
# print(type(a))                          
# result1 = 0                              
# result2 = 0
# for i in range(len(a)):
#     if i < len(a) / 2:
#         result1 += int(a[i:i+1])
#     else:
#         result2 += int(a[i:i+1])
# if result1 == result2:
#     print('lucky ticket!!')
# else:
#     print('bad luck.')

a = int(input('enter six-digit number'))
n1 = a % 10
n2 = a // 10 % 10
n3 = a // 100 % 10
n4 = a // 1000 % 10
n5 = a // 10000 % 10
n6 = a // 100000 % 10
result1 = n1 + n2 + n3
result2 = n4 + n5 + n6
if result1 == result2:
    print('lucky ticket!!')
else:
    print('bad luck.')