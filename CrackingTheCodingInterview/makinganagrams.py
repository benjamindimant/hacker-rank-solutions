def number_needed(a, b):
    count = 0
    for i in range(ord('a'), ord('z') + 1):
        ia = sum(letter == chr(i) for letter in a)
        ib = sum(letter == chr(i) for letter in b)
        count += abs(ia-ib)
    return count

a = input().strip()
b = input().strip()

print(number_needed(a, b))
