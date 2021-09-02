def zarb(n,m):
    total=0
    for i in range(n):
        total+=m
        print(f"is {total}")
def tavan(n,m):
    s=0
    s=n**m
    print(f"is {s}")
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print(f"{n }is {fact}")



if __name__=='__main__':
##    m=int(input("Adad:"))
##    n=int(input("Adad:"))
##    tavan(m,n)
    
    n=int(input("Adad:"))
    factorial(n)
