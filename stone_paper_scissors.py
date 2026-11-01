import random
ch=["stone", "paper", "scissor"]
while True:
    you = input("Enter your choice (stone, paper or scissor): ").lower()
    if you not in ch:
        print("Invalid, please enter stone, paper or scissor")
        continue
    computer=random.choice(ch)
    print("Your choice is:", you)
    print("Computer choice is:", computer)
    if you==computer:
        print("It's a draw!!")
    elif (you == "stone" and computer == "scissor") or \
         (you == "scissor" and computer == "paper") or \
         (you == "paper" and computer == "stone"):
        print("You Win, Yaayy!!")
    else:
        print("Computer Wins!!")
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break
