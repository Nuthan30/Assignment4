with open('Output.txt', 'w') as file:
    user_input = input('Enter text to write to the file: ')
    file.write(user_input+'\n')
    print('Data is successfully written to output.txt')

with open('Output.txt', 'a') as file:
    additional_input = input('Enter addition text to append: ')
    file.write(additional_input+'\n')
    print('Data successfully appended')

with open('Output.txt', 'r') as file:
    final_content = file.read()
    print('\nfinal content of output.txt: ')
    print(final_content)
