secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count<guess_limit:
    guess = int(input("Enter a number "))
    guess_count = guess_count+1
    if guess == secret_number:
        print("You win")
        break
    if guess_count == guess_limit:
        print("Out of attempts")
        break