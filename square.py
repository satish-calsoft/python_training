num = int(raw_input('Enter the number:'))

for i in range(num):
    if i == 0:
        print(' *' * (num)+'*')
    elif i >= 1:
        print ((' ' * (i-(i))+'*') + (' ' * (num*2)+'*'))
print(' *' * (num)+'*')      