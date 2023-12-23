# x = ["slithy", [7, 10, 12], 2, "tove", 1]  # Statement 1
# y = x[0:50]  # Statement 2
# z = y  # Statement 3
# w = x  # Statement 4
# x[0] = x[0][:5] + 'ery'  # Statement 5
# y[2] = 4  # Statement 6
# z[4] = 42  # Statement 7
# w[0][:3] = 'fea'  # Statement 8
# x[1][0] = 5555  # Statement 9
# a = (x[4][1] == 1)

b = [23, 44, 87, 100]
# print(b)

a = b[1:]
# print(a)
d = b[2:]
# print(d)
c = b

d[0] = 97

c[2] = 77
print(a[1], b[2], c[2], d[0])

startmsg = "python"
endmsg = ""
for i in range(1, 1 + len(startmsg)):
    endmsg = startmsg[-i] + endmsg
print(endmsg)


def mystery(l):
    l = l[1:]
    return ()


mylist = [7, 11, 13]
mystery(mylist)
print(mylist)


def factors(n):
    factorlist = []
    for i in range(1, n + 1):
        if n % i == 0:
            factorlist.append(i)
    return factorlist


def isprime(n):
    return factors(n) == [1, n]


def primeproduct(n):
    for i in range(1, n + 1):
        if n % i == 0:
            if isprime(i) and isprime(n // i):
                print(True)
    print(False)


primeproduct(118)


def delchar(s, c):
    if len(c) != 1:
        return s
    snew = ""
    for char in s:
        if char != c:
            snew = snew + char
    return snew


# delchar("banana", "b")
#
# delchar("banana", "a")

def shuffle(l1, l2):
    if len(l1) < len(l2):
        minlenght = len(l1)
    else:
        minlenght = len(l2)
    shuffled = []
    for i in range(minlenght):
        shuffled.append(l1[i])
        shuffled.append(l2[i])
    shuffled = shuffled + l1[minlenght:] + l2[minlenght:]
    return shuffled


shuffle([0], [1, 3, 5])
