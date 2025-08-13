# menu = {
#     "Pizza": 40,
#     "Pasta": 50,
#     "Burger": 60,
#     "Salad":  70,
#     "Coffee": 80,
# }
#
# print("Welcome to Python Restaurant.")
# print("Pizza: Rs40\nPasta: Rs50\nBurger: 60\nSalad: 70\nCoffee: 80")
#
#
# order_total = 0
# item=input("Enter the name of item you want to order = ").capitalize()
# if item in menu:
#     order_total += menu[item]
#     print(f"Your item {item} has been added to your order and price of the order", order_total )
# else:
#     print(f"Ordered item {item} is not available yet.")


#------------------------------------------------------------------------------------------
# Two orders
# #Menu dictionary
# menu = {
#     "Pizza": 40,
#     "Pasta": 50,
#     "Burger": 60,
#     "Salad":  70,
#     "Coffee": 80,
# }
#
# print("Welcome to Python Restaurant!\n")
# print("Menu:")
#
# for item, price in menu.items():
#     print(f"{item}: Rs{price}")
#
# order_total = 0
# item_1=input("\nEnter the name of item you want to order = ").capitalize()
#
# if item_1 in menu:
#     order_total+=menu[item_1]
#     print(f"{item_1} added to your order. Total: Rs{order_total}")
# else:
#     print(f"Sorry, {item_1} is not avaliable")
#
#
# #Asking for another order
# anothor = input("\nDo you want to order another item? (yes/no): ").lower()
#
# if anothor == "yes":
#     item_2 = input("\nEnter the name of second item you want to order = ").capitalize()
#     if item_2 in menu:
#         order_total +=menu[item_2]
#         print(f"{item_2} added to your order. Total: Rs{order_total}")
#     else:
#         print(f"Sorry, {item_1} is not avaliable")
#
#
# print(f"\nFinal bill amount: Rs{order_total}")
# print("Thank you for visiting Python Restaurant!")


#------------------------------------------------------------------------
#order unlimited
#Menu dictionary
menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad":  70,
    "Coffee": 80,
}
print("Welcome to Python Restaurant!\n")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")
order_total = 0
while True:
    item=input("\nEnter the name of item you want to order = ").capitalize()
    if item in menu:
        quantity = int(input(f"How many {item}s would you like to order? "))
        order_total+=menu[item]*quantity
        print(f"{quantity} {item}s added to your order. Total: Rs{order_total}")
    else:
        print(f"Sorry, {item} is not avaliable")
#Ask if user wants to order more
    anothor = input("\nDo you want to order another item? (yes/no): ").lower()
    if anothor == "yes":
        continue
    elif anothor == "no":
       break
    else:
        print("You have entered wrong input. Type only yes/no")
        continue


print(f"\nFinal bill amount: Rs{order_total}")
print("Thank you for visiting Python Restaurant!")
