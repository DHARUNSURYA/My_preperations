in_wall=int(input("Enter No. Of Interior Walls: "))
ex_wall=int(input("Enter No. Of Exterior Walls: "))
if in_wall <0 or ex_wall<0:
    print("Invalid Input")
    exit()
if in_wall:
    inwall=[]
    for i in range(in_wall):
        inwall.append(float(input(f"Enter {i+1} No. Wall : ")))    
        
if ex_wall:
    exwall=[]
    for i in range(ex_wall):
        exwall.append(float(input(f"Enter {i+1} No. Wall : ")))
        
if ex_wall and in_wall:
    print("Total Extimate Cost is : ",sum(inwall)*18+(sum(exwall)*12),"INR")                    
else:
    if ex_wall:
        print("Total Extimate Cose is : ",sum(exwall)*12,"INR")    
    elif in_wall:
        print("Total Extimate Cost is : ",sum(inwall)*18,"INR")
    else:
        print("Total Estimate Cost is : 0.0 INR")    