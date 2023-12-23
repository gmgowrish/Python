s = "   fly me   to   the moon  "
lis = list(s.split(" "))
print(len(lis[-1]))


i = len(s) - 1

while i >= 0 and s[i] == ' ':
    i -= 1
lastIndex = i
while i >= 0 and s[i] != ' ':
    i -= 1

print(lastIndex - i)