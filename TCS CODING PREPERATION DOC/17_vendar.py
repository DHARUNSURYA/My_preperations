menu = [['Espresso Coffee','Cappuucino Coffee','Latte Coffee'], ['Plain Tea',

'Assam Tea','Ginger Tea','Cardamom Tea','Masala Tea','Lemon Tea','Green Tea',

'Organic Darjeeling Tea'], ['Hot and Sour Soup','Veg Corn Soup','Tomato Soup',

'Spicy Tomato Soup'], ['Hot Chocolate Drink', 'Badam Drink',

'Badam-Pista Drink']]
m=input("Enter : ")
ms=['t','c','s','b']
if m in ms:
    if m=='c':
        submenu=int(input("Enter sub menu : "))
        if submenu in range(1,4):
            print("Welcome To CCD!!!!\n")
            print(f"Enjoy Your {menu[0][submenu-1]}")
        else:
            print("INVALID INPUT")
        
    if m=='t':
        
        submenu=int(input("Enter sub menu : "))
        if submenu in range(1,9):
            print("Welcome To CCD!!!!\n")
            print(f"Enjoy Your {menu[1][submenu-1]}")
        else:
            print("INVALID INPUT")
    if m=='s':
        
        submenu=int(input("Enter sub menu : "))
        if submenu in range(1,5):
            print("Welcome To CCD!!!!\n")
            print(f"Enjoy Your {menu[2][submenu-1]}")
        else:
            print("INVALID INPUT") 
            
    if m=='b':
        
        submenu=int(input("Enter sub menu : "))
        if submenu in range(1,4):
            print("Welcome To CCD!!!!\n")
            print(f"Enjoy Your {menu[3][submenu-1]}")
        else:
            print("INVALID INPUT") 
else:
    print("Invalid Input")            
            
            
            
                   