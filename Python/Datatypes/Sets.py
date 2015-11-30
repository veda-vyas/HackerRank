a = input()
b = map(int,raw_input().split())[:a]
c = input()
d = map(int,raw_input().split())[:c]
for i in sorted(list(set(b)^set(d))):
    print i