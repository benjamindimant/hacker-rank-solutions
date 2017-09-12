for _ in range(int(input().strip())):
    print(["First", "Second"][(int(input().strip()) % 7) in [0, 1]])
