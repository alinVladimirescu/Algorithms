def coin_change(coins , target):
    mini = float("inf")
    
    def bkt(i,sum, count):
        nonlocal mini
        if sum > target:
            return
        if sum == target:
            mini = min(mini, count)
            return
        if i >= len(coins):
            return
        
        bkt(i, sum + coins[i], count + 1)
        
        bkt(i + 1 , sum, count)
    
    bkt(0, 0, 0)
    return mini 
def coin_change2(coins, amount):
    dp = [ amount + 1 ] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
                
    return dp[amount + 1]

print(coin_change([1, 4, 6], 9))