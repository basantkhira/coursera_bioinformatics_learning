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


if __name__ == "__main__":
    coins = list(map(int,(input("Coins: ").strip().split(" "))))
    money = int(input("Money: ").strip())

    print(f"Coins available: {coins}")
    print(f"Amount to change: {money}")
    
    print(f"Minimum coins needed: {DPchange(money, coins)}")