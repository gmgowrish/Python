def maxelement(arr):
    ans = 0
    for i in arr:
        if i > ans:
            ans = i

    print(ans)


maxelement([-0.0011, -0.0001, -0.00009])

