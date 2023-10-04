n= int(input("enter odd number greater than 1 : "))
if n==1 or n%2==0:
    print("you have entered even or 1 : ")
else:
    #upar triangle
    for i in range(n//2+1):
        for j in range(n+2):
            print(" ",end="")
        for k in range(n//2-i):
            print(" ",end="")
        for l in range(2*i+1):
            print("e",end="")
        print()
    for i in range(n+2-n//2-1):
        for j in range(0,n//2+n+3):
            if j==n//2+n+2:
                print("*",end="")
            else:
                print(" ",end="")
        
        print()
    #lower
    for i in range(n//2+1):
        for j in range(n//2+1):
            if j>i:
                print(" ",end="")
            else:
                print("e",end="")
        
        for k in range(n+2):
            if i==n//2 or k==n+1:
                print("*",end="")
            else:
                print(" ",end="")
        
        print()
    #lowest
    for i in range(n//2):
        for j in range(n//2-i):
            print("e",end="")
        print()