def factorial(n) :
    if n==0 :
        return 1
    else :
        result = n*factorial(n-1)
        return result
        # return n*factorial(n-1)
print(factorial(6))
print('ans is = ',factorial(4))