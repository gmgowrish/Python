def maximumWealth(accounts):
    max_wealth = 0
    wealth = 0
    for i in accounts:
        print(i)
        wealth = sum(i)
        print(wealth)
        max_wealth = max(wealth, max_wealth)

    print(max_wealth)


maximumWealth([[1, 5], [7, 3], [3, 5]])
