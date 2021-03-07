# Functions are little snippets of code
# that we can reuse over and over
def average(numbers):
	return sum(numbers) / len(numbers)

grades = [90, 85, 74]
prices = [12.99, 9.99, 5.49, 7.50]

print(average(grades))
print(average(prices))
print(average([0, 1, -1]))


def get_city(address):
    return address.split(', ')[1]

columbia = "3022 Broadway, New York, NY 10027, USA"
city = get_city(columbia)
print(city)


# Function Challenge #1
def get_state(address):
    return address.split(', ')[2].split()[0]

state = get_state(columbia)
print(state)


def divisible_by(number, divisor):
    return number % divisor == 0

print(divisible_by(number=15, divisor=3))
print(divisible_by(number=20, divisor=3))


# Function Challenge #2
def uppercase_and_reverse(text):
    return text.upper()[::-1]

print(uppercase_and_reverse('Banana'))
