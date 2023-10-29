purchase_price = int(input("Enter the purchase price: "))
discount = 0
if purchase_price < 100:
    discount = 5
    purchase_price *= 0.95
elif purchase_price > 200:
    discount = 15
    purchase_price *= 0.85
else:
    discount = 10
    purchase_price *= 0.9
print("Your discount is {}%, the amount to be paid is ${:.2f}.".format(
    discount,
    purchase_price,
))