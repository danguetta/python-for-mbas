# Function Challenge #3
def future_value(present_value, rate, periods=1):
    return round(present_value * (1 + rate) ** periods, 2)

print(future_value(present_value=1000, rate=.1, periods=5))
