# sorting using the lambda

# to add the two number using the lambda
result = lambda x, b: x + b
print(result(3, 4))

# example two
add = lambda x: x + 100
print(add(50))

# Example 3 of the lambda function without creating the variable

print((lambda a, b: a * b)(5, 7))

# Using the 3 argument

product = lambda x, y, z: x * y * z
print(product(z=5, x=10, y=4))

add_ = lambda x, y=15, z=24: x + y + z
print(add_(20))


