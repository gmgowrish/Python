import array as arr


# my_array = arr.array('i', [1, 3, 5, 6])
def pr(a, n):
    for i in range(n + 1):
        print(a[i], end=' ')
    print()


# creating an array
a = arr.array('i', [1, 3, 5, 6])

pr(a, 3)

# inserting a new element
a.insert(1, 4)

pr(a, 4)

# append a new element

a.append(7)

pr(a, 5)

# fetch the element
print(a[4])

# delete the element

# remove the element
a.remove(4)

pr(a, 4)

# pop the element

a.pop()

pr(a, 3)

# sort the array
