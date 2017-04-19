choice = input("Enter value choice for range : ")
#(a*a) + (b*b) = (c*c)
for a in range(1,choice):
    for b in range(1,choice):
        for c in range(1,choice):
            if a*a + b*b == c*c and a<b<c:
                print a,b,c
            else:
                continue

        