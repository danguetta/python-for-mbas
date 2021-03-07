# Tip Calculator by Mattan Griffel and Daniel Guetta

# Convert the user's input into a float
amount = float(input("How much was your bill? "))

# Calculate the tip amounts
print(f"18%: ${amount * .18 :,.2f}")
print(f"20%: ${amount * .20 :,.2f}")
print(f"25%: ${amount * .25 :,.2f}")
