import random

bars = ["McSorley's Old Ale House",
        "Death & Company",
        "The Back Room",
        "PDT"]

people = ["Mattan",
          "Sarah",
          "that person you forgot to text back",
          "Samuel L. Jackson",
          "Daniel"]

random_bar = random.choice(bars)
random_person = random.choice(people)
random_person2 = random.choice(people)

print(f"How about you go to {random_bar} with {random_person} and {random_person2}?")
