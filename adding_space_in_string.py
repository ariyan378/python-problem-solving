list = ['campusxIs', 'bestFor', 'dataScientist']
output = []

for word in list:
    
    modified_word = []

    for i , char in enumerate(word):

        if char.isupper() and i >0 :
            modified_word.append(' ')

        modified_word.append(char)

    output.append(''.join(modified_word))


print(output)            