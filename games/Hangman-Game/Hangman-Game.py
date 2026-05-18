import random

print("=" * 50)
print("   WELCOME TO HANGMAN GAME")
print("=" * 50)

# Expanded word list categorized by difficulty (length)
word_categories = {
    "1": ["python", "java", "code", "data", "web", "logic", "task", "link", "host", "user"], # Easy: 3-5 letters
    "2": ["program", "network", "monitor", "storage", "laptop", "desktop", "server", "browser"], # Medium: 6-7 letters
    "3": ["algorithm", "programming", "software", "hardware", "database", "developer", "variable", "function"] # Hard: 8+ letters
}

print("\n🎯 Select Difficulty:")
print("1️⃣ Easy (3-5 letters)")
print("2️⃣ Medium (6-7 letters)")
print("3️⃣ Hard (8+ letters)")

while True:
    choice = input("\nEnter choice (1-3): ").strip()
    if choice in word_categories:
        words = word_categories[choice]
        difficulty_name = {"1": "Easy", "2": "Medium", "3": "Hard"}[choice]
        break
    print("❌ Invalid choice! Please select 1, 2, or 3.")

word = random.choice(words)
word_length = len(word)

guessed_letters = []
correct_letters = []
max_attempts = 6
attempts = 0
won = False

print(f"\nSelected Difficulty: {difficulty_name}")
print(f"The word has {word_length} letters.")
print(f"You have {max_attempts} attempts to guess the word.\n")

while attempts < max_attempts and not won:
    display = ""
    for letter in word:
        if letter in correct_letters:
            display += letter + " "
        else:
            display += "_ "
    
    print(f"Word: {display}")
    print(f"Attempts remaining: {max_attempts - attempts}")
    print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
    
    guess = input("\nGuess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter!")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)
    
    if guess in word:
        print(f"✓ Correct! '{guess}' is in the word.")
        correct_letters.append(guess)
        
        all_guessed = True
        for letter in word:
            if letter not in correct_letters:
                all_guessed = False
                break
        
        if all_guessed:
            won = True
    else:
        print(f"✗ Wrong! '{guess}' is not in the word.")
        attempts += 1
    
    print("-" * 50)

print("\n" + "=" * 50)
if won:
    print("🎉 CONGRATULATIONS! YOU WON!")
    print(f"The word was: {word}")
    print(f"You guessed it with {max_attempts - attempts} attempts remaining!")
else:
    print("😔 GAME OVER! YOU LOST!")
    print(f"The word was: {word}")
print("=" * 50)
