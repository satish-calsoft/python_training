num = int(raw_input('Enter the number:'))
num = num * 2

for i in range(num):
    if i == 0:
        print ((' ' *  (num))+'*')
    elif i >= 1:
        print ((' ' * (num-i)+ '* ' ) + (' ' *(i*2-1)+'*' ))
print ((' *' * (num)+' *'))  