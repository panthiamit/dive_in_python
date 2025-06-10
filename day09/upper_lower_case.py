s = 'This is  Clear Cut Case of Misunderstanding '
def up_low_case(s) :
    lower_char = 0
    upper_char = 0
    for c in s :
        if c.isupper():
             upper_char += 1
           
        
        elif c.islower():
             lower_char += 1
           
        
        else :
            pass
    
    print('total no. of lower character = ',lower_char)
    print('total no. of upper character = ',upper_char)

up_low_case(s)