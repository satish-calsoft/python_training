Actual_Str=raw_input("Enter the actual string: ")
Input_Str=raw_input("Enter the input string: ")

for i in Actual_Str:
    for j in Input_Str:
        if i==j:
            print "Identical", i
            break
#print i
        
'''if Actual_Str == Input_Str:
    print "Indentical"
else:
    print "Non Identical"'''

