from math import*
print("find GCD,LCM")

a=int(input("Smaller value a="))
b=int(input("Larger value b="))  
for i in range (1,b,1): 
  c=a%i
  d=b%i

  if c==0 and d==0:
    e=i
    f=int(abs(a*b/e))

   
print("GCD=",e)
print("LCM=",f)
   
