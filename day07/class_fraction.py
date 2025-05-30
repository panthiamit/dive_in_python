class Fraction :
    def __init__(self,n,d) :
        self.nume = n
        self.deno = d

    def __str__(self) :
        return "{}/{}".format(self.nume , self.deno)

    def __add__(self,other) :
        temp_nume = self.nume * other.deno + other.nume + self.deno
        temp_deno = self.deno * other.deno
        return "{}/{}".format(temp_nume ,temp_deno)

    def __sub__(self ,other) :
        temp_nume = self.nume * other.deno - other.nume * self.deno
        temp_deno = self.deno * other.deno
        return "{}/{}".format(temp_nume , temp_deno)
    
    def __mul__(self,other) :
        temp_nume = self.nume * other.nume
        temp_deno = self.deno * other.deno
        return "{}/{}".format(temp_nume ,temp_deno)
    
    def __truediv__(self ,other) :
        temp_nume = self.nume * other.deno
        temp_deno = self.deno * other.nume
        return "{}/{}".format(temp_nume , temp_deno)
        


x = Fraction(3,7)
print(x)
y = Fraction(4,5)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)