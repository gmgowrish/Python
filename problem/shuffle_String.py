s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
# test = list(map(list,s))

test = list(zip(s, indices))
sorted_data = sorted(test, key=lambda x: x[1])
result = ''.join([x[0] for x in sorted_data])
print(result)
