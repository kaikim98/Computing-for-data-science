class Calculator:
    def __init__(self):
        
        self.buffer = ""
        self.formula = []
    
    def digit(self, num):
        num = str(num)
        self.buffer += num
        
    def plus(self):
        if self.buffer != "":
            self.buffer = int(self.buffer)
            self.formula.append(self.buffer)
        self.formula.append('+')
        self.buffer = ""
    def minus(self):
        if list(self)[-1] == '-' or '+':
            return self.replace(list(self)[-1], str('-'))
        else:
            return int(self) + '-'
    def clear(self):
        self.buffer = ""
        self.formula = []
        
    def equal(self):
        if self.buffer != "":
            self.buffer = int(self.buffer)
            self.formula.append(self.buffer)
        
    
c = Calculator()
c.digit(0)
c.digit(1)
c.digit(2) #buffer
c.plus() # buffer to list + '+'
c.digit(3)
c.digit(2)
c.digit(1) #buffer 
c.equal() #bufferto list + calculation
print(c.formula)
# c.equal()