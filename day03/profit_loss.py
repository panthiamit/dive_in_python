cs = int(input('cost price of goods '))
sp = int(input('selling price of goods '))
if sp > cs :
    p = sp-cs 
    print('profit = ', p)
else :
    loss = cs - sp
    print('loss = ',loss)