import math


def DPchange(money,coins):
    min_num_coins = [math.inf] * (money + 1)
    min_num_coins[0] = 0

    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                if min_num_coins[m - coin] + 1 < min_num_coins[m]:
                    min_num_coins[m] = min_num_coins[m - coin] + 1
       # print(f"  dp[{m:2}] = {min_num_coins[m]}")
    return min_num_coins[money]


def dp_change_small(money, coins):
    max_coin = max(coins)

    min_num_coins = [math.inf] * max_coin
    min_num_coins[0] = 0

    for m in range(1, money + 1):
        idx = m % max_coin          # circular index
        min_num_coins[idx] = math.inf

        for coin in coins:
            if m >= coin:
                prev_idx = (m - coin) % max_coin
                if min_num_coins[prev_idx] + 1 < min_num_coins[idx]:
                    min_num_coins[idx] = min_num_coins[prev_idx] + 1

    return min_num_coins[money % max_coin]


def dp_change_with_coins(money, coins):
    min_num_coins = [math.inf] * (money + 1)
    used_coin     = [0] * (money + 1) 
    min_num_coins[0] = 0

    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                if min_num_coins[m - coin] + 1 < min_num_coins[m]:
                    min_num_coins[m] = min_num_coins[m - coin] + 1
                    used_coin[m]     = coin    

    result_coins = []
    m = money
    while m > 0:
        result_coins.append(used_coin[m])
        m -= used_coin[m]

    return min_num_coins[money], result_coins


if __name__ == "__main__":
    coins = list(map(int,(input("Coins: ").strip().split(" "))))
    money = int(input("Money: ").strip())

    print(f"Coins available: {coins}")
    print(f"Amount to change: {money}")
    
    print(f"Minimum coins needed: {DPchange(money, coins)}")