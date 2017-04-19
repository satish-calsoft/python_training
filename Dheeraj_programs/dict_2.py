l_keys = [1,2,3,4,5,6,7,8,9,10]
l_values = ['a','b','c','d','e']

dict = {}

for i in range(len(l_keys)):
    if i in range(len(l_values)):
        dict[l_keys[i]] = l_values[i]
    else:
        dict[l_keys[i]] = 'There is no value'
        
print dict