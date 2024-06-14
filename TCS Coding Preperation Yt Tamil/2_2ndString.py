def secfreq(arr,n):
    freq = {}
    for string in arr:
        if string in freq:
            freq[string] += 1
        else:
            freq[string]=1
    print(freq)        
    sorted_freq=sorted(freq.items(),key=lambda item: item[1],reverse=True)      
    print(sorted_freq)   
    if len(sorted_freq)<2:
        return ''
    else:
        return sorted_freq[1][0]
input_1 = ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
input_2 = ["geek", "for", "geek", "for", "geek", "aaa"]

print(secfreq(input_1, len(input_1)))  # Output: bbb
print(secfreq(input_2, len(input_2)))  # Output: for    