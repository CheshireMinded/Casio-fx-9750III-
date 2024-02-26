from math import*
a=float(input("a="))
b=float(input("b="))
N=int(input("N="))

dx=(b-a)/N

def y(x):
  return x**3+x**2-3

ar=a
al=a
am=a
at=a

total=0
ttal=0
ttl=0
tttl=0

while al<b:
  sm_lt=y(al)*dx
  total=sm_lt+total
  al=al+dx
print("left sum=",total)

while ar<b:
  ar=ar+dx
  smrt=y(ar)*dx
  ttal=smrt+ttal
print("right sum=",ttal)

am=am+dx/2

while am<b:
  smmpt=y(am)*dx
  ttl=smmpt+ttl
  am=am+dx
print("midpt sum=",ttl)

while at<b:
  trp=0.5*(y(at)+y(at+dx))*dx
  at=at+dx
  tttl=tttl+trp
print("trap sum=",tttl)

  