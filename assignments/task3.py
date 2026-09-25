receipt = "receipt"
item = "coffee"
price = 45.5
quantity = 3
item=item.upper()
print("Item: " + item + ", quantity: " + str(quantity))

total = price * quantity
print("Total: " + str(total) + " UAH")
print(f"Average: {total / quantity:.2f}")