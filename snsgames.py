def dice():
    import random
    min = 1
    max = 6

    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        print("Rolling the dices...")
        print("The values are....")
        print(random.randint(min, max))
        print(random.randint(min, max))

        roll_again = input("Roll the dices again?")


def rps():
    import random
    answer = input("Please enter rock, paper or scissors:")     
    user = answer.lower()
    print ("You chose" , answer)
    command = ["rock" , "paper" , "scissors"]
    computer_choice = random.choice(command)

    if user == "rock" and computer_choice == "rock":
        print("I chose" , computer_choice)
        print("Draw!")
    
    elif user == "scissors" and computer_choice == "scissors":
        print ("I chose" , computer_choice)
        print("Draw!") 
    
    elif user == "paper" and computer_choice == "paper":
        print ("I chose" , computer_choice)
        print("Draw!") 
    
    elif user == "paper" and computer_choice == "rock":
        print ("I chose" , computer_choice)
        print("You win!")  
    
    elif user == "rock" and computer_choice == "scissors":
        print ("I chose" , computer_choice)
        print("You win!")
    
    elif user == "scissors" and computer_choice == "paper":
        print ("I chose" , computer_choice)
        print("You win!") 
    
    elif user == "rock" and computer_choice == "paper":
        print ("I chose" , computer_choice)
        print("I win!")
    
    elif user == "paper" and computer_choice == "scissors":
        print ("I chose" , computer_choice)
        print("I win!")       
    
    elif user == "scissors" and computer_choice == "rock":
        print ("I chose" , computer_choice)
        print("I win!")
