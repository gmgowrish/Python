a = [1, 2, 4]
b = [1, 3, 4]

c = a + b

for i in c:
    if c[i] > c[i + 1]:
        c[i], c[i + 1] = c[i + 1], c[i]

print(c)
