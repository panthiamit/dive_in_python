class A:
    def m1(self):
        return 20
    

class B(A):
    def m1(self):
        return 30
    def m2(self):
        return 40
    
class C(B):
    def m2(self):
        return 50
    

o1 = A()
o2 = B()
o3 = C()

print(o1.m1()+o2.m1()+o3.m2())