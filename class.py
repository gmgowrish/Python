# creating the class blueprint
class human:
    # 'Human class Implementation'
    def __init__(self, height, name, age):  # Constru ctor,  when we created the object it is invoked
        print("hey , init invoked")
        self.height = height
        self.name = name
        self.age = age

    def set_age(self, age):
        self.age = age

    def work(self):
        print("working !")

    def eat(self):
        print("Eating")


h = human(4.5, "gmg", 34)  # instantiating an objects
g = human(4.3, "dilip", 23)
print(h.name)  # access constructor
print(h.height)
print(h.age)
print(g.age)
print(human.__doc__)
h.set_age(25)
print(h.age)
h.work()
