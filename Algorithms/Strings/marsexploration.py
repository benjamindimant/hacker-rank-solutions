import sys

def num_differences(string):
    count = 0
    compare_string = "SOS"
    for i in range(3):
        if compare_string[i] != string[i]:
            count += 1
    return count

S = input().strip()

print(sum(list(map(lambda x: num_differences(x), [S[i:i+3] for i in range(0, len(S), 3)]))))
