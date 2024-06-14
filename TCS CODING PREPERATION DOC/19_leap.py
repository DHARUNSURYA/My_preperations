def leap(y):
    return y%400==0 or (y%4==0 and y%100!=0)
y=int(input("Enter Year : "))
if leap(y):
    print(f'{y} Id Leap Year')
else:
    print(f'{y} Is Not Leap Year')    