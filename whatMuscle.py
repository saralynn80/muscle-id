def muscleType():
    skelMuscle = ["bicep", "sternocleidomastoid", "tibialis anterior"]
    cardiacMuscle = ["heart", "myocardium", "pericardium"]
    smoothMuscle = ["bladder", "stomach", "esophagus"]

    userMuscle = raw_data("Enter muscle type: ")

    if userMuscle == skelMuscle:
        for s in skelMuscle:
            print s
    elif userMuscle == cardiacMuscle:
        for c in cardiacMuscle:
            print c
    elif userMuscle == smoothMuscle:
        for m in smoothMuscle:
            print m

muscleType()


def muscle():

    muscleType = ["Skeletal", "Caridac", "Smooth"]
    userMuscle = raw_input("Please enter a muscle: ")

    if userMuscle == "bicep":
        print "The bicep is made up of " + muscleType[0] + " muscle."
    elif userMuscle == "heart":
        print "The heart is made up of " + muscleType[1] + " muscle."
    elif userMuscle == "bladder":
        print "The bladder is made up of " + muscleType[3] + "muscle."
    else:
        print "Try typing bicep, heart, or bladder!"

muscle()
