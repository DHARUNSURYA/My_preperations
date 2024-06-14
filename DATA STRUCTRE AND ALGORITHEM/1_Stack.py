stack=[]
def puch():
    if len(stack)==n:
        print("Stack is Full")
    else:
        a=input("Enter The Element")
        stack.append(a)
        print(f"{a} is success fully Append")
def pop():
    if not stack:
        print("Stack is Empty")
    else:
        e=stack.pop()
        print(f"{e} is success fully Pop")
def show():
    if not stack:     
        print("Stack is Empty")
    else:
        print(stack) 
n=int(input("Enter The Size Of Stack : "))
while True:
    print("1 : Puch, 2 : Pop, 3 : Show, 4 : Exit ")
    ch=int(input("Enter Menu : "))
    if ch==1:
        puch()
    elif ch==2:
        pop()
    elif ch==3:
        show()
    elif ch==4:
        print(stack)
        break
    else:
        print("Enter Correct Menu Number")                     
              
        
                    
        