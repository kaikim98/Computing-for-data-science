class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
    
    def is_square(self):
        a = (self.p1.x-self.p2.x)**2+(self.p1.y-self.p2.y)**2
        b = (self.p1.x-self.p3.x)**2+(self.p1.y-self.p3.y)**2
        c = (self.p1.x-self.p4.x)**2+(self.p1.y-self.p4.y)**2
        d = (self.p3.x-self.p2.x)**2+(self.p3.y-self.p2.y)**2
        e = (self.p4.x-self.p2.x)**2+(self.p4.y-self.p2.y)**2
        f = (self.p3.x-self.p4.x)**2+(self.p4.y-self.p3.y)**2
        
        L1 = [a, b, c, d, e, f]
        L2 = set(L1)
        L3 = list(L2)
        L4 = []
        for i in L1:
            if i == 0:
                return False
                break
        if len(L3) == 2:
            for i in L3:
                L4.append(L1.count(i))
        else:
            return False
        if L4 == [2, 4] or [4, 2]:
                return True
        else:
            return False