from cs50 import get_float
from math import floor

change = 0

# Request change amount
while change < 1:
    change = get_float('Change: ') * 100

# List of coin denominations in descending value
coins = [25, 10, 5, 1]

coin_count = 0

# Iterate over coin list reducing the amount of coins according to how many already used
for coin in coins:
    coin_count += floor(change / coin)
    change = change % coin

print(coin_count)
