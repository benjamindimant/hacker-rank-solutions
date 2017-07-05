s = input().strip().lower()

alphabet = set("abcdefghijklmnopqrstuvwxyz")

if set(s).issuperset(alphabet):
    print("pangram")
else:
    print("not pangram")
