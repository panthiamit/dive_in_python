def reverse_num(num) :
    reversed_num = 0
    while num > 0 :
        digit = num%10
        reversed_num = reversed_num *10 + digit
        num = num //10
    return reversed_num
for i in range(5):
    try:
        num = int(input('enter any four digit number =')) 
        reversed_num = int(reverse_num(num))
        print("reverse number of your given number is = ", reversed_num) 
    except:
        print(' enter only integer value')