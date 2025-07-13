def febonacci(n):
    if n == 0:
        return 0
    elif n== 1:
        return 1
    else :
        return  febonacci(n - 1) + febonacci(n - 2)
    
for num in range(7):
    print(febonacci(num), end = ' ')
 
# print(febonacci(7))




# def febonacci_series(num):
#     a,b = 0,1
#     for counter in range(num):
#         print(a , end = ' ')
#         a , b = b , a+b


# print(febonacci_series(7))