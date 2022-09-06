#main game
def main():
    #Built in Modules
    import random
    
    #Variables and Lists
    user_wins = 0
    computer_wins = 0
    selection = ["rock", "paper", "scissors"]
        
    #Begin
    while True:
        user_input = input("Type Rock, Paper, or Scissors to play.  Type 'Q' to quit:  ").lower()
        if user_input == "q":
            break
        
        if user_input not in selection:
            print("Please enter 'rock', 'paper', or 'scissors'\n")
            continue
        
        random_number = random.randint(0, 2)
        #0 = ROCK, 1 = PAPER, 2 = SCISSORS
        computer_pick = selection[random_number]

        print("Computer picked " + computer_pick + ".")

        if user_input == "rock" and computer_pick == "scissors":
            print("You won!")
            user_wins += 1
            
        elif user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1
            
        elif user_input == "scissors" and computer_pick == "paper":
            print("You won!")
            user_wins += 1

        elif user_input == computer_pick:
            print("It's a tie!")
            user_wins += 0
            computer_wins += 0

        else:
            print("You lost!")
            computer_wins += 1

        if user_wins == 3 or computer_wins == 3:
            results_screen(user_wins, computer_wins)
        
#Results Screen
def results_screen(user_wins, computer_wins):
    print("You won " + str(user_wins) + " times.")
    print("The computer won " + str(computer_wins) + " times.")
    game_restart()
    
#Restart Game?  Yes or no?
def game_restart():
    restart = input("Do you want to play again?\n").lower()

    if restart == "yes":
        print("Ok Great!")
        main()
    
    elif restart == "no":
        print("Thank you for playing my game.")
        quit()

    else:
        print("Please choose 'yes' or 'no'")
        game_restart()

main()

