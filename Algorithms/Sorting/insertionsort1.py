n = int(input().strip())
arr = list(input().strip().split(' '))

e = arr[len(arr) - 1]
index = len(arr) - 2
while index >= 0 and e < arr[index]:
    arr[index + 1] = arr[index]
    index -= 1
    print(' '.join(arr))

arr[index + 1] = e
print(' '.join(arr))
