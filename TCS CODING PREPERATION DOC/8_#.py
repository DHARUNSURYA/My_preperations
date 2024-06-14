s='####***' 
star=0
h=0
for i in s:
    if i == '*':
        star+=1
    elif i == '#':
        h+=1
print(star-h)
            