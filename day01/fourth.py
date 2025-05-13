
def sum_of_digits(num):
    digit_sum = 0 

    while num > 10 :
        x = num%10
        num = num //10    
        digit_sum = digit_sum + x

    digit_sum = digit_sum + num
    return digit_sum
num = int(input('enter any three digit number')) 

a = sum_of_digits(num)
print(a)
    