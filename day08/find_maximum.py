l = [9,37,5,9,22,57,23,6,15,87,34,5]
 


def max(l) :
    temp_max = l[0]
    for num in l :
        if num > temp_max :
            temp_max = num 
    return temp_max

def total(l) : 
    sum = 0
    for num in l :
        sum = sum + num
        print(sum)
    return sum 

result = total(l)
print(result)    

print('hello')
ans = max(l)
print(ans)