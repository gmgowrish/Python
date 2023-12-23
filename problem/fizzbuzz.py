n = 15
append = []
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        append.append('FizzBuzz')
    elif i % 3 == 0:
        append.append('Fizz')
    elif i % 5 == 0:
        append.append('Buzz')
    else:
        append.append(str(i))
print(append)
