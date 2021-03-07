# Use for to loop over a list
numbers = [1, 2, 3]
for number in numbers:
    print(number)

stocks = ["fb", "aapl", "nflx", "goog"]
for stock in stocks:
    print(stock.upper())

# Looping Challenge
for number in range(1, 11):
    print(number, "squared is", number * number)

squares = []
for number in range(1, 11):
    squares.append(number * number)
    print(squares)
