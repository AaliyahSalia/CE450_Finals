class Student:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def __str__(self):
        return str(self.courses)

    def __repr__(self):
        return str(self)

    def __add__(self, st):
        return Student("", self.courses + st.courses)

    def __lt__(self, st):
        return self.courses < st.courses

    def __eq__(self, st):
        return self.courses == st.courses

    def __ne__(self, st):
        return self.courses != st.courses

    def __gt__(self, st):
        return self.name > st.courses

a = Student('Peter', 3)

b = Student('Mike', 4)

c = Student('John',5)

d = Student('Kelvin', 3)

print(a+b+d)
print(a!=d)
print(b<c)
