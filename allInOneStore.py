"""

There is an All-in-One Store that sells everything from groceries, medicines, clothes, books, music CDs, imported commodities etc.
Standard tax rates apply on these commodities as below. 

-    5% on medicines and Food
-    5% on clothes below 1000 INR and 12% above 1000INR purchase
-    3% on music cds/dvds
-    Flat 18% on the imported commodities.
-    Books are exempted from tax.
-    On every purchase I get a receipt that has the below information :
-    Date and Time of purchase
-    List of commodities, each with their final price, tax amount with the applicable rate
-    Total amount payable
-    Additionally, a 5% discount is applied by the store if the bill exceeds 2000INR.

The bill is sorted in the ascending order of the commodity names.

Write an API that computes the taxes and the final bill amount. Sample inputs are given below. Output should have the total amount, total tax.

Sample: input

{
       "item": "Headache pills",
       "itemCategory": "Medicine",
       "quantity": 5,
       "price": 50
}

"""
import datetime
now = datetime.datetime.now()


class Item:
    
    def __init__(self, item, itemCategory, quantity, price, finalPrice, isImported):
        self.item = item
        self.itemCategory = itemCategory
        self.quantity = quantity
        self.price = price
        self.finalPrice = finalPrice
        self.isImported = isImported

def computeTax(itemCategory, quantity, price, isImported):
    finalPrice = 0
    if itemCategory == "Books":
        finalPrice = price*quantity
        return finalPrice
    elif isImported:
        finalPrice = (quantity*price*1.18)
        #finalPrice += finalPrice*0.18
        return finalPrice
    elif (itemCategory == "Medicine") or (itemCategory == "Clothes"):
        finalPrice = (quantity*price*1.05)
        return (finalPrice)
    elif (itemCategory == "Music"):
        finalPrice += (quantity*price*1.03)
        return (finalPrice)
    elif (itemCategory == "Clothes"):
        finalPrice += (quantity*price)
        if finalPrice > 1000:
            finalPrice += finalPrice*1.12
        else:
            finalPrice += finalPrice*1.05
        return finalPrice
        

def billItems():
    shoppingCart = list()

    print("\n\n-------- All In One Store, Bengaluru --------\n\n")
    #print("         Current date and time:         ")
    print(now.strftime('           %d-%m-%Y , %H:%M:%S         \n\n'))

    print("------------  Purchase particulars  --------\n\n")

    while True:
        categorySerial = int(input("Enter item Category serial number: 1. Medicine 2. Clothes 3. Music 4. Books 5. Check-out\n\nCategory? "))
        if(categorySerial == 5):
            print("Preparing your bill...")
            break
        categories = {1:"Medicine", 2:"Clothes", 3: "Music", 4: "Books", 5:"Exit"}
        itemCategory = categories[categorySerial]
        item = input("\nEnter item name: ")
        quantity = int(input("\nEnter quantity of item: "))
        price = int(input("\nEnter price per item: "))
        isImported = bool(input("\nIs it Imported (True/False): "))
        finalPrice = computeTax(itemCategory, quantity, price, isImported)
        itemCounter = 0
        shoppingCart.append(Item(item,itemCategory, quantity, price, finalPrice, isImported))
    return shoppingCart

def computeAmount(shoppingCart):
    i = 0
    cartAmount = 0
    print(shoppingCart[0].finalPrice)
    while i != len(shoppingCart):  
        cartAmount = cartAmount + shoppingCart[i].finalPrice
        i += 1
    if cartAmount>1000:
        return (cartAmount - cartAmount*0.05)
    else:
        return cartAmount

shoppingCart = billItems()
cartAmount = computeAmount(shoppingCart)
#print(cartAmount)

def sortItemsByName(shoppingCart):
    i = 0
    itemNames = []
    while i != len(shoppingCart):
        itemNames.append(shoppingCart[i].item)
        i += 1
    itemNames.sort()
    
    
    return itemNames

sortedItemNames = sortItemsByName(shoppingCart)

def printBill(shoppingCart, sortedItemNames):
    
    i = 0

    while i != len(sortedItemNames):
        j = 0
        while j != len(shoppingCart):
            if (sortedItemNames[i] == shoppingCart[j].item):
                
                print("\n\nSerial-no: {0}\nItem-name: {1}\nItem-category: {2}\nQuantity: {3}\nPrice-per-unit: {4}\nImported: {5}\nAmount: {6}".format(i+1, shoppingCart[j].item, shoppingCart[j].itemCategory, shoppingCart[j].quantity, shoppingCart[j].price, shoppingCart[j].isImported, shoppingCart[j].finalPrice))
            j += 1
        i += 1


printBill(shoppingCart, sortedItemNames)
print("\n\n-------------------------------------------------\n\n")
print("Your total final bill amount is Rs. {0}".format(cartAmount))
print("\n\n-------------------------------------------------\n\n")

print("Note: 5% on medicines and Food, 5% on clothes below 1000 INR and 12% above 1000INR purchase, 3% on music cds/dvds, Flat 18% on the imported commodities. Total amount payable,Additionally, a 5% discount is applied by the store if the bill exceeds 2000INR.")
##billItems()








    
    
