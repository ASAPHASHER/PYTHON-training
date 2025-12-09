print("Welcome to Online Food Center!")
print("1. Veg Combo  - ₹199")
print("2. Non-Veg Combo - ₹399")

choice = int(input("Enter your choice (1 for Veg, 2 for Non-Veg): "))

# Food price selection
if choice == 1:
    food_price = 199
    print("You selected Veg Combo.")
elif choice == 2:
    food_price = 399
    print("You selected Non-Veg Combo.")
else:
    print("Invalid choice! Please select either 1 or 2.")
    exit()

# Enter distance
distance = float(input("Enter delivery distance in km: "))

# Delivery charge calculation
if distance <= 3:
    delivery_charge = 0
elif distance <= 6:
    delivery_charge = 6
else:
    delivery_charge = 8

# Total bill
total_bill = food_price + delivery_charge

print("\n----- BILL DETAILS -----")
print(f"Food Price       : ₹{food_price}")
print(f"Delivery Charge  : ₹{delivery_charge}")
print(f"Total Bill       : ₹{total_bill}")
print("-------------------------")
