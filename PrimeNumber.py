
for i in range(0,51):
    if i >1:
        for j in range(2,i):
            if i%j== 0:
                print "Not prime", i
                break
        else:
            print "Prime", i
