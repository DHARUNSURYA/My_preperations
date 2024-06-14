def fill(sno,fno):
    width=len(str(fno))
    
    for i in range(sno,fno+1):
        print(str(i).zfill(width),end=" ")
fill(5,10)  
print()      
fill(9,100)        