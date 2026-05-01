# Dont delete this .....
def game():

    print("Welcome to the number guessing game!\nI am thinking of a number between 1 and 100.\n \t\tGUESS THAT NUMBER.")
    num=input("Enter the mode 'hard' or 'easy': ").lower()
    while num not in ("hard","easy"):
        print("Select the mode correctly.")
        num = input("Enter the mode 'hard' or 'easy': ").lower()
    EASY=10
    HARD=5

    import random

    def mode_guess(life):
        a = random.randint(1, 100)

        guess=int(input(f"Enter the number to guess,\nyou have {life} chances to guess: "))
        while life>0:

            if guess==a:
                print(f"Ya you got it ,the number is {a} ")
                again=input("Do you wanna play again?(y or n): ").lower()
                if again=="y":
                    game()
                else:
                    exit()
            elif guess>a:
                print("Too high!")
                life -= 1
                guess = int(input(f"Enter number to guess,\nyou have {life} chances to guess: "))

            elif guess <a:
                print("Too low")
                life -= 1
                guess = int(input(f"Enter number to guess,\nyou have {life} chances to guess: "))
        if life ==0:
            print("You are ran out of given chances ,BETTER LUCK NEXT TIME.")

    if num == "hard":
        mode_guess(HARD)
    elif num == "easy":
        mode_guess(EASY)

game()
