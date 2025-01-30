import pandas as pd

# Read the CSV into a DataFrame
df = pd.read_csv("nato_phonetic_alphabet.csv")

NATO = {row.letter: row.code for _, row in df.iterrows()}
print(NATO)

word = input("Enter a word: ").upper()

word_split = list(word.upper())

# output_dict = [NATO[letter] for letter in word]
# print(output_dict)

for letter in word_split:
    if letter in NATO:
        print(NATO[letter])