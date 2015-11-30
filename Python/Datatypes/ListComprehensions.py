x,y,z,n = input(),input(),input(),input()
l = []
for a in range(0,x+1): 
    for b in range(0,y+1): 
        for c in range(0,z+1):
            if a + b + c != n:
                l.append([a,b,c])
print l