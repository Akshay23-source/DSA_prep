s1="on";s2="no"
print(sorted(s1)==sorted(s2))


s1="listen";s2="silent"
print(sorted(s1)==sorted(s2))

s1="hello";s2="world"
print(sorted(s1)==sorted(s2))


s1="rat"; s2="tar"
d={}
for c in s1: d[c]=d.get(c,0)+1
for c in s2: d[c]=d.get(c,0)-1
print(all(v==0 for v in d.values()))
