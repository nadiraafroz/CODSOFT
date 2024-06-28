import random

print("Welcome to Rock-Paper-Scissors Game!")

user_score = 0
computer_score = 0
tie = 0

name = input("Enter your name:")
print("""
      Winning Rules:
1. paper vs rock --> paper
2. rock vs scissor --> rock
3. scissor vs paper --> scissor           """)

while True:
        print(""" 
        choices are:
        1.rock
        2.paper
        3.scissor""")

        choice = int(input("enter your choice from 1-3:"))
        print()
        while choice>3 or choice<1:
                choice = int(input("enter valid choice:"))

        if choice == 1:
                user_choice= "rock"
        elif choice == 2:
                user_choice= "paper"
        else:
                user_choice= "scissor"
        print("The user's choice is:", user_choice)

        computer = random.randint(1,3)

        if computer == 1:
                computer_choice = "rock"
        elif computer == 2:
                computer_choice = "paper"
        else:
                computer_choice = "scissor"

        print("The computer's choise is: ", computer_choice)
        if ((user_choice == "paper" and computer_choice == "rock")or (user_choice == "rock" and computer_choice == "paper")):
                print("paper wins")
                result = "paper"
        elif ((user_choice == "scissor" and computer_choice == "rock")or (user_choice == "rock" and computer_choice == "scissor")):
                print("rock wins")
                result = "rock"
        elif(user_choice == computer_choice):
                print("it's a tie")
                result = "tie"
        else:
                print("scissor wins")
                result = "scissor"

        if result == "tie":
                tie += 1
        elif result == user_choice:
                user_score +=1
        else:
                computer_score +=1

        print("scores are:")
        print(name,"'s score is:", user_score)
        print(" computer's score is:", computer_score)
        print(" tie's are:", tie)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
                print("Thanks for playing!")
                break





        













