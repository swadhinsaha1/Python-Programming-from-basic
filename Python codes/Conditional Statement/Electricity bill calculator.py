# Up to 100 units → ₹0.80 per unit
# Up to 200 units → ₹1.00 per unit (for the next 100 units)
# Above 200 units → ₹1.25 per unit
unit = int(input("Enter the units = "))

if unit <= 100:
    paisa = unit * 0.80

elif unit <= 200:
    paisa = (100 * 0.80) + (unit - 100) * 1.00

else:
    paisa = (100 * 0.80) + (100 * 1.00) + (unit - 200) * 1.25

print("The bill will be ₹", paisa)