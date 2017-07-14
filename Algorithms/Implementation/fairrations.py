def all_even(nums):
    if sum(nums) % 2 != 0:
        return "NO"
    for i in nums:
        if i % 2 != 0:
            return "NO"
    return count

N = int(input().strip())
B = [int(B_temp) for B_temp in input().strip().split(' ')]

count = 0
i = 0
while i < len(B) - 1:
    if B[i] % 2 != 0:
        B[i] += 1
        B[i + 1] += 1
        count += 2
    i += 1
print(all_even(B))
