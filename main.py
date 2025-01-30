import pandas as pd

# Read the CSV into a DataFrame
df = pd.read_csv("nato_phonetic_alphabet.csv")

NATO = {row.letter: row.code for _, row in df.iterrows()}
print(NATO)

word = input("Enter a word: ").upper()

def display_NATO():
    output_dict = []
    for letter in word:
        if letter in NATO:
            output_dict.append(NATO[letter])
        else:
            print(f"You entered an invalid character: {letter} ")
    print(output_dict)

# word_split = list(word.upper())
try:
    display_NATO()
except KeyError:
    print("Please enter a valid word with alphabetic characters.")

# for letter in word_split:
#     if letter in NATO:
#         print(NATO[letter])