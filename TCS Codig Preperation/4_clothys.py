def we(w):
    if not isinstance(w,int) or w<0 or w>7000:
        return 'INVALID INPUT'
    if w==0:
        return "Time Estimate: 0 minutes"
    elif w>0 and w<=2000:
        return "Time Estimate: 25 minutes"
    elif w>=2001 and w<=4000:
        return "Time Estimate: 35 minutes"
    elif w>=4001 and w>=7000:
        return "Time Estimate: 45 minutes"
    else:
        return "OVERLOADED !!!"

wi=int(input("Enter Weigth Of Clothe: "))
print(we(wi))       
