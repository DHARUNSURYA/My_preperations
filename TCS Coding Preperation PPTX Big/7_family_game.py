def findsparsal(n,s1):
    current_index=0
    members=list(range(1,n+1))
    song_lenght=len(s1)
    while len(members)>1:
        for lyric in s1:
            if len(members)==1:
                break
            if lyric=='y':
                members.pop(current_index)
                if current_index>=len(members):
                    current_index=0
            elif lyric=='x':
                current_index=(current_index+1)%len(members)
    return members[0]
if __name__=="__main__":
    n=int(input("Enter N Value : "))
    song=input("Enter lyrics of the song : ").strip()
    winner=findsparsal(n,song)
    print("The Winner Is : ",winner)  
                


























# def find_winner(N, song):
#     # Initialize the list of family members
#     members = list(range(1, N + 1))

#     # Initialize the index of the current member holding the parcel
#     current_member_index = 0

#     # Iterate through the lyrics of the song
#     for lyric in song:
#         # If 'y' is encountered, eliminate the current member
#         if lyric == 'y':
#             members.pop(current_member_index)
#             # If all members are eliminated, break the loop
#             if not members:
#                 break
#             # Update the index to the next member
#             current_member_index %= len(members)
#         # If 'x' is encountered, pass the parcel to the next member
#         elif lyric == 'x':
#             current_member_index = (current_member_index + 1) % len(members)

#     # The last remaining member is the winner
#     return members[0]

# # Main function
# if __name__ == "__main__":
#     N = int(input("Enter the number of family members: "))
#     song = input("Enter the lyrics of the song: ").strip()
#     winner = find_winner(N, song)
#     print("The winner is member:", winner)
