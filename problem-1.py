'''
Question 1:

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve
any profit, return 0.
''''


def max_profit_calc(prices):
    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        diff = prices[i] - min_price

        if diff > max_profit:
            max_profit = diff
        if prices[i] < min_price:
            min_price = prices[i]

    return max_profit


if __name__ == "__main__":
    # prices = [7, 6, 4, 3, 1]
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit_calc(prices))
	
