# class Creditcard:
#     def __init__(self, cardNumber):
#         self.__cardNumber = cardNumber  # Private Attribute
#
#
#     def useCard(self):
#         print(f"credit card {self.__cardNumber} used")
#
#
# c = Creditcard(12345)
# print(c._Creditcard__cardNumber)
# c.useCard()

# a, b = 12, 5
# if a + b:
#     print("True")
# else:
#     print("False")

def g(y):
    b = 0
    while y >= 3:
        (y, b) = (y / 3, b + 1)
    print(b)


# g(728)


#  assignment 2


def f(n):
    s = 0
    for i in range(2, n):
        if n % i == 0 and i % 2 == 1:
            s = s + 1
            print(s)
    print(s)


# f(90) 5 -0 = 5
# f(89)


def h(n):
    s = True
    for i in range(1, n + 1):
        if i * i == n:
            s = False
        print(i*i)


h(5)
