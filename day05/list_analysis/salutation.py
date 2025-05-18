name = input('enter your name')
sal = input('enter the salutation')
#print("hello mister",name ,sal,"how are you")
#print(f"Hello {sal} {name}. How are you?")


def print_welcome(a):
    print(a)

print_welcome("Hello {0} {1}. How are you?".format(sal,name))