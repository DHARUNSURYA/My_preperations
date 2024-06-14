r=3
r1=[]
r2=[]
r3=[]
avgs=[]
for i in range(1,r+1):
    print("Round Number: ",i)
    for j in range(r):
        s=int(input("Ente: "))
        if i==1:
            r1.append(s)
        elif i==2:
            r2.append(s)
        else:
            r3.append(s)
avg_t1=sum([r1[0],r2[0],r3[0]])/3
avg_t2=sum([r1[1]+r2[1]+r3[1]])/3
avg_t3=sum([r1[2]+r2[2]+r3[2]])/3
print(avg_t1)
d=[{'name':'1','avg':avg_t1},{'name':'2','avg':avg_t2},{'name':'3','avg':avg_t3}]

sort_d=sorted(d,key=lambda x: x['avg'],reverse=True)
print(f"Trainine Numberr : {sort_d[0]['name']}")
print(f"Trainine Numberr : {sort_d[1]['name']}")


