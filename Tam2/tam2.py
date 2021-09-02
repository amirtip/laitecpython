x=int(input("Enter The Num:"))
for i in range(1,x+1):
    print(" "*(x-i),end='')    
    print(" * "*i," ")
for i in range(x,0):
    print(" "*(x-i),end='')    
    print(" *"*i)
