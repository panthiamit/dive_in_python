# import time
# for i in range (7,1,-1):
#     for j in range(0,i):
#         print('**',end=" ")
#     print(' ')


import random 
jackpot = random.randint(1,100)
counter = 1
guess = int(input('guess the number == '))
    
while jackpot != guess:
    if guess < jackpot:
        print('guess higher')
    else:
        print('guess lower')

    guess = int(input('again guess the number == '))
    counter+=1
    
if guess == jackpot:
    print('sahi jabab \n **you won the jackpot**') 
    print('you took ',counter,'attempts')   