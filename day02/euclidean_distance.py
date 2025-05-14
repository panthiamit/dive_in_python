import math
x1 =int(input('enter the x co-ordinate'))
y1 = int(input('enter the y co-ordinate'))
x2 = int(input('enter the x co-ordinate'))
y2 = int(input('enter the y co-ordinate'))
ecd_distance = 0
p = int((x1-y1)*(x1-y1))
q = int((x2-y2)*(x2-y2))
ecd_distance = (p-q)**0.5
print('euclidean distancs = ',ecd_distance)