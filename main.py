from auxiliary_functions import *

def get_help() -> None:
    print(text_help)

def read_file() -> None:
    while not correct_format_day((day := input("Enter the day in \"DD.MM.YY\" format: "))):
        print('\nError: wrong format. Try again 😔', end='\n\n')
    
    with open('db.txt', mode='rt', encoding='utf-8') as file:
        lines = file.readlines()

    print_lines(filter_lines(lines, day))

def write_file() -> None:
    while not correct_format_day((day := input("Enter the day in \"DD.MM.YY\" format: "))):
        print('\nError: wrong format. Try again 😔', end='\n\n')

    task = input('Enter a task name: ')

    while not correct_result((result := input("Enter result (0, 25, 50, 75, 100): "))):
        print('\nError: wrong result. Try again 😔', end='\n\n')

    with open('db.txt', mode='a', encoding='utf-8') as file:
        file.write(f"{day} {task} {result}%\n")

    print("\nThe task successfully recorded 📝", end='\n\n')

def clear_file() -> None:
    while (answer := input("Do you really want to clear all data? (yes, no): ")) not in ('yes', 'no'):
        print('\nError: wrong answer. Try again 😔', end='\n\n')

    if answer == 'yes':
        with open('db.txt', mode='w') as file:
            file.write('')

        print("\nThe file cleaned successfully 🗑️", end='\n\n')

def main() -> None:
    commands = {'help': get_help, 'read': read_file, 'write': write_file, 'clear': clear_file}

    while True:
        inp = input('Enter the command (help, read, write, clear, exit): ')
        if inp == 'exit':
            break
        elif inp not in commands:
            print('\nError: the command not recognized. Try again 😔', end='\n\n')
        else:
            commands[inp]()

if __name__ == '__main__':
    print('Hello 🙋', end='\n\n')
    main()
    print('\nGood luck 😉')