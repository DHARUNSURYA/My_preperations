n=int(input("Enter Number Of Mondeys: "))
k=int(input("Enter Number Of Banana For Each MonKey: "))
j=int(input("Enter Number Of Peanuts For Single Monkey: "))
m=int(input("Enter Total Number Of Banana: "))
p=int(input("Enter Total Number Of Peanuts: "))

no_of_banana_eated_by_monkeys=m/k
no_of_peanuts_eated_by_monkeys=p/j
eated_monkeys=no_of_banana_eated_by_monkeys+no_of_peanuts_eated_by_monkeys
print("Left of Monkeys in Tree: ",n-eated_monkeys)


# There are total n number of Monkeys sitting on the branches of a huge Tree. As travelers offer Bananas and Peanuts, the Monkeys jump down the Tree. If every Monkey can eat k Bananas and j Peanuts. If total m number of Bananas and p number of Peanuts are offered by travelers, calculate how many Monkeys remain on the Tree after some of them jumped down to eat.
# At a time one Monkeys gets down and finishes eating and go to the other side of the road. The Monkey who climbed down does not climb up again after eating until the other Monkeys finish eating.
# Monkey can either eat k Bananas or j Peanuts. If for last Monkey there are less than k Bananas left on the ground or less than j Peanuts left on the ground, only that Monkey can eat Bananas(<k) along with the Peanuts(<j).
# Write code to take inputs as n, m, p, k, j and return  the number of Monkeys left on the Tree.
# Where, 
# 	n= Total no of Monkeys
#         k= Number of eatable Bananas by Single Monkey (Monkey that jumped down last may get less than k Bananas)
#         j = Number of eatable Peanuts by single Monkey(Monkey that jumped down last may get less than j Peanuts)
#         m = Total number of Bananas
#         p  = Total number of Peanuts
# Remember that the Monkeys always eat Bananas and Peanuts, so there is no possibility of k and j having a value zero.


# Example 1:
# Input Values    
# 20
# 2
# 3
# 12
# 12
# Output Values
# Number of  Monkeys left on the tree:10
# Note: Kindly follow  the order of inputs as n,k,j,m,p as given in the above example. And output must include  the same format  as in above example(Number of Monkeys left on the Tree:)
