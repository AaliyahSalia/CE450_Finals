class Fibonacci():
    def __init__(self):
        self.val = 0
        self.pre = 0

    def nxt(self):
        """ YOUR SOURCE CODE HRER """
        if self.val == 0:
            self.val = 1
            self.pre = 0
        else:
            self.val = self.val + self.pre
            self.pre = self.val - self.pre
        return self
    
    def __repr__(self):
        return str(self.val)

    

a = Fibonacci()
print(a)

a.nxt()
print(a)

a.nxt()
print(a)

a.nxt()
print(a)

a.nxt()
print(a)

a.nxt()
print(a)

a.nxt()
print(a)






