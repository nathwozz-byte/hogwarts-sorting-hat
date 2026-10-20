print("welcome to hogwarts sorting hat")
trait = input("what trait best describes you?\n").lower()

if trait == "brave":
    print("griffindor")
elif trait == "intelligent":
    print("ravenclaw")
elif trait == "loyal":
    print("hufflepuff")
elif trait == "ambitious":
    print("slytherin")   
else:
    print("hat is confused")