def magicIndex(a, n):
    ans = -1
    for i in range(n-1):
        if a[i] == i:
            ans = i

    print(ans)


magicIndex([2 ,3 ,4 ,5 ,6],5)
