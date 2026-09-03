from texttools.cleaning import clean_text
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency

text = input("Enter text: ")

cleaned = clean_text(text)

print("Cleaned Text:", cleaned)

words = tokenize(cleaned)

print("Tokens:", words)

frequency = word_frequency(words)

print("Word Frequency:", frequency)