#python class02 date 0224
#topic if elif else

price = 0
item = input("please take the order(A, B, C) :")
item = item.upper()
if item == "A":
    price = 100
    addfood = input("Do you want the coke ?(Y/N):")
    addfood = addfood.upper()
    if addfood == "Y":
        price += 20
elif item == "B":
    price = 90
elif item == "C":
    price = 70
    addprice = input("Do you want donate us ?(Y/N):")
    addprice = addprice.upper()
    if addprice == "Y":
        p = int(input("Enter the price :"))
        price += p
else:
    print("Error, retry this order please!")
print("You need to pay $", price)
