# 1. Welcome the User
print("Welcome to Code & Beans!")
print("-----------------------------")

customer_name = input("What is your name?\n> ")

print(f"Hello, {customer_name}! Here is our menu for today:")
print("\n")

# 2. Display the Menu
item1_name = "Coffee"
item1_price = 2.50

item2_name = "Tea"
item2_price = 2.00

item3_name = "Sandwich"
item3_price = 5.50

print("-----------------------------")
print(f"1. {item1_name} - ${item1_price:.2f}")
print(f"2. {item2_name} - ${item2_price:.2f}")
print(f"3. {item3_name} - ${item3_price:.2f}")
print("-----------------------------")
print("\n")

# 3. Take the Order
# Setup variables for the loop
total_cost = 0
ordered_items = []
is_ordering = True

while is_ordering:
  # Ask the user for their order
  order = input("What would you like to order? (Type the item name or 'done' to finish)\n> ")

  # Use .lower() to make the user's input case-insensitive
  if order.lower() == item1_name.lower():
    total_cost += item1_price
    ordered_items.append(item1_name)
    print(f"Added {item1_name} to your order.")

  elif order.lower() == item2_name.lower():
    total_cost += item2_price
    ordered_items.append(item2_name)
    print(f"Added {item2_name} to your order.")

  elif order.lower() == item3_name.lower():
    total_cost += item3_price
    ordered_items.append(item3_name)
    print(f"Added {item3_name} to your order.")

  elif order.lower() == 'done':
    is_ordering = False

  else:
    print("Sorry, we don't have that item. Please try again.")

  if is_ordering:
      print(f"Your order so far: {', '.join(ordered_items)}")
      print(f"Current total: ${total_cost:.2f}\n")

# 4. Calculate Final Total & Print Receipt
# This code runs AFTER the user types 'done'

# Define the sales tax rate (7% = 0.07)
SALES_TAX_RATE = 0.07
sales_tax = total_cost * SALES_TAX_RATE
grand_total = total_cost + sales_tax

print("\n") # Add some space before the receipt
print(f"Thanks for your order, {customer_name}! Here is your receipt:")
print("========================")
print(f"Customer: {customer_name}")
print("Items Ordered:")

# Use a for loop to print each item from the list on a new line
for item in ordered_items:
  print(f"- {item}")

print("------------------------")
print(f"Subtotal:      ${total_cost:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"Grand Total:   ${grand_total:.2f}")
print("========================")
print("Please come again!")