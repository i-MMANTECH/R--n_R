CoffeeSel = ("Coffee Selection Menu:\n\nCappucino Price:15\nExpresso Price:12\nLatte Price:$11\nIced Latte Price:16\nIced Cappuccino Price:20\n")
print(CoffeeSel)


takeout = input("Do you want a takeout?(yes/no) ")
coffeeType = input("Please enter your coffee type: ")
coffee = float(input("Please enter coffee price: "))


tax = coffee * (7/100) #tax rate is 7%
takeout = coffee * (18/100) #takeout rate is 18%

total = coffee + tax + takeout

print("Tax amount: $",tax)
print("Tax amount(If Takeout):$", takeout)
print("Total amount for "+coffeeType+"=$", total)