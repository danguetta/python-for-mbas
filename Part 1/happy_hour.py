import random

bars = ["McSorley's Old Ale House",
        "Death & Company",
        "The Back Room",
        "PDT"]

people = ["Mattan",
          "Sarah",
          "that person you forgot to text back",
          "Samule L. Jackson"]

random_bar = random.choice(bars)
random_person = random.choice(people)

print(f"How about you go to {random_bar} with {random_person}?")
