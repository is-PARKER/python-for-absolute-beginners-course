import random


print("---------------------")
print("  M&M guessing game  ")
print("---------------------")

mm_count = random.randint(1,100)
attempt_limit = 0
attempts = 0

print("Guess the number of M&Ms!")
print()

while attempts < attempt_limit:
    guess_text = input("How many M&MS? ")
    guess = int(guess_text)
    attempts += 1

    if guess == mm_count:
        print(f"you got free lunch. It was {guess}.")
        break
    elif guess < mm_count:
        print("That's too LOW")
    else:
        print("That's too HIGH")



print(f"Only {attempts} attempt! Goodjob!")



