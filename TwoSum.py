a=[2,7,11,15];t=9
s=set()
for x in a:
    if t-x in s:print(True);break
    s.add(x)