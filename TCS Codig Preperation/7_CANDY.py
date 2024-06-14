n=10
k=5
c_candy=n
def disp(sold,ava):
    print(f"No of Candies Sold : {sold}")
    print(f"No of Candies Available : {ava}")

while True:
    print(f"No of Candies Available in Jar {c_candy}")
    try:
        c_o=int(input("Enter No of Candies Coustomer Order : "))

        if c_o<=0 or c_o>c_candy:
            print("INVALID INPUT")
        else:
            c_candy-=c_o
            disp(c_o,c_candy)
            print("The jar is refilled to full capacity.")
    except ValueError:
         print("INVALID INPUT ENTER CORRECT INPUT")


# There is a JAR full of candies for sale at a mall counter. JAR has the capacity N, that is JAR can contain maximum N candies when JAR is full. At any point of time. JAR can have M number of Candies where M<=N. Candies are served to the customers. JAR is never remain empty as when last k candies are left. JAR if refilled with new candies in such a way that JAR get full.
# Write a code to implement above scenario. Display JAR at counter with available number of candies. Input should be the number of candies one customer can order at point of time. Update the JAR after each purchase and display JAR at Counter.
# Output should give number of Candies sold and updated number of Candies in JAR.
# If Input is more than candies in JAR, return: “INVALID INPUT”
# Given, 
# N=10, where N is NUMBER OF CANDIES AVAILABLE
# K =< 5, where k is number of minimum candies that must be inside JAR ever.
# Example 1:(N = 10, k =< 5)
# Input Value
# 3
# Output Value
# NUMBER OF CANDIES SOLD : 3
# NUMBER OF CANDIES AVAILABLE : 7


# Example : (N=10, k<=5)
# Input Value
# 0
# Output Value
# INVALID INPUT
# NUMBER OF CANDIES LEFT : 10
