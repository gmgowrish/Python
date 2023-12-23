fm = [1, 2, 3, 6]
fn = [1, 2, 4]
cf = []

for f in fm:
    if f in fn:
        cf.append(f)
print(cf[-1])
