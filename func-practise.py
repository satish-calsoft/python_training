def summ(*args):
    c = 0
    for i in args:
        c = c + i
        if i == 3:
            c = 3
            break
    return c
print "result is", summ(5,3,2)
################
def sum(*args):
    c = 0
    for i in args:
        break
        c = c + i
        if i == 3:
            c = 3
        break
    return c
print "result is", sum(5,3,2)
####################
def sum(*args):
    c = 0
    for i in args:
        c = c + i
        return args
        if i == 3:
            a = 3
            return a
    return c
print "result is", sum(5,3,2)
#################################
def sum(*args):
    c = 0
    for i in args:
        c = c + i
        if i == 3:
            a = 3
            return a, c
    return c  #####after return stamts willnot execute
print "result is", sum(5,3,2)