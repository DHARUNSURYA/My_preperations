total_no_candy=10
no_of_candy=int(input("Enter: "))
if no_of_candy in range(1,6):
    print("No. Of Candies Sold: ",no_of_candy)
    print("Total No. Of Candies Available: ",total_no_candy-no_of_candy)
    print(total_no_candy)
else:
    print('INVALID INPUT')
    print("Total No. Of Candies Available: ",total_no_candy-no_of_candy)
