x=int(input("EnterThe Num:"))
a=bin(x)
b=format(x,'b')
print(a,"\n",b)
s=[]
while x:
    if x==0:
        print(f"Your Number Is{x}")
    else:
        s=x%2
        a=x//2
    while a>=2:
        a//2
