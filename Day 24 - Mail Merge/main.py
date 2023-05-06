names = []

with open('./Input/Names/invited_names.txt', 'r') as names_file:
    for line in names_file.readlines():
        name = line.strip('\n')
        names.append(name)

with open('./Input/Letters/starting_letter.txt', 'r') as letter_file:
    letter_text = letter_file.read()


for name in names:
    letter = letter_text.replace('[name]', name.title())
    print(letter)
    with open(f'./Output/ReadyToSend/letter_for_{name.lower()}.txt', 'w') as personalized_letter:
        personalized_letter.write(letter)
