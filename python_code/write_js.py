import csv, random

with open('transcriptions.csv', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    words = [{'word':row[0], 'phonemic':row[1],'phonetic':row[2]} for row in reader]

with open('test.js', 'w') as js_file:
    for word in words:
        js_file.write('{question: "How is the word \"'+word['word']+'\" transcribed?, answers: [ { text:' + word['phonemic']+ ', correct: true }]},\n')


groups = [['i', 'ɪ'], ['u', 'ʊ'], ['p', 'b'], ['θ', 'ð'], ['a', 'æ'], ['t', 'd']]

def generate_false(phonemic):
    false_answers = []

    for letter in phonemic:
        print(letter)
        for group in groups:
            if letter in group:
                selection_group = group[:]
                selection_group.remove(letter)
                print(selection_group)
                substitute_letter = random.choice(selection_group)
                print(substitute_letter)
        false_answers.append(phonemic.replace(letter, substitute_letter))
    return(false_answers)
print(generate_false('pit'))
