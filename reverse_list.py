## list reverse
def rev_list():
    list=[4,3,5,6,8,9,1]
    copy_list=list
    ll=[]
    for i in range(len(copy_list)):
        ll.append(copy_list.pop())
    print ll,list,copy_list

rev_list()