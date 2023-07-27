import requests 
import html

art = [(r""" _________  ________  ___  ___      ___ ___  ________          ________  ________  _____ ______   _______      
|\___   ___\\   __  \|\  \|\  \    /  /|\  \|\   __  \        |\   ____\|\   __  \|\   _ \  _   \|\  ___ \     
\|___ \  \_\ \  \|\  \ \  \ \  \  /  / | \  \ \  \|\  \       \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|    
     \ \  \ \ \   _  _\ \  \ \  \/  / / \ \  \ \   __  \       \ \  \  __\ \   __  \ \  \\|__| \  \ \  \_|/__  
      \ \  \ \ \  \\  \\ \  \ \    / /   \ \  \ \  \ \  \       \ \  \|\  \ \  \ \  \ \  \    \ \  \ \  \_|\ \ 
       \ \__\ \ \__\\ _\\ \__\ \__/ /     \ \__\ \__\ \__\       \ \_______\ \__\ \__\ \__\    \ \__\ \_______\
        \|__|  \|__|\|__|\|__|\|__|/       \|__|\|__|\|__|        \|_______|\|__|\|__|\|__|     \|__|\|_______|""")]


api_url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=multiple"
response = requests.get(api_url)


tf_api_url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean"
tf_response = requests.get(tf_api_url)


data = response.json()
tf_data = tf_response.json()
print(art[0])
for i in range(5):
    print("")


def unes(word):
    return html.unescape(word)
def play_mult():
    
    score = 0

    for i in data["results"]:
        new_answers= []
        new_answers.append(i["correct_answer"])
        for x in i["incorrect_answers"]:
            new_answers.append(x)
    
        xx = (i["correct_answer"])
        new_answers.sort()

        for u in range(len(new_answers)):
            new_answers[u] = html.unescape(new_answers[u])
        
        print(unes(i["question"]))
        print(new_answers)
        user_answer = input("what is your answer? ")
        if user_answer == xx:
              print("correct")
              score += 1
        else:
              print("you suck")
        print("----------------------")
    print(f"\n Your final score was: {xx}")


def play_tf():
    for i in tf_data["results"]:
        print(html.unescape(i["question"]))
        print(i["correct_answer"])
        print("---")
play_mult()

