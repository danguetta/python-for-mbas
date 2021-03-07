# Variables are just nicknames
# they're plain, lowercase words

name = "Mattan Griffel"
orphan_fee = 200
teddy_bear_fee = 121.80
total = orphan_fee + teddy_bear_fee

print(name, "the total will be", total)

# This will produce an error unless you've already defined subtotal
# print(subtotal)

# You can use an f-string to put a variable directly into a string
print(f"{name}, the total will be ${total:,.2f}")