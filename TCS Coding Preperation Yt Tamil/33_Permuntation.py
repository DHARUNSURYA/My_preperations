def count_permutations(s):
    # Initialize an empty set to track used characters
    used = set()
    # Initialize a list to store all permutations
    permutations = []
    
    # Define the recursive function to generate permutations
    def generate(current):
        # Base case: If the length of current permutation equals length of s
        if len(current) == len(s):
            permutations.append(''.join(current))  # Convert list to string and add to permutations list
            return
        
        # Iterate through each character in s
        for i in range(len(s)):
            if i not in used:
                # Add character at index i to current permutation
                current.append(s[i])
                used.add(i)
                # Recursively generate permutations
                generate(current)
                # Backtrack: Remove added character and mark it as unused
                current.pop()
                used.remove(i)
    
    # Start generating permutations from an empty list
    generate([])
    
    # Return the number of permutations and the list of permutations
    return len(permutations), permutations

# Example usage:
s = "aab"
count, perm_list = count_permutations(s)

print(f"Number of permutations of '{s}': {count}")
print("Permutations:", perm_list)
