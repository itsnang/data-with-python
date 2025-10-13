product1_weight, product1_price = eval(input("Enter weight and price for package 1: "))
product2_weight, product2_price = eval(input("Enter weight and price for package 2: "))

product1 = product1_weight / product1_price
product2 = product2_weight / product2_price

if(product1 < product2):
  print("Package 1 has a better price.")
else:
  print("Package 2 has a better price.")
