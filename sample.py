import re
import products

f=open("groceries.txt","r")
groceries_text=f.read()

while True:
    your_choice = input("Enter your choice: ")
    x = re.search(your_choice, groceries_text)

    if x:
        print("Yes, the product is available")

        if your_choice == "kids":
            products.kids()
        elif your_choice == "women":
            products.women()
        elif your_choice == "man":
            products.man()
        elif your_choice == "beverage":
            products.beverage()
        else:
            print("Option available but not yet implemented")
        
        var = input("Do you wish to continue (yes/no): ").lower()
        if var == "no":     
            print("Thank you for shopping")
            break
    else:
        print("Product not found in the groceries list")

 

