count = 0
total = 0

while True:
    item_name = input('Item name (0 to finish): ')
    if item_name == '0':
        break
    try:
        price = float(input('Price: '))
    except ValueError:
        print("Please enter a valid number for price.")
        continue
    count += 1
    total += price

print('Number of item:', count)
print('Total price :', total)
