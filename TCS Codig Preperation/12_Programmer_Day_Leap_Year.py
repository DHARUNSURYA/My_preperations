def julian(year):
    return year % 4==0
def gregorian(year):
    return year%400==0 or(year%4==0 and year %100!=0)

def findprogramday(year):
    if year<1918:
        if julian(year):
            program_day=12
        else:
            program_day=13
    elif year>1918:
        if gregorian(year):
            program_day=12            
        else:
            program_day=13
    else:
        program_day=26
    
    return "{:02d}.09.{}".format(program_day,year) 

year=int(input("Enter Year: "))
print(findprogramday(year))           
                