num = input('enter any number = ')
total_digit = len(num) 
result = 0 
num = int(num)
x = num
while num != 0  :
        digit = num % 10
        result = digit ** total_digit + result
        sum = result
        num = num//10
if result == x :
        print('given number is armstrong number', result)

else :
        print('given number is not armstrong number', result)
