class Calc:
    """Creates a basic calculator."""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return  self.a + self.b

    def subtract(self):
        return self.a - self.b
        
    def multiply(self):
        return self.a * self.b
        
    def divide(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero!")
        return self.a / self.b

class ModulusFunc(Calc):
    """Class adds a modulus division method and inherits from the parent class above."""
    def __init__(self, a, b):
        super().__init__(a,b)
        
    def mod_division(self):
        return self.a % self.b 

