def extractdigit(s1):
    numbers=[]
    current_no=''
    for i in s1:
        if i.isdigit():
            current_no+=i
        else:
            if current_no:
                numbers.append(int(current_no))
                current_no=''
    if current_no:
        numbers.append(int(current_no))
    return numbers
def findlargeno(numbers):
    valid_n0=[num for num in numbers if '9' not in str(num)]
    if valid_n0:
        return max(valid_n0)
    else:
        return -1
if __name__=="__main__":
    T=int(input("Enter no of text cases : "))
    for _ in range(T):
        string=input("Enter The String : ")
        numbers=extractdigit(string)
        largeno=findlargeno(numbers)
        print("Largest No. Of Without 9 Is : ",largeno)