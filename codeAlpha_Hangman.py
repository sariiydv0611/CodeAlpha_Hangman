import random

words = ["python", "apple", "computer", "school", "robot"]

word = random.choice(words)

guessed_word = ["_"] * len(word)
incorrect_guess = 0
max_guess = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while incorrect_guess < max_guess and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guess left:", max_guess - incorrect_guess)

    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct!")
    else:
        incorrect_guess += 1
        print("Wrong guess!")

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)