data = [2,11,4,6,7,40,8,10,4,6,6,6,6,6,6,6,8,17,17,17,4,5,15,3,25]
result = 0
i = 0
for element in data :
    result = result + element
    i = i + 1
    avg = result / i
print('sum of the elements of list = ',result)
print('mean of given list = ',avg)

data.sort()
print(data)
count = 0
ans = -1
for element in data :
   k =  data.count(element)
   if count < k :
       count = k
       ans = element

print('mode of list maximum occurance of element in list ',ans,'is = ',count)