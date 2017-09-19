def maxXor(l, r):
    return max([x ^ y for x in range(l, r + 1) for y in range(l, r + 1)])

if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(maxXor(l, r))
