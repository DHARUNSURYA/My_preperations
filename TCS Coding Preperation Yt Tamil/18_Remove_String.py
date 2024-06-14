def rem(s1,s2):
    set_s2=set(s2)
    result=[]
    for char in s1:
        if char not in set_s2:
            result.append(char)
    return ''.join(result)        
s1='computer'
s2='cat'
print(rem(s1,s2))