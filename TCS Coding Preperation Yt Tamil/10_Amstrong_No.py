def is_arm(n):
    ns = str(n)
    nl=len(ns)
    nlist=sum(int(digit)**nl for digit in ns)
    if nlist==n:
        return "Yes"
    else:
        return "No"
    
  
print(is_arm(153))  
    
    