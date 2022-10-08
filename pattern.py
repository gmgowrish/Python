# # 1 for this pattern
# #####
# #####
# #####
# #####
# #####

for i in range(5):
    for j in range(5):
        print("#", end="")
    print()

# # 2 for this pattern
# # $
# # $$
# # $$$
# # $$$$
# # $$$$$

# for i in range(5):
#         for j in range(i):
#             print("$",end="")
#         print()  


# # 3 for this pattern:
# #####
# ####
# ###
# ##
# #
# n='#'
# for i in range(5):
#     for j in range(i,5):
#        print(n, end=" ")
#     #    n = n + 1
#     print()    


# # for this pattern
# # 1 
# # 2 3 
# # 4 5 6 
# # 7 8 9 10 

# n=1
# for i in range(5):
#     for j in range(i):
#        print(n, end=" ")
#        n = n + 1
#     print() 


n = int(input("enter thr rows"))

a = n
