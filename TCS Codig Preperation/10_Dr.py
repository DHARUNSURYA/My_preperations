# Python3 program for the above approach 
  
# Function that returns number of 
# patient for a day in a month 
def getPatients( M,  D): 
  
    return ((6 - M) * (6 - M)) + abs(D - 15); 
  
# Function that count the TVs with 
# given amount of revenue target 
def countTVs(  n,   r1,  r2,   target): 
  
  
    # Days in each month 
    days = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]; 
  
    # Check all possible combinations 
    for tvs in range(n + 1): 
  
        # Stores the current target 
        current_target = 0; 
  
        for m in range(1, 13): 
              
            for d in range(1, 1 + days[m]): 
  
                # Number of patients 
                # on day d of month m 
                np = getPatients(m, d); 
  
                # Patients cannot be 
                # exceed number of rooms 
                np = min(np, n); 
  
                # If the number of patient is 
                # <= count of rooms without tv 
                if (np <= n - tvs) : 
  
                    # All patients will opt 
                    # for rooms without tv 
                    current_target += np * r2; 
                  
  
                # Otherwise 
                else : 
  
                    # Some will opt for 
                    # rooms with tv and 
                    # others without tv 
                    current_target += ((n - tvs) * r2 + ((np - (n - tvs)) * r1)); 
                  
              
          
  
        # If current target meets 
        # the required target 
        if (current_target >= target): 
            break; 
          
      
  
    # Pr the count of TVs 
    print(min(tvs, n)); 
  
  
# Driver Code 
N = 10
R1 = 1000; 
R2 = 1500; 
target = 10000000; 
  
# Function Call 
countTVs(N, R1, R2, target);