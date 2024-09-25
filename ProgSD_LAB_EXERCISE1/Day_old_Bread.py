REGULAR_PRICE = 3.49
DISCOUNT = 0.60

num_loaves = int(input("Enter the number of day old loaves being purchased: "))

regular_price = num_loaves * REGULAR_PRICE
discount_amount = regular_price * DISCOUNT
total_price = regular_price - discount_amount

print(f"Regular price: £{regular_price:.2f}")
print(f"Discount:      £{discount_amount:.2f}")
print(f"Total price:   £{total_price:.2f}")