a = int(input('enter total crane number'))
if a % 6 != 0:
    print('no integer solution')
else:
    print('Petya and Sergey made: ', a / 6)
    print('Kate made: ', a / 3 * 2)