a = input()
b = map(int,raw_input().split()[:a])
for i in range(b.count(max(b))):
    b.pop(b.index(max(b)))
print max(b)