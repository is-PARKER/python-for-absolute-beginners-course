print("Hello World")

given = input("Gimme a number? ")
given_num = int(given)
odd_even = given_num % 2


while given_num > 0:



    if odd_even == 0 and given_num == 0:
        print(f" {given_num} is even!")
        break
    elif odd_even == 0:
        print(f" {given_num} is even!")
        given = input("New number? ")
        given_num = int(given)
        odd_even = given_num % 2
    else:
        print(f"{given_num} is odd!")
        given = input("New number? ")
        given_num = int(given)
        odd_even = given_num % 2

print("That's not a number!")
