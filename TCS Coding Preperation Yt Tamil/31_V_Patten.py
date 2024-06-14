def generate(n):
    for i in range(1,n+1):
        
        digit_Str=str(i)*i
        if i==n:
            row=digit_Str*2
        else:
            middle_space=' '*(2*(n-i))
            row=digit_Str+middle_space+digit_Str
        print(row)
generate(4)            