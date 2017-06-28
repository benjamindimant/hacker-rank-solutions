n = int(input())
a = input().strip().split(' ')

def most_common(lst):
    return max(set(lst), key = lst.count)

print(len(list(filter(lambda x: x != most_common(a), a))))
