import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")

data = {row.letter:row.code for (index, row) in file.iterrows()}

print(data)
def nato():
    user_input = input("What is the word: ").upper()
    try:
        word_code = [data[code] for code in user_input]
    except KeyError:
        print("Sorry, words have only letters")
        nato()
    else:
        print(word_code)

nato()