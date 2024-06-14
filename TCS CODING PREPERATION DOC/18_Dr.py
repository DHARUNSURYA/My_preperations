ages=[]
for i in range(20):
    m=input(f"Enter {i+1} Patient Age : ")
    if m==' ':
        break
    elif int(m) in range(1,121):
        ages.append(int(m))
    else:
        print("INVALID INPUT")
        exit()
fees=0
for i in ages:
    if i in range(1,17):
        fees+=200
    elif i in range(17,40):
        fees+=400
    else:
        fees+=300
print(f"Total Income {fees} INR")          