import random

random.seed()
choice = ""
g_choice = ""

while True:
    num_list = [0]
    num_min = int(input("Enter the minimum number: "))
    num_max = int(input("Enter the maximum number: "))
    num_list  = range(num_min, num_max + 1)
    p_choice = random.choice(num_list)

    while g_choice != p_choice:
        g_choice = int(input("Guess the number I chose: "))
        if g_choice > p_choice:
            print("The number I thought is less than yours. Try again")
        elif g_choice < p_choice:
            print("The number that I thought is greater than yours. Try again")
        else:
            print("You guessed!!")
            break


    choice  = str(input("Do you want to replay [Y/n]:"))
    if choice == "" or choice == "Y" or choice == "y":
        pass
    else:
        break

print("See you at the next game!")
