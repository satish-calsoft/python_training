Actual_Str=raw_input("Enter the actual string: ")
Input_Str=raw_input("Enter the input string: ")

if len(Actual_Str)==len(Input_Str):
    for i in Actual_Str:
        if i in Input_Str:
            print "Identical", i
        else:
            print "Not Identical"
            break

        

