#using arguemnts--if we pass arguments we can change the input every time by calling this fn.
'''def prime(list1):
    l1= []
    for i in list1:
        if i > 1:
            for j in range(2,i):
                if i%j == 0:
                  break
            else:
                    l1.append(i)
    return  l1
                    
fn= prime(range(50))
print fn'''


#without  using arguments if we specify range(50 in the fn itself,every time we cal this fn the op will be same if we dont give arguments.)
def prime( ):
    l1= []
    for i in range(50):
        if i > 1:
            for j in range(2,i):
                if i%j == 0:
                  break
            else:
                    l1.append(i)
    return  l1
                    
fn= prime()
print fn
