
from random import randint

pc_choice = randint(1, 50)  # I imported this
playing = True
print("🚦🚦🚦Welcome to Python Casino!🚦🚦🚦")

while playing == True:
    user_choice = int(input("Choose number."))
    if user_choice == pc_choice:
        print(
            f"Your number is {user_choice}, Pc choose number is {pc_choice}. Congraturation! You Win!")
        playing = False
    elif user_choice > pc_choice:
        print("Lower!")
    elif user_choice < pc_choice:
        print("Higher!")
"""
        while distance < 20:
            print("I'm running:", distance, "km")
            distance = distance + 1
"""
