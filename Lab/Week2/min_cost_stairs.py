cost = [1,100, 1, 1, 1, 100, 1, 1, 100, 1]
n = len(cost)

def calculate_cost(n):
    dp = []
    dp.append(cost[0])
    dp.append(cost[1] + dp[0])
    print(dp)
    for i in range(2,n):
        dp.append(min(cost[i] + dp[i - 1], cost[i] + dp[i - 2]))
    print(dp)
    return dp[n - 1]
print(calculate_cost(n))