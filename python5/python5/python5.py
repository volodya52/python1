import cmath
a=int(input("Enter A"))
b=int(input("Enter B"))
c=int(input("Enter C"))
discriminant=b**2-4*a*c
if discriminant>0:
     root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
     root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
     print (root1,root2)
elif discriminant==0:
    root1 = -b / (2*a)
    print(root1)
elif discriminant<0:
    print("Discriminant < 0")
