for i in range(1,101): 
    for j in range(2,101):
        for k in range(3,101):
	    if (k*k == i*i + j*j) and (i<j<k):
		print(i, j, k)
