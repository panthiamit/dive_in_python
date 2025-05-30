import random
x = random.randint(1,10)
for i in range(0,3) :
    num = int(input('enter any number between 1 to 10 >> '))  
    if num > x :
                print('guess number is greater than the random number')
    elif num < x :
                print('guess number is lower than the random number')
    else :
                print('guess number is equal to random number')
        
print('your attempts are over, number is ', x)
