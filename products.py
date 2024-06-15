import datetime
import smtplib
import re
now=datetime.datetime.now()

def email(total,mail):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls
        s.login("niveditha240203@gmail.com","ksdq fjuf pzbv nmkx")
        message=f"the total amount is {total} and the payment is received successfully."
        s.sendmail("niveditha240203@gmail",mail,message)
        s.quit
        print("mail sent successfully")
    

def payment(price):
    how_many = int(input("How many Piece do you want: "))
    GST = (price*5)/100
    net_price = price + GST
    total = how_many * price + net_price
    with open("bill.txt", "w") as f:
            f.write(f"The total bill is {total} at {now.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"The total price is {total}")
            print("Bill generated successfully")
            mail=input("enter your email id: ")
            email(total,mail)


def kids():
    try:
        print("enter 1 for shirt")
        print("enter 2 for pant")
        print("enter 3 for gowns")

        choice = int(input("enter the choice you want: "))
        if choice == 1:
            brand=int(input("which type you want 1.half sleeve 2.full sleeve 3.sleeveless"))
            if brand==1:
                price =500
                print("choose the colour of the shirt you like and proceed to billing")
                payment(price)
            elif brand==2:
                price =550
                print("choose the colour of the shirt you like and proceed to billing")
                payment(price)
            elif brand==3:
                price =450
                print("choose the colour of the shirt you like and proceed to billing")
                payment(price)
            else:
                print("enter valid choice")
        elif choice == 2:
            brand=int(input("which type you want 1.full pant 2.trowsers"))
            if brand==1:
                price =700
                print("choose the colour of the pant you like and proceed to billing")
                payment(price)
            elif brand==2:
                price =650
                print("choose the colour of the trowser you like and proceed to billing")
                payment(price)
            else:
                print("enter valid choice")
        elif choice == 3:
            brand=int(input("which type you want 1.full gown 2.knee length gown"))
            if brand==1:
                price =500
                print("choose the colour of the gown you like and proceed to billing")
                payment(price)
            elif brand==2:
                price =550
                print("choose the colour of the gown you like and proceed to billing")
                payment(price)
            
            else:
                print("enter valid choice")
        else:
            print("not available")
        
    except ValueError:
        print("Please enter a valid number")

def women():
    try:
        print("1.saree")
        print("2.kurti")
        print("3.jewellery&makeup")
        choice = int(input("enter the choice you want: "))
        if choice == "saree":
            brand=int(input("which type you want 1.silk 2.cotton:"))
            if brand==1:
                price =1000
                print("choose the colour of the saree you like and proceed to billing")
                payment(price)
            elif brand==2:
                price =550
                print("choose the colour of the shirt you like and proceed to billing")
                payment(price)
            else:
                print("enter valid choice")
        elif choice == "kurti":
            brand=int(input("which type you want 1.floral 2.plain"))
            if brand==1:
                price =800
                print("choose the colour of the pant you like and proceed to billing")
                payment(price)
            elif brand==2:
                price =550
                print("choose the colour of the trowser you like and proceed to billing")
                payment(price)
            else:
                print("enter valid choice")
        elif choice == "jewellery&makeup":
            brand=int(input("which type you want 1.necklace 2.earring 3.lipstick 4.kajal"))
            if brand==1:
                price =400
                print("choose the type of the necklace you like and proceed to billing")
                payment(price)
            elif brand==2:
                price =50
                print("choose the set of the earring you like and proceed to billing")
                payment(price)
            elif brand==3:
                price =350
                print("choose the colour of the lipstick you like and proceed to billing")
                payment(price)
            elif brand==4:
                price =250
                print("choose the brand of the kajal you like and proceed to billing")
                payment(price)
            else:
                print("enter valid choice")
        else:
            print("not available")
        
    except ValueError:
        print("Please enter a valid number")
def man():
    try:
        print("enter 1 for shirt")
        print("enter 2 for pant")

        choice = int(input("enter the choice you want: "))
        if choice == 1:
            brand=int(input("which type you want 1.half sleeve 2.full sleeve 3.sleeveless"))
            if brand==1:
                price =500
                print("choose the colour of the shirt you like and proceed to billing")
                payment(price)
            elif brand==2:
                price =550
                print("choose the colour of the shirt you like and proceed to billing")
                payment(price)
            else:
                print("enter valid choice")
        elif choice == 2:
            brand=int(input("which type you want 1.full pant 2.trowsers"))
            if brand==1:
                price =700
                print("choose the colour of the pant you like and proceed to billing")
                payment()
            elif brand==2:
                price =650
                print("choose the colour of the trowser you like and proceed to billing")
                payment()
            else:
                print("enter valid choice")
        else:
            print("not available")
        
    except ValueError:
        print("Please enter a valid number")

def beverage():
    try:
        print("enter 1 for milkshakes")
        print("enter 2 for softdrinks")

        choice = int(input("enter the choice you want: "))
        if choice == 1:
            brand=int(input("which flavor you want 1.chocolate 2.strawberry"))
            if brand==1:
                price =50
                payment(price)
            elif brand==2:
                price =40
                payment(price)
            else:
                print("enter valid choice")
        elif choice == 2:
            brand=int(input("which type you want 1.coke 2.pepsi"))
            if brand==1:
                price =40
                payment(price)
            elif brand==2:
                price =50
                payment(price)
            else:
                print("enter valid choice")
        else:
            print("not available")
        
    except ValueError:
        print("Please enter a valid number")

    
