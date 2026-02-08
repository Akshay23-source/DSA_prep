a=[6,8,5,11,6];t=10
s=set()
for x in a :
    if t-x in s:print(True);break
    else: 
        print(False);break
    
    
    
    
    a=[3,2,4]; t=6
d={}
for i,x in enumerate(a):
    if t-x in d: print(d[t-x],i)
    d[x]=i
