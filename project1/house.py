import images
print(images.images[0])
def ask_question(question, options):
    while True:
        try:
            print(question)
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")
            answer = int(input("Enter your answer: "))
            if answer < 1 or answer > len(options):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please try again.")
    return answer


def determine_house(answers):
    points = [0, 0, 0, 0]   #Gryffindor, Hufflepuff, Ravenclaw, Slytherin
    for answer in answers:
        if answer == 1:
            points[0] += 1
        elif answer == 2:
            points[1] += 1
        elif answer == 3:
            points[2] += 1
        elif answer == 4:
            points[3] += 1

    max_points = max(points)
    house = ""
    if points[0] == max_points:
        house += "Gryffindor "
    if points[1] == max_points:
        house += "Hufflepuff "
    if points[2] == max_points:
        house += "Ravenclaw "
    if points[3] == max_points:
        house += "Slytherin "

    return house.strip()

questions = [
    "Q1: Which of the following qualities do you value the most?",
    "Q2: What type of animal would you bring to Hogwarts as your pet?",
    "Q3: Which subject would you excel at?",
    "Q4: How would you like to be remembered in history?",
    "Q5: Which magical artifact would you choose to possess?",
    "Q6: What is your preferred method of travel?",
    "Q7: Which Hogwarts professor do you admire the most?",
    "Q8: What is your favorite magical creature?",
    "Q9: Which Hogwarts House do you admire the most?",
    "Q10: Which Hogwarts House would you least like to be sorted into?"
]

options = [
    ["Bravery", "Kindness", "Intelligence", "Ambition"],
    ["Owl", "Cat", "Toad", "Snake"],
    ["Charms", "Herbology", "Transfiguration", "Potions"],
    ["As a hero", "As a loyal friend", "As a wise scholar", "As a powerful leader"],
    ["The Sword of Gryffindor", "The Resurrection Stone", "The Diadem of Ravenclaw", "The Locket of Slytherin"],
    ["Broomstick", "Thestral", "Apparition", "Floo Powder"],
    ["Professor McGonagall", "Professor Sprout", "Professor Flitwick", "Professor Snape"],
    ["Phoenix", "Unicorn", "Hippogriff", "Basilisk"],
    ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"],
    ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
]

answers = []

for i in range(len(questions)):
    answer = ask_question(questions[i], options[i])
    answers.append(answer)
    print("--------------------------------------------------")
house = determine_house(answers)

print("the hat decided!, you should be sorted into the following Hogwarts house:")
print(house)



