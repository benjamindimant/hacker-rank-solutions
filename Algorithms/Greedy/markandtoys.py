#!/bin/python3

import sys

def maximumToys(prices, k):
    num_toys = 0
    sum = 0
    while (sum < k and num_toys < len(prices) and sum + prices[num_toys] < k):
        sum += prices[num_toys]
        num_toys += 1
    return num_toys

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = sorted(list(map(int, input().strip().split(' '))))
    result = maximumToys(prices, k)
    print(result)
