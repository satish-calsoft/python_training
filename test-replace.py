with open("circle.py",'r+') as f:
    a = f.read()
    spt = (" ","\n")
    for i in spt:
        a = a.replace(i, " ")
    c = a.split()
    print c