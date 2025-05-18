
def square_sum(a,b,c) :
    result = a*a + b*b + c*c
    return result

a,b,c =map(int,input("enter 3 numbers").split(','))
sum = square_sum(a,b,c)
print('sum of squares =', sum)
