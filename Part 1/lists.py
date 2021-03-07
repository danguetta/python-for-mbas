# In Python, lists are a way of grouping
# (usually) similar things together
the_count = [1, 2, 3, 4, 5]
stocks = ["FB", "AAPL", "NFLX", "GOOG"]
random_things = [55, 1/2, "Puppies", stocks]

print(random_things)

# You can start with an empty list
# and append or remove
people = []

people.append("Mattan")
people.append("Sarah")
people.append("Daniel")
people.remove("Sarah")

print(people)

# Use split() to turn a string into a list
cities = "New York, San Francisco, London".split(", ")
print(cities)

# Use join() to turn a list into a string
groceries = ["Milk", "Eggs", "Cheese"]
print(" and ".join(groceries))

# Access elements of a list using [ ]
first_city = cities[0]
second_city = cities[1]
last_city = cities[-1]
first_two_cities = cities[0:2]
print(first_two_cities)
