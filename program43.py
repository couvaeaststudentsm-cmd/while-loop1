import random

while True:
    user_actions = input("Enter a choice(rock,paper,scissors): ")
   
    possible_actions = ['rock','paper','scissors']
    coumpter_action = random.choice(possible_actions)
    
    print(f"You chose{user_actions},computer chose{coumpter_action}.\n")
    if user_actions == coumpter_action:
        print(f"Both players selected{user_actions}.It's a tie")
    elif user_actions == 'rock':
        if coumpter_action == 'scissors':
            print("Rock smahes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_actions == 'scissors':
        if coumpter_action == 'paper':
            print("Scisoors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again?(y/n):")
    if play_again != 'y':
      break
 

    