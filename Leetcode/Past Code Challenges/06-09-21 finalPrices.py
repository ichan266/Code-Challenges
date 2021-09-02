# Leetcode # 1475
# Easy
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

# Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

# Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.

def finalPrices(prices):
    
    result = []
    
    for i in range(len(prices)-1):
        if min(prices[i+1:]) > prices[i]:
            result.append(prices[i])
        else:
            for discount in prices[i+1:]:
                if discount <= prices[i]:
                    result.append(prices[i] - discount)
                    break
    
    return result + [prices[-1]]

prices = [8,4,6,2,3]