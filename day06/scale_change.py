option = input('select any option \t\n 1 >> cm to meter \t\n 2 >> km to miles \t\n 3 >> USD to INR \t\n 4 >> exit \t\n  ... ')

try:
    option = int(option)

except Exception as e:
    print('error in converting to int: ', e)
    



if option == 1 :
    c_m = int(input('enter the centi meter value ')) 
    meter = c_m / 100
    print(c_m ,'cm = ', meter ,'meter' )

elif option == 2:
    input('enter the km distance')

elif option == 3 :
    input('enter the USD ammount')
elif option == 4 :
    exit()
else :
    print('invalid input') 
