
def pattern3(n):
    for i in range(1,n):
        for j in range(n-i):
            print(i ,end='')

        print('')

pattern3(6)

# output

# 1111
# 222
# 33
# 4