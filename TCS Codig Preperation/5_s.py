s=input("Enter: ")
h=0
s=0
for char in s:
    if char =='#':
        h+=1
    elif char =='*':
        s+=1
if h>s:
    print("-ve -> number of # > *")
elif s>h:
    print("+ve -> number of * > #")
else:
    print("0 -> number of * and # are equal")
