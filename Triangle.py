
def triangle_print(userValue):
    decrement = userValue
    increment = 1
    for i in range(userValue):
        print decrement*" "+increment*"* "
        decrement = decrement - 1
        increment = increment + 1

triangle_print(10)


def triangle_print1(userValue):
    decrement = userValue
    increment = 1
    for i in range(userValue):
        if i < 2:
            print decrement*" "+increment*"* "
        if 2 <= i < (userValue-1):
            print decrement*" "+"* "+(2*i-2)*" "+"* "
        if i == userValue-1:
            print decrement*" "+increment*"* "
        decrement = decrement - 1
        increment = increment + 1

triangle_print1(20)

