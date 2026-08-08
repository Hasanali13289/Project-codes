import random

WORDS = [
    "python",
    "computer",
    "elephant",
    "mountain",
    "adventure",
    "keyboard",
]

HANGMAN_PICTURES = [
    r"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
    r"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
    r"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
    r"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
    r"""
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
""",
    r"""
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
""",
    r"""
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
""",
]

MAX_MISTAKES = len(HANGMAN_PICTURES) - 1


def display_word(secret_word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def get_guess():
    while True:
        guess = input("\nGuess a letter or the whole word: ").strip().lower()

        if not guess.isalpha():
            print("❌ Only letters are allowed.")
            continue

        return guess


def play_game():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_letters = set()

    print("\n🎮 Welcome to Hangman!")

    while len(wrong_letters) < MAX_MISTAKES:

        print(HANGMAN_PICTURES[len(wrong_letters)])
        print(f"Word: {display_word(secret_word, guessed_letters)}")
        print(f"Lives Remaining: {MAX_MISTAKES - len(wrong_letters)}")

        if guessed_letters:
            print("Correct:", " ".join(sorted(guessed_letters)))

        if wrong_letters:
            print("Wrong:  ", " ".join(sorted(wrong_letters)))

        if set(secret_word).issubset(guessed_letters):
            print(f"\n🎉 Congratulations! You guessed '{secret_word}'.")
            return

        guess = get_guess()

        # Whole word guess
        if len(guess) > 1:
            if guess == secret_word:
                print(f"\n🎉 Amazing! The word was '{secret_word}'.")
            else:
                wrong_letters.add(f"({guess})")
                print("❌ Incorrect word.")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print("⚠️ You already guessed that.")
            continue

        if guess in secret_word:
            guessed_letters.add(guess)
            print("✅ Correct!")
        else:
            wrong_letters.add(guess)
            print("❌ Wrong!")

    print(HANGMAN_PICTURES[-1])
    print(f"\n💀 Game Over! The word was '{secret_word}'.")


def main():
    while True:
        play_game()

        again = input("\nPlay again? (y/n): ").strip().lower()

        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
    
