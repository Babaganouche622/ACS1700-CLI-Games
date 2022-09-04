from random import randint

# These set the game
roles = ["bear", "Ninja", "Cowboy"]
player = False
score = 0

# This is where we ask if the player needs instructions.
print("Let's play Bear, Ninja, Cowboy.")
instructions = input("Do you need instructions?:" ).upper()
if instructions == "YES":
    print("Bears > Ninja \nBears < Cowboys \nNinja > Cowboys \nNinja < Bears \nCowboys > Bears \nCowboys < Ninja")
    print("Pick your fighter and fight the Computer.")

# Here we build our functions out for how points are scored and the game rules.
def bear(player, computer, score):
    if computer == "BEAR":
        print("The Bears start wrastling!")
        print(f"Draw! {score}")
        return score
    if computer == "NINJA":
        print(f"{player} eats {computer}")
        score += 1
        print(f"Gain a point! {score}")
        return score
    if computer == "COWBOY":
        print(f"{player} shot by {computer}")
        score -= 1
        print(f"Lose a point! {score}")
        return score

def ninja(player, computer, score):
    if computer == "BEAR":
        print(f"{player} eaten by {computer}")
        score -= 1
        print(f"Lose a point! {score}")
        return score
    if computer == "NINJA":
        print("The Ninjas vanish!")
        print(f"Draw! {score}")
        return score
    if computer == "COWBOY":
        print(f"{player} stabs {computer}")
        score += 1
        print(f"Gain a point! {score}")
        return score

def cowboy(player, computer, score):
    if computer == "BEAR":
        print(f"{player} shoots {computer}")
        score += 1
        print(f"Gain a point! {score}")
        return score
    if computer == "NINJA":
        print(f"{player} stabbed by {computer}")
        score -= 1
        print(f"Lose a point! {score}")
        return score
    if computer == "COWBOY":
        print("The Cowboys ride off into the sunset.")
        print(f"Draw! {score}")
        return score

# This is where we start our gameplay loop.
while player == False:
    player = input("Bear, Ninja, or Cowboy? > ").upper()
    computer = roles[randint(0,2)].upper()

    # This is where we confirm that the player is inputing a valid fighter.
    while True:
        #player = input("Bear, Ninja, or Cowboy? > ").upper()
        if player not in ["BEAR", "NINJA", "COWBOY"]:
            print(f"{player} is not Bear, Cowboy, or Ninja.")
            player = input("Bear, Ninja, or Cowboy?: ").upper()
        else:
            break

    # This is the game itself. 
    if player == "BEAR":
        score = bear(player, computer, score)
        
    if player == "NINJA":
        score = ninja(player, computer, score)

    if player == "COWBOY":
        score = cowboy(player, computer, score)

    # Do we play again? We print the score either way for the player to keep track as they win and lose.
    play_again = input("Would you like to play again? (yes/no): ").upper()
    if play_again == "yes".upper():
        print(score)
        player = False
    else:
        print(f"Total score: {score}")
        print("Thanks for playing!")
        break
    