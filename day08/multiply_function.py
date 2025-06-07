l = [6,20,9,8,4,10,9,2,]


def multiply_list(l) :
    result = 1
    for num in l :       
      result = result * num
      print(result)
    return result
    

ans = multiply_list(l)
print(ans)

dict_dd = {'name = ':'Amit','age = ':27,'educaion >> ':{'school_1':'Admv','school_2':'Jnv','college':'Manit'},'work >> ':{'2019 to2022':'company01','2022 to 2024':'company02'}}
# print(dict_dd)
x = dict_dd.keys()
y = dict_dd.values()
z = dict_dd.items()
for items in dict_dd :
    # print(k ,v)
    print(items())
# for item in dict_dd :
#     print(f"{dict_dd.keys()}'\n\t',{dict_dd.values()},'\n\t',{dict_dd.items()}" )