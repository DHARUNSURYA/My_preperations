import keyword

def kf(s):
    k=keyword.kwlist
    if s in k:
        print(f"{s} is Keyword")
    else:
        print(f"{s} is Not Keyword")     

kf("While")        
print(keyword.kwlist)
