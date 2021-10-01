# Hackbright AlumNight 9/29/21
# DroneDeploy
# Write a coin machine in a language of your choice. Given 87 cents, return the minimum number of coins. The program should be able to handle different values for coins, as well as different numbers of coins

def min_num_of_coin(cash, coins):

    # divmod operations:
    # given cash, find the highest value of coin, then do divmod operation:
    #  if div >= 1, keep track of that value.
    #  if div == 0 and mod != 0, go to the next highest coin value
    #  if div and mod of cash are zeros, I return result

    coins = sorted(coins, reverse=True)
    result_dict = {}  # key is coin value; value is amount of coins

    for coin in coins:
        div, cash = divmod(cash, coin)  # 25 cents : div = 3, mod = 12
        result_dict[coin] = div

    for coin in result_dict:
        print(f"coin: {coin}, number of coins: {result_dict[coin]}")


min_num_of_coin(87, [25, 10, 5, 1])
