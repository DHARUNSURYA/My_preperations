import math

def getfer(start,end):
    start=start.upper()
    end=end.upper()
    
    BusStop=['TH','GA','IC','HA','TE','LU','NI','CA']
    distance=[800,600,750,900,1400,1200,1100,1500]
    
    if not(start in BusStop and end in BusStop):
        print("INVALID INPUT")
        exit()
    index_start=BusStop.index(start)
    index_end=BusStop.index(end)
    
    if index_start <= index_end:
        totdistanc=sum(distance[index_start:index_end])
    else:
        totdistanc=sum(distance[index_start:]) + sum(distance[:index_end])
    
    fare = math.ceil(totdistanc/1000)*5
    
    return f"{fare}.0 INR"    
print(getfer("ca", "Ca"))  # Expected output: INVALID OUTPUT
print(getfer("NI", "HA"))  # Expected output: 23.0 INR
        
        