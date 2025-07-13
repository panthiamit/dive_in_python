def summation(n):
    sum = 0
    for j in range(1,n+1):
        sum = sum + j
        for i in range(1 , j +1) :
            print(i, sep = ' ' , end=' ')
            if i < j:
                print('+', sep=' ', end=' ')
        
        print("=", sum)




def summation_with_pattern(n):
    sum = 0
    pattern = '0=0'
    L = []
    digit_incre_flag = 0
    for i in range(1, n+1):
        sum = sum + i
        # 1+2=3
        k = len(str(sum)) + 1
        pattern = pattern[:-k] + ' + ' + str(i)
        pattern = pattern + '=' + str(sum)
        print(pattern)



def summation_of_numbers(n):
    sum = 0
    p = ['0' , '=' ,'0']
    for num in range(1 , n+1) :
        sum = sum + num 
        # print(sum)
        p.insert(-2,'+')
        p.insert(-2, str(num))
        p[-1] = str(sum)
        if num ==1:
            p = p[2:]

        print(" ".join(p))


                

summation_with_pattern(6)





# """
# Q:
# "({[]}{[]}[[[[]]])"
# """ 
# para = "({[]}{[]}[[[[]]]])"
# def is_valid_paranthesis(s):
#     complements = {'(' : ')',
#          '{' : '}',
#          '[' : ']'
#          }
#     stack = []
#     for braket in s :
#         if braket in complements.keys() :
#             stack.append(braket)
#         elif complements[stack[-1]]==braket :
#             stack.pop()
#         else:
#             return False
#     return not stack

# print(is_valid_paranthesis(para))





# a = [1,2]

# a = None

# if a:
#     print ('a is not empty')
#     print(a[0])