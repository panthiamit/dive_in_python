x = int(input('enter any year = '))
if x % 400 == 0 :
        print('given year is leap year')
elif x % 4 ==0 and x % 100 != 0 :
        print('given year is leap year')
elif x % 4 ==0 and x % 100  ==0 :
        print('given year is not a leap year')
else :
        print('given year is not a leap year')