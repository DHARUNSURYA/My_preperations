def findc(s1,s2):
    if len(s1) != len(s2):
        return False
    
    s1d={}
    s2d={}
    
    for char1 in s1:
        if char1 in s1d:
            s1d[char1]+=1
        else:
            s1d[char1]=1
    print(s1d)
    for char2 in s2:
        if char2 in s2d:
            s2d[char2]+=1
        else:
            s2d[char2]=1
    print(s2d)
    return s1d == s2d

print(findc('cbb','bbb'))                        