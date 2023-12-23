s = 'chris alan'
# for i in s.split():
#     s = s.replace(i, i.capitalize())
# print(s)

b = list(s)
c = ''.join(b)
d = c.split()
for i in d:
    print(i.capitalize(), end=' ')


print(s.split())  # converting the string to list  ['chris', 'alan']
