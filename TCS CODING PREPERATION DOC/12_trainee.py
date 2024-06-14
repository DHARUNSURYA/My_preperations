trainee=[[],[],[],[]]
for i in range(3):
    for j in range(3):
        trainee[i].append(int(input('Enter: ')))
        if (trainee[i][-1]) not in range(1,101):
            print('INVALID INPUT')
for i in range(3):
    trainee[3].append(trainee[2][i]+trainee[1][i]+trainee[0][i])
maxval=max(trainee[3])
for i in range(3):
    if trainee[3][i] <70:
        print(f"Trainee {i+1} Is Unfit")
    elif maxval==trainee[3][i]:
        print("Trainee Number is: ",i+1)
                            