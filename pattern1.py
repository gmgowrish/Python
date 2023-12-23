def patt1(n):
    for i in range (0,n):
        for j in range(0,n-i):
            print("#",end='')

        print()  


    for i in range (0,n):
        for j in range (0,i+1):
            print("#",end='')

        print('')


    for i in range(n):
        for j in range (n-i): # for incressing to decressing we use the n-i
            print( ' ',end='')  # for space 

        for k in range (i+1):  # for decressing to incressing we use the i+1
            print("#",end='')  # in this we print # 
        print('')
patt1(5)



# for i in range(5):
#     for j in range (5-i):
#         print( ' ',end='')

#     for k in range (i+1):
#         print("#",end='')
#     print('')
