def are_anagrams(s1,s2):
    s1s=sorted(s1)
    s2s=sorted(s2)
    print(f'{s1s} s1s')
    print(f'{s2s} s2s')
    
    return s1s == s2s
s1="listen"
s2="silent"
if are_anagrams:
    print("YES")
else:
    print("No")    