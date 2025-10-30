amount_of_purchase = eval(input("Enter the purchase amount of purchase: "))

discount_over_100 = 0.10
discount_under_100 = 0.05

if amount_of_purchase > 100:
    discount = amount_of_purchase * discount_over_100
else :
    discount = amount_of_purchase * discount_under_100

final_price = amount_of_purchase - discount

print("Final amount after discount:", final_price)
