# Ask user to input a type of muscle (skeletal, cardiac, or smooth)
def muscleType():
    skelMuscle = ["bicep", "sternocleidomastoid", "tibialis anterior"]
    cardiacMuscle = ["heart", "myocardium", "pericardium"]
    smoothMuscle = ["bladder", "stomach", "esophagus"]

    userMuscle = raw_input("Which type of muscle would you like to see examples for - skeletal, cardiac, or smooth?")

    skeletal = "skeletal"
    cardiac = "cardiac"
    smooth = "smooth"

    if userMuscle == skeletal:
        for s in skelMuscle:
            print s
    elif userMuscle == cardiac:
        for c in cardiacMuscle:
            print c
    elif userMuscle == smooth:
        for m in smoothMuscle:
            print m
    else:
        print "Please enter 'skeletal', 'cardiac', or 'smooth'"

muscleType()