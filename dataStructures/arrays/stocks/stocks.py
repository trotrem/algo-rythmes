#!/usr/bin/env python

#Say you have an array for which the ith element is the price of a given stock on day i.

#Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

#Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

def maxProfit2(self, prices):
    if not prices:
        return 0
    sell_day = None
    buy_day = None
    profit = 0

    for i in reversed(range(len(prices))):
        if buy_day != None and prices[i] >= buy_day:
            profit += sell_day - buy_day
            sell_day = prices[i]
            buy_day = None
        elif sell_day != None and prices[i] < sell_day:
            buy_day = prices[i]
        else:
            sell_day = prices[i]
    if buy_day != None:
        profit += sell_day - buy_day
    return profit

def maxProfit3(self, prices):
    profit = 0
    for i in range(len(prices)):
        if i + 1 < len(prices) and prices[i + 1] > prices[i]:
            profit += prices[i + 1] - prices[i]
    return profit

def maxProfit(self, prices):
    return sum(prices[i + 1] - prices[i] for i in range(len(prices) - 1) if prices[i + 1] > prices[i])
