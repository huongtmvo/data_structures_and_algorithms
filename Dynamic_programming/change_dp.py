# Uses python3
import sys
import math

def get_change(money):
    denominations = [1,3,4]
    min_coins = [0] + [math.inf] * money

    for m in range(1,money+1):
        for c in denominations:
            if m >= c:
                coins = min_coins[m-c] + 1
                if coins < min_coins[m]:
                    min_coins[m] = coins
    return min_coins[money]

if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))

