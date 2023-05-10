import pandas as pd

nato_df = pd.read_csv('nato_phonetic_alphabet.csv', index_col='letter')

nato_dict = {index: row.code for (index, row) in nato_df.iterrows()}

user_name = input('Enter your name: ').upper()
names_list = [nato_dict[letter] for letter in user_name]
print(names_list)
