a=[-2,1,-3,4,-1,3,2,6]
s=m=a[0]
for x in a[1:]:
    s=max(x,s+x);m=max(m,s)
    print(m)