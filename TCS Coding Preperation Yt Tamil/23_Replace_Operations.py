# A=and
# B=or
# C=xor

def evalbool(exp):
    mapping={'A':'&','B':'|','C':'^'}
    for char,op in mapping.items():
        exp=exp.replace(char,op)
    result=eval(exp)
    return result
expression1 = "1C0C1C1A0B1"
print(evalbool(expression1))  # Output: 1 (True)    