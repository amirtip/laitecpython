x=int(input("Zavieh:"))
y=int(input("Zavieh:"))
z=int(input("Zavieh:"))
if x+y+z==180:
    print("Mosalas Ast")
    if x==90 or y==90 or z==90:
        print("Mosalas Ghaem Ast")
    elif x==y==z==60:
        print("Mosalas motesaviazla")
    elif x==y or x==z or y==z:
        print("Mosalas motesaviSagh")
else:
     print("Mosalas nis")
