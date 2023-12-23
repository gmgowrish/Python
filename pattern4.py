def pattern4(n):
    for i in range(n):
        for j in range(i):
            print(j+1,end='')
        print('')

pattern4(5)