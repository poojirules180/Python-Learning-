import random
file1 = open("poojith_vs_python.txt", "w")
askInput = input("Choose one of the three; Rock,Paper,Scissors : ")
computer = random.choice(["Rock", "Paper" , "Scissors"])
if askInput == computer:
    file1.write("Tie!")
elif askInput == "Rock":
    if computer == "Paper":
        file1.write("You lose. Computer chose Paper")
    else:
        file1.write("You win! Computer chose Scissors")
elif askInput == "Paper":
    if computer == "Scissors":
        file1.write("You lose. Computer chose Scissors")
    else:
        file1.write("You win! Computer chose Rock")
elif askInput == "Scissors":
    if computer == "Rock":
        file1.write("You lose. Computer chose Rock")
    else:
        file1.write("You win! Computer chose paper")
else:
    file1.write("Input Invaild. Check your spelling!")

file1.close()