
total = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(number):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.1

print("Total price for ", number, " items is $", total, sep='')


print("Total price for {} items is ${:.2f}".format(number, total))