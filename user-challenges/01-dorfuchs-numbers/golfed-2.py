count=1
for i in range(10**4,10**5):
 l = map(int,sorted(str(i)))
 if any(map(lambda n:n[0]+1!=n[1],zip(l,l[1:]))):continue
 print("%i: %i"%(count,i))
 count+=1