import random
def rpsGame():
    file1 = open("poojith_vs_python.txt", "a")
    askInput = input("Choose one of the three; Rock,Paper,Scissors : ")
    computer = random.choice(["Rock", "Paper" , "Scissors"])
    if askInput == computer:
        file1.write("Tie!" + "\n")
    elif askInput == "Rock":
        if computer == "Paper":
            file1.write("You lose. Computer chose Paper"+ "\n")
        else: 
            file1.write("You win! Computer chose Scissors"+ "\n")
    elif askInput == "Paper":
        if computer == "Scissors":
            file1.write("You lose. Computer chose Scissors"+ "\n")
        else:
            file1.write("You win! Computer chose Rock"+ "\n")
    elif askInput == "Scissors":
        if computer == "Rock":
            file1.write("You lose. Computer chose Rock"+ "\n")
        else:
            file1.write("You win! Computer chose paper"+ "\n")
    else:
        return file1.write("Input Invaild. Check your spelling!"+ "\n")
    file1.close()
rpsGame()
repeat = input("Would you like to play again? Yes or No: ")
if repeat == "Yes":
    rpsGame()
else:
    print("Thank you for playing!")