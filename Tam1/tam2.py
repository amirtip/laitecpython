sabti="iran"
sabti2="Iran"
loc=input("Enter the Location:")
if loc==sabti or loc==sabti2:
        x=float(input("Nomre:"))
        if x>=0 and x<=20:
            print(f"{x} Is nomre Irani")
            if x>=18 and x<=20:
                print(f"{x} Is A")
            elif x>=16 and x<18:
                print(f"{x} Is B")
            elif x>=14 and x<16:
                print(f"{x} Is C")
            elif x>=12 and x<14:
                print(f"{x} Is D")
            elif x>=10 and x<12:
                print(f"{x} Is E")
            elif x>=0 and x<10:
                print(f"{x} Is F")
        else:
            print("Error")
else:
    print("You Are Not Irani!!")
sabti="france"
sabti2="France"
if loc==sabti or loc==sabti2:
    i=(input("Nomre:"))
    if i=="A":
        print("Your Nomre 18 ta 20")
    elif i=="B":
        print("Your Nomre 16 ya 17")
    elif i=="C":
        print("Your Nomre 14 ya 15")
    elif i=="D":
        print("Your Nomre 12 ya 13")
    elif i=="E":
        print("Your Nomre 10 ya 11")
    elif i=="F":
        print("Your Nomre 0 ta 9")
else:
            print("Error")
        


