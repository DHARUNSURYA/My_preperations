def findunique(no):
    nostr=str(no)
    return len(nostr)==len(set(nostr))
def coundunique(lower,upper):
    count=0
    for i in range(lower,upper+1):
        if findunique(i):
            count+=1
    if count>0:
        print(count)
    else:
        print("NO UNIQUES NUMBERS")
if __name__=="__main__":
    lower=int(input("Enter the lower number : "))                     
    upper=int(input("Enter the upper number : "))
    coundunique(lower,upper)                     
    