
"""
Q:
"({[]}{[]}[[[[]]])"
""" 
para = "({[]}{[]}[[[[]]]])"
def is_valid_paranthesis(s):
    complements = {'(' : ')',
         '{' : '}',
         '[' : ']'
         }
    stack = []
    for braket in s :
        if braket in complements.keys() :
            stack.append(braket)
        elif complements[stack[-1]]==braket :
            stack.pop()
        else:
            return False
    return not stack

print(is_valid_paranthesis(para))





a = [1,2]

a = None

if a:
    print ('a is not empty')
    print(a[0])