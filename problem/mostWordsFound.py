sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
ans = 0
for i in sentences:
    print(i)

    pr = len(i.split())
    # print(pr)
    if pr > ans:
        ans = pr
        print(ans)
        print(pr)
print(ans)



""" 



"""