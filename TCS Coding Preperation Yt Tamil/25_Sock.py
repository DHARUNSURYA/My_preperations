def socks(n,arr):
    pair=0
    sock_counts={}
    
    for color in arr:
        if color in sock_counts:
            sock_counts[color] += 1
        else:
            sock_counts[color]=1
    for count in sock_counts.values():
        pair+=count//2
    return pair
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(socks(n, ar))  # Output: 3               