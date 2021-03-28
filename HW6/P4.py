class Calculator:
    def __init__(self):
        self = 0
    
    def digit(self, num):
        return str(self) + str(num)
        
    def plus(self):
        if list(self)[-1] == '-' or '+':
            return self.replace(list(self)[-1], str('+'))
        else:
            return int(self) + '+'
    def minus(self):
        if list(self)[-1] == '-' or '+':
            return self.replace(list(self)[-1], str('-'))
        else:
            return int(self) + '-'
    def clear(self):
        return 0
        
    def equal(self):
        return print(int(self))
    
c = Calculator()
c.digit(1)
c.digit(2)
c.plus()
c.minus()
c.digit(3)
c.digit(1)
c.digit(2)
c.plus()
c.digit(0)
c.digit(0)
c.digit(1)
c.digit(0)
c.digit(0)
c.equal()