def find_nth_term(n):
    a=0
    b=0
    for i in range(1,1+n):
        if i%2!=0:
            a+=2
        else:
            b+=1
    if n%2!=0:
        return a-2
    else:
        return b-1            
            

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    nth_term = find_nth_term(n)
    print(nth_term)