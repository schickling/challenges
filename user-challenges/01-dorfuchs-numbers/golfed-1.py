count=1
for i in range(10**4,10**5):
 l = map(int,sorted(str(i)))
 l = zip(l,l[1:])
 l = map(lambda n:n[0]+1!=n[1],l)
 if any(l):continue
 print("%i: %i"%(count,i))
 count+=1