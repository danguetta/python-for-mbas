# Dictionaries let you label values using strings
stock = {"name": "Microsoft",
         "ticker": "MSFT",
         "index": "NASDAQ"}

print(f"{stock['name']}'s stock ticker is {stock['ticker']}")

# Dictionary Challenge
user = {'name': 'Mattan',
        'height': 70,
        'shoe size': 10.5,
        'hair': 'Brown',
        'eyes': 'Brown'}

print(f"Name: {user['name']}")
print(f"Height: {user['height']}")
print(f"Shoe Size: {user['shoe size']}")
print(f"Hair Color: {user['hair']}")
print(f"Eye Color: {user['eyes']}")

# Adding a Key/Value Pair to a Dictionary
stock["open price"] = 108.25
stock["close price"] = 106.03
print(stock)

# print(stock["Open Price"])

# Dictionary Challenge pt. 2
user['favorite movies'] = ['Pulp Fiction', 'Magnolia', 'The Royal Tenenbaums']
print(f"Favorite Movies: {', '.join(user['favorite movies'])}")

# Looping over a List of Dictionaries
mattan = {'name': 'Mattan',
          'height': 70,
          'shoe size': 10.5,
          'hair': 'Brown',
          'eyes': 'Brown',
          'favorite movies': ['Pulp Fiction',
                              'Magnolia',
                              'The Royal Tenenbaums']}

chris =  {'name': 'Chris',
          'height': 72,
          'shoe size': 11,
          'hair': 'Blonde',
          'eyes': 'Blue',
          'favorite movies': ['Shawshank Redemption',
                              'Lord of the Rings']}

lisa =   {'name': 'Lisa',
          'height': 64,
          'shoe size': 6.5,
          'hair': 'Black',
          'eyes': 'Brown',
          'favorite movies': ['Crazy Rich Asians',
                              'Avengers',
                              'Lord of the Rings']}

users = [mattan, chris, lisa]

for user in users:
    print(f"{user['name']}'s shoe size is {user['shoe size']}")

# Using If to Get a Subset of a List
large_shoes = []
for user in users:
    if user['shoe size'] > 10:
        large_shoes.append(user)

print(large_shoes)

lord_of_the_rings_lovers = []
for user in users:
    if 'Lord of the Rings' in user['favorite movies']:
        lord_of_the_rings_lovers.append(user)

print(lord_of_the_rings_lovers)

# VLOOKUP Challenge
for user in users:
    if user['name'] == 'Chris':
        print(', '.join(user['favorite movies']))
