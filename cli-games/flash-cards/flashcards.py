# import the json and random.
import json
import random

# Set game state so we can call it and change it with input later.
game_state = True
# This is so we can use user input to later select which deck to study.
# Josh Faigan and I pair-programmed much of these stretch goals togther.
warcraft = 'warcraft.json'
capitals = 'me-capitals.json'
anime = 'anime.json'


while (game_state) == True:

    print("What are we studying today?")
    print("Input : warcraft, anime, or capitals")
    input_deck = input().lower()
    # This if stetement is how we parse the json to grab the deck, then we shuffle the cards.
    # To shuffle we needed to convert the dictionairy type to a list type.
    # This took far too much effort to figure out, Alex Rocha was instrumental figuring this out with us.
    if input_deck == 'warcraft':
        with open((warcraft), 'r') as f:
            data = list(json.load(f)["cards"])
            random.shuffle(data)
            print("You picked Warcraft!")
    elif input_deck == 'anime':
        with open((anime), 'r') as f:
            data = list(json.load(f)["cards"])
            random.shuffle(data)
            print("You picked Anime!")
    else:
        with open((capitals), 'r') as f:
            data = list(json.load(f)["cards"])
            random.shuffle(data)
            print("You picked Capitals!")

    # This will give us the score as we answer cards through the deck right or wrong.
    # Every time the game loops the score resets to 0 and recounts a new total based on deck selection.
    total = len(data)   
    score = 0

    for i in data:
        guess = input(i["q"] + ":")
        answer = i["a"]
        # Safeguarding input inconsistencies.
        if guess.upper() == answer.upper():
            score += 1
            print(f"Correct! Current score: {score}/{total}")
        else:
            print(f"Incorrect! The correct answer was", i["a"])
            print(f"Current score: {score}/{total}")
    
    # Feedback for improvement.
    total_half = total / 2
    if score == total:
        print("Amazing")
    elif score == 0:
        print("You suck!")
    elif score > total_half:
        print("Good Work")
    elif score < total_half:
        print("You could use some practice")

    
    print(f'Your Final Score is {score} out of {total}')
    if (input(f'Would you like to play again? yes or no :') == 'yes'):
        print("Another round coming up!")
    else:
        print("Thanks for playing!")
        break
