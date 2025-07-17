import random

# Predefined list of 5 words
word_list = ["apple", "banana", "grape", "mango", "peach"]

# Select a random word from the list
secret_word = random.choice(word_list)

# Create a list to store guessed letters and wrong guesses
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Display version of the word (e.g. "_ _ _ _ _")
display_word = ["_" for _ in secret_word]

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 chances to guess wrong.\n")

# Main game loop
while wrong_guesses < max_wrong and "_" in display_word:
    print("Word: " + " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Invalid input. Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
        print("✅ Good guess!\n")
    else:
        wrong_guesses += 1
        print(f"❌ Wrong guess! You have {max_wrong - wrong_guesses} guesses left.\n")

# Final result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The word was:", secret_word)
