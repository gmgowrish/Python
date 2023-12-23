import math

def smallestelement(arrr):
    ans = math.inf
    for i in arrr:
        if i < ans:
            ans = i
    print(ans)


smallestelement([1, 2, 3, 4, -1])
