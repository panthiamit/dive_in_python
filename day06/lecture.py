def return_sum(func,L) :
    result=0

    for i in L :
      if func(i):
        result = result + i
        
    return result


L = [23,42,45,56,34,5,7,53,75,4,7,]

a=lambda x:x%2==0
b=lambda y:y%2!=0
c=lambda z:z%3==0

print(return_sum(a,L)) 
print(return_sum(b,L))
print(return_sum(c,L))