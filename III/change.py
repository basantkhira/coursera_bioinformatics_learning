import math

# count of minimum coins
def DPchange(money,coins):
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
    count,used_coins = DPchange(money, coins)
    print(f"Minimum coins needed: {count},\n coins needed: {used_coins} ")

    