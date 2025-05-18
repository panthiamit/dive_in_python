l =[1,2,3,5,6,5,9,24]
print(l)
l[0] = 100
print(l)
# reverse the list

# method 1
p = l[::-1]
print(p)

# method 2
l.reverse()
print('the reverse order of list = ', l)


print(l[3])


l.append(500)
print(l)

l.remove(5)
print(l)

# l.append('world')
# print(l)
# l.extend('hello')
# print(l)
# x =['world']
# print(x)
l.sort(key=None)
print(l)
print('maximun number of list = ',l[-1])
print('minimun number of list = ',l[0]) 

# insertion in list
l.insert(5,'master')
print(l)

# remove the spesific item from list
l.remove('master')
print(l)
 
#  deletion of last element from list
l.pop()
print(l)

a = l
print('new list is = ',a)

b = a
print('copy of list = ', b)

for item in l :
    item = item + 15
    print(' item in list = ',item)



# item of list call by index 
my_list = [2,3,4,1,0,6,5,10, 20, 30]
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1



# enumerate fuction take two arguments index and item variable
# enumerate funtion gives item with the index 
my_list = ['a', 'b', 'c',12 , 30 , 40, 'world']
for index, item in enumerate(my_list):
       print(f"Index: {index}, Item: {item}") 
    
# iteration on each item in list
mine = [45,56,14,98,79,12,32,88,49]
for i in mine :
     print('items in mine list is = ',i)


# 2D list (list within list)
my_list = [[45,26,58],[78,28,65],[19,20,30]]
for i in my_list :
    for item in i :
      print('new list added = ',item)


# 2D list (MATRIX form)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix :
    print(end = '\n')
    for item in row :
        if item is not row[-1] :
          print(item,end= ',')
        else :
          print(item)



common_list = [50,40,16,3,97,45,99,22,62,85,79]
res = common_list[0]
for item in common_list :
    if res  < item :
        res = item
print('maximum number in a list = ',res)


min = common_list[0]
for item in common_list :
    if min > item :
        min = item
print('minimum number in list = ',min)





