no_of_interior_walls=int(input("Enter Number Of Interior walls: "))
no_of_exterior_walls=int(input("Enter Number Of Exterior walls: "))
full_in=[]
for i in range(1,no_of_interior_walls+1):
    n=float(input(f"Enter sq.ft. of {i} Interior wall: "))
    mul_in=n*18
    full_in.append(mul_in)

for j in range(1,no_of_exterior_walls+1):
    n=float(input(f"Enter sq.ft. of {j} Exterior wall: "))
    mul_ex=n*12
    full_in.append(mul_ex)

print(f"Total Estimated Cose : {round(sum(full_in),2)} INR")    
      
# We want to estimate the cost of painting a property. Interior wall painting cost is Rs.18 per sq.ft. and exterior wall painting cost is Rs.12 per sq.ft.

# Take input as
# 1. Number of Interior walls  6
# 2. Number of Exterior walls 3
# 3. Surface Area of each Interior  
# 4. Wall in units of square feet
# Surface Area of each Exterior Wall in units of square feet

# If a user enters zero  as the number of walls then skip Surface area values as User may don’t  want to paint that wall. Calculate and display the total cost of painting the property.
