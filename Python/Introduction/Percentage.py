a = input()
d = {}
for i in range(0,a):
    j = raw_input().split()
    d[j[0]] = format(sum(map(float,j[1:]))/len(j[1:]),'.2f')
print d[raw_input()]