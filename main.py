with open('./Input/letters/starting_letter.txt') as letter:
    letter_format = letter.read()

# for each name in invited_names.txt
with open('./Input/Names/invited_names.txt') as names:
    name_list = names.readlines()
    for name in name_list:
        name_strip = name.strip()
        replace_name = letter_format.replace('[name]', name_strip)
        with open(f'./Output/ReadyToSend/letter_for_{name_strip}.txt', 'w') as completed_letter:
            completed_letter.write(replace_name)
