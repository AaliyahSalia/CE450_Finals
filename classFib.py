class Fibonacci():
    def __init__(self):
        self.val = 0
        self.next_val = 1

    def nxt(self):
        result = Fibonacci()
        result.val = self.next_val
        result.next_val = self.val + self.next_val
        return result

    def __repr__(self):
        return str(self.val)


a = Fibonacci()
print(a)
print(a.nxt())
print(a.nxt().nxt())
print(a.nxt().nxt().nxt())
print(a.nxt().nxt().nxt().nxt())
print(a.nxt().nxt().nxt().nxt().nxt())
print(a.nxt().nxt().nxt().nxt().nxt().nxt())


