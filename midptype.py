print("1. given endpts")
print("2. given end an midpt")
r=int(input("choice "))

if r==1:
  a=float(input("x1="))
  b=float(input("x2="))
  c=float(input("y1="))
  d=float(input("y2="))

  midx=(a+b)/2
  midy=(c+d)/2

  print("mid X=",midx)
  print("mid Y=",midy)

else: 
  print("will find 2nd endpt")

  a=float(input("endpt x1="))
  b=float(input("endpt y1="))
  c=float(input("midpt x="))
  d=float(input("midpt y="))

  endx=(c-a)+c
  endy=(d-b)+d

  print("end x=",endx)
  print("end y=",endy)

    
