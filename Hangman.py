import random

word_list = ["howard", "family", "nepal", "downtown", "apple"]

chosen_word = random.choice(word_list)

display_word = "_" * len(chosen_word)
guessed_letters = []
max_attempts = 4 

print("Welcome to Hangman!")

while "_" in display_word and max_attempts > 0:
    print(display_word)
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display_word = display_word[:i] + guess + display_word[i + 1:]
    else:
        max_attempts -= 1
        print(f"Wrong guess! You have {max_attempts} attempts left.")

if "_" not in display_word:
    print(f"Congratulations! You guessed the word: {chosen_word}")
else:
    print(f"Sorry, you're out of attempts. The word was: {chosen_word}")
