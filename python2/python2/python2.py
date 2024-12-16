print ("Calculator")
print ("Press 1 for +")
print ("Press 2 for -")
print ("Press 3 for *")
print ("Press 4 for /")
a=int(input("Choose operation"))
if a==1:
    b=int(input("Write the first number"))
    c=int(input("Write the second number"))
    d=b+c
    print(d)
elif a==2:
     b=int(input("Write the first number"))
     c=int(input("Write the second number"))
     d=b-c
     print(d)
elif a==3:
     b=int(input("Write the first number"))
     c=int(input("Write the second number"))
     d=b*c
     print(d)
elif a==4:
     b=int(input("Write the first number"))
     c=int(input("Write the second number"))
     d=b/c
     print(d)