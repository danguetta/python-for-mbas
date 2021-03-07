answer = input("Do you want to hear a joke? ")

if answer.lower() in ["yes", "y"]:
    print("What's loud and sounds like an apple?")
    print("AN APPLE")
elif answer.lower() in ["no", "n"]:
    print("Fine.")
else:
    print("I don't understand.")