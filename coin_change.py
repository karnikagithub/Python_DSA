def coin_change(coins,amount):

    dp = [amount + 1] * (amount + 1)
    print(dp,'dddddddddddddddd')
    dp[0] = 0

    for amt in range(1, amount + 1):
        # print(amt,'amrtttttttttt')
        for coin in coins:
            # print(amt,'amt',coin,'coin',amt - coin)
            if amt - coin >= 0:
                dp[amt] = min(dp[amt], 1 + dp[amt - coin])

        # print(dp)

    return dp[amount] if dp[amount] != amount + 1 else -1


#### O(amount * len(coins)) - TIME COMPLEXCITY
#### O(amount) SPACE COMPLEXCITY


print(coin_change([1,3,4,5],7))


def coin(coins,amount):

    dp = [amount + 1] * (amount + 1)
    dp[0] = 0


    for amt in range(1, amount+1):
        for coin in coins:

            if amt - coin >= 0:
                dp[amt] = min(dp[amt], 1 + dp[amt - coin])


    return dp[amount] if dp[amount] != amount + 1 else -1


print(coin([1,3,4,5],10))