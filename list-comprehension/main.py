import pandas as pd

NATO_letters = pd.read_csv("nato_phonetic_alphabet.csv")
letters = {row.letter: row.code for (index, row) in NATO_letters.iterrows()}

word = input("Enter a word: ").upper()
word_list = [letters[letter] for letter in word]
print(word_list)