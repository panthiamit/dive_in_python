age1 = input('enter first age =')
age2 = input('enter second age =')
age3 = input('enter third age =')
if age1 > age2 :
    if age1 > age3 :
        print('first is oldest =',  age1)
    else :
        print('third is oldest =',age3)   
else :
    if age2 > age3 :
        print('second is oldest =',age2)
    else :
        print('third  is oldest =',age3)   
                                        
                                        
                                        
  #first concept is end





num1 = input('num1 =')
num2 = input('num2 =')
num3 = input('num3 =')
def comparision (num1,num2,num3):
    oldest = max(num1,num2,num3)
    return oldest
print('largest number is =',comparision(num1,num2,num3))

