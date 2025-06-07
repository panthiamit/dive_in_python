s = "abcd1234"

def rev_str(s) :
    str01 = ' '
    length = len(s)
    while length > 0 :
        str01 = str01 + s[length -1]
        length = length -1
    return str01
x = rev_str(s)
print(x)
print(rev_str(s))
