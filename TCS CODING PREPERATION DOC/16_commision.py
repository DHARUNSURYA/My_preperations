parent_member=input("Enter Your Name : ")
if_child=input("Enter If any Child Member (Y or N) : ").upper()
if if_child=='N':
    print("Total Member Is 1\n")
    print("Comission Details : 250 INR")
elif if_child=='Y':
    child=list(map(str,input("Enter Child Members Seperate By ',' : ").split(",")))
    print(f"Total Members is {len(child)+1}")
    print(f"Comission Details : {len(child)*500}")
    for i in child:
        print(f"Child Member : {i} have 250 INR")