## guessing game with if, while, var and all previous knowledge
## using secret until with get it right

secret_word = "Awana_Academy" ## this is the secret word
guess = ""
guess_count = 0## counter var
guess_limit = 3 ## limit var
out_of_guesses = False
### prompt the user to enter a word until they guess it correctly
### set limit on the nomber of guesses that a user can have

while guess != secret_word and not (out_of_guesses): ## as long word not guess keep looping
    if guess_count < guess_limit:
        guess = input("Please enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses")
else:
    print("You won")

