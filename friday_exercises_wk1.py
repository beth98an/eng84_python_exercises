# Some more exercises

# Task 1: Control Flow Age and Permission

age = input("What is your age? ")
driving_licence = input("Do you have a driving licence? y/n ")
while age != "exit":
    while driving_licence != "exit":
        age = int(age)
        if age >= 18:
            if driving_licence == "y":
                print("You can vote and drive")
            elif driving_licence == "n":
                print("You can vote")
        elif age == 17 and driving_licence == "y":
            print("You can drive")
        elif age >= 16 and driving_licence == "n":
            print("you can't legally drink but your mates/uncles might have your back")
        else:
            print("You're too young, go back to school!")
        age = input("What is your age? ")
        driving_licence = input("Do you have a driving licence? y/n ")

# Task 2: Your Hero Story!
story1 = {
    "start": "This is the start",
    "middle": "This is the middle",
    "end": "This is the end"
}
print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())
print(story1["start"])
print(story1["middle"])
print(story1["end"])
story1["hero"] = "a superhero"
