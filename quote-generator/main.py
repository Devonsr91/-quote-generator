
import random

quotes = [
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("Stay hungry, stay foolish.", "Steve Jobs"),
    ("The future depends on what you do today.", "Mahatma Gandhi"),
    ("Great things are done by a series of small things brought together.", "Vincent van Gogh"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("Act as if what you do makes a difference. It does.", "William James"),
    ("Success is not final, failure is not fatal.", "Winston Churchill"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("Your limitation is only your imagination.", "Unknown")
]

random_quote = random.choice(quotes)

print("\n" + "=" * 55)
print("           DAILY INSPIRATION")
print("=" * 55)
print(f'\n"{random_quote[0]}"')
print(f"— {random_quote[1]}")
print("\n" + "=" * 55)
