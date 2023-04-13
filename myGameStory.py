# This is the story file

def chap1(Player1):
    match Player1.type:
        case 1:
            # Barbarian Subclass 1 "Berserker"
            filePath = "c:/Users/nicho/Documents/My Creation/Story Files/Berzerker/Chapter 1.txt"
        case 2:
            # Barbarian Subclass 2 "Ancestral Guardian"
            filePath = "c:/Users/nicho/Documents/My Creation/Story Files/Ancestral Guardian/Chapter 1.txt"
        case 3:
            # Knight Subclass 1 "Crusader"
            filePath = "c:/Users/nicho/Documents/My Creation/Story Files/Knights 1/Chapter 1.txt"
        case 4:
            # Knight Subclass 2 "Champion"
            filePath = "c:/Users/nicho/Documents/My Creation/Story Files/Knight 2/Chapter 1.txt"
        case 5:
            # Assassin Subclass 1
            filePath = "c:/Users/nicho/Documents/My Creation/Story Files/Assassin 1/Chapter 1.txt"
        case 6:
            # Assassin Subclass 2
            filePath = "c:/Users/nicho/Documents/My Creation/Story Files/Assassin 2/Chapter 1.txt"
        case 7:
            # Monk Subclass 1
            filePath = "c:/Users/nicho/Documents/My Creation/Story Files/Monk 1/Chapter 1.txt"
        case 8:
            # Monk Subclass 2
            filePath = "c:/Users/nicho/Documents/My Creation/`Story Files/Monk 2/Chapter 1.txt"
        
    with open(filePath, "r") as file:
        text = file.read()
    print(text)
    input("\n(Press ENTER to continue...)")


def chap2(Player1):
    match Player1.type:
        case 1:
            # Barbarian Subclass 1
            print("The first barbarian subclass")
        case 2:
            # Barbarian Subclass 2
            print("The second barbarian subclass")
        case 3:
            # Assassin Subclass 1
            print("The first assassin subclass")
        case 4:
            # Assassin Subclass 2
            print("The second assassin subclass")
        case 5:
            # Knight Subclass 1
            print("The first knight subclass")
        case 6:
            # Knight Subclass 2
            print("The second knight subclass")
        case 7:
            # Monk Subclass 1
            print("The first monk subclass")
        case 8:
            # Monk Subclass 2
            print("The second monk subclass")
    input("\n(Press ENTER to continue...)")
