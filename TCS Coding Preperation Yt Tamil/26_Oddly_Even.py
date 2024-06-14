def cal(s):
    sl=list(map(int,s))
    odd=0
    even=0
    slen=len(sl)
    for i in range(slen):
        if i%2==0:
            odd+=sl[i]
        else:
            even+=sl[i]
    return odd-even
print(cal('501324'))        
                