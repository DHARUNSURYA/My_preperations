def vr(s):
    result=[]
    v=set('aeiou')
    for char in s:
        if char.lower() not in v:
            result.append(char)
    return ''.join(result)

s1="Welcome to geekforgeeks"
s2="what is your name ?"
print(vr(s1))        
print(vr(s2))        
            