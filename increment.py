def incre(n): 
    
    if n <= 0:
        return []
    else:
        j= incre(n-1)
        # count = n + j[-1]
        if j:
            count = n + j[-1]
        else:
            count = n

        return [count] ,j

    
n = 10
a = incre(n)

print(a)


# def incre_sequence(n):
#     if n <= 0:
#         return []
#     else:
#         prev_sequence = incre_sequence(n - 1)
#         current_increment = n + prev_sequence[-1] if prev_sequence else n
#         return prev_sequence + [current_increment]

# n = 10
# sequence = incre_sequence(n)
# print(sequence)
