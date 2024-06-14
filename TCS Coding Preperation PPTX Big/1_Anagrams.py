def angrams(s1,s2):
    if len(s1)!=len(s2):
        return False
    sorted_s1=sorted(s1)
    print(f's1 {sorted_s1}')
    sorted_s2=sorted(s2)
    print(f's2 {sorted_s2}')
    print(sorted_s1==sorted_s2)
    return sorted_s1==sorted_s2
s1=input("Enter string 1 : ")
s2=input("Enter String 2 : ")
if angrams(s1,s2):
    print("A given string are anagrams. ")
else:
    print("A given string are not anagrams. ")    