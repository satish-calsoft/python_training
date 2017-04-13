def pythagorean_theorem(userData):
    for i in range(2,userData):
        for j in range(2,userData):
            for k in range(2,userData):
                if i*i + j*j == k*k:
                    print i, j, k
                


pythagorean_theorem(50)



