import random

def main():
    print_top()
    gen_random()

def print_top():
    print("------------------------------")
    print("     M&M guessing game!")
    print("------------------------------")

    print("Guess the number of M&Ms and you get lunch on the house!")
    print()


def take_guess():
    guess_text = input("How many M&Ms are in the jar? ")
    guess = int(guess_text)
    return guess

def gen_random():
    mm_count = random.randint(1, 100)
    attempt_limit = 5
    attempts = 0

    while attempts < attempt_limit:
        attempts += 1
        guess = take_guess()

        if mm_count == guess:
            print(f"You got a free lunch! It was {guess}.")
            break
        elif guess < mm_count:
            print("Sorry, that's too LOW!")
        else:
            print("That's too HIGH!")

    print(f"Bye, you're done in {attempts}!")

if __name__ == "__main__":
    main()