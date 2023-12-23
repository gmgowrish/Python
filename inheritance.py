class pet:  # base / super/ parent
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("not eating")

    def display(self):
        print(f"I'm {self.name} and my age is {self.age}")

    def speak(self):
        print("I dont speak ")


class dog(pet):  # derived / sub /child
    def speak(self):
        print("bark")

    def eat(self):
        print("eating biscuit")


class cat(pet):
    def speak(self):
        print("meow")

    def eat(self):
        print("drinking milk")


class fish(pet):
    pass


p = dog("tommy", 23)
c = cat("jerry", 12)
f = fish("sita", 34)
print("_____________________________________")
p.display()
p.speak()
p.eat()
print("_____________________________________")
c.display()
c.speak()
c.eat()

print("_____________________________________")

f.display()
f.speak()
f.eat()
print("_____________________________________")
