is_shopping = True
counter_items = 0
subtotal = 0
customer_name = input("Enter customer name: ")
while(is_shopping):
    product_name = input("Enter product name: ")
    if product_name.lower() == "done":
        is_shopping = False
        break
    price_in_KZT = float(input("Enter price (KZT): "))
    counter_items += 1
    subtotal += price_in_KZT

if subtotal >= 7000:
    discount_tier = "Gold"
    discount = subtotal * 0.15
elif subtotal >= 3000:
    discount_tier = "Silver"
    discount = subtotal * 0.05
else:
    discount_tier = "No discount"
    discount = 0.0

total = subtotal - discount
print(" " * 30)
print(f"Customer : {customer_name.upper()}")
print(f"Items : {counter_items}")
print(f"Subtotal : {subtotal} KZT")
print("-" * 30)
print(f"Discount_tier : {discount_tier}")
print(f"Discount : {discount} KZT")
print(f"Total : {total} KZT")
print("-" * 30)
print(f"Name uppercase: {customer_name.upper()}")
print(f"Name lower: {customer_name.lower()}")
print(f"Name length: {len(customer_name)}")
if len(customer_name) > 5:
    print("Long name")
else:
    print("Short name")
