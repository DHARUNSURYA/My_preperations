def findunique(n):
    strn=str(n)
    return len(strn)==len(set(strn))
def count_unique(lower,upper):
    count=0
    for i in range(lower,upper+1):
        if findunique(i):
            count+=1
    if count>0:
        print("No Of Unique Pairs is : ",count)
    else:
        print("No Unique")     
count_unique(10,22)                