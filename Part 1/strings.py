# Strings are text surrounded by quotes
# Both single (' ') and double (" ") can be used

kanye_quote = ('My greatest pain in life is that I will never '
'be able to see myself perform live.')
print(kanye_quote)

# Switch to single quotes if your string uses double-quotes
hamilton_quote = 'Well, the word got around, they said, "This kid is insane, man"'
print(hamilton_quote)

# A few string functions
print(kanye_quote.upper())
print(kanye_quote.lower())
print("ok fine".replace("fine", "great").upper())

# F-Strings let you write Python code directly inside of a string
# inside of curly brackets ({ })
print(f"1 + 1 equals {1 + 1}")
name = "mattan griffel"
print(f"{name.title()}, the total will be ${200 + 121.8 :,.2f}")
