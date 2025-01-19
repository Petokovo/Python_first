import random

def guess_number():
    random_number = random.randint(1, 100)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > random_number:
            print("Sorry, guess again. Too high")
        elif guess < random_number:
            print("Sorry, guess again. Too low")
    print(f"Congratulations! You have guessed the number {random_number}")

def computer_guess():
    print("Ahoj mysli si číslo od 1 do 100 a ja ho budem musieť uhádnuť:)")
    input("Pre pokračovanie stlač ľubovolnú klávesnícu...")

    low = 1
    high = 100
    feedback = ""
    while feedback != "s":
        guess = random.randint(low, high)
        while True:
            feedback = input(f"Je číslo {guess} moc veľké(V), moc malé(M) alebo správne(S)?").lower()
            if feedback in ["v", "m", "s"]:
                if feedback == "v":
                    high = guess - 1
                    break
                elif feedback == "m":
                    low = guess + 1
                    break
                else:
                    break
            else:
                print("Treba zadať iba V, M alebo S")
                continue
        if feedback == "s":
            again = input("Super uhádol som :) Chceš hrať znovu? (áno/nie)").lower()
            if again in ["áno", "ano"]:
                low = 1
                high = 100
                feedback = ""
                continue
            else:
                print("Dovidenia:)")
                break

computer_guess()