from auxiliary_functions import *

def get_help() -> None:
    print()
    print("🌟 Welcome to the Activity Tracker! 🌟")
    print()
    print("✍️ To add a new entry, type the command \"write\" and follow the instructions")
    print("📖 To view your activity, type the command \"read\" and follow the instructions")
    print("🗑️  To clear your activity, type \"clear\" and follow the instructions")
    print("🚪 To exit the program, type the command \"exit\"")
    print()
    print("🎉 Enjoy tracking your progress! 🎉")
    print()

def read_file() -> None:
    location = get_current_location()

    while not correct_format_day((day := input("Enter the day in \"DD.MM.YY\" format: "))):
        print('\nError: wrong format. Try again 😔', end='\n\n')
    
    with open(location, mode='rt', encoding='utf-8') as file:
        lines = file.readlines()

    print_lines(filter_lines(lines, day))

def write_file() -> None:
    location = get_current_location()

    while not correct_format_day((day := input("Enter the day in \"DD.MM.YY\" format: "))):
        print('\nError: wrong format. Try again 😔', end='\n\n')

    task = input('Enter a task name: ')

    while not correct_result((result := input("Enter result (0, 25, 50, 75, 100): "))):
        print('\nError: wrong result. Try again 😔', end='\n\n')

    with open(location, mode='a', encoding='utf-8') as file:
        file.write(f"{day} {task} {result}%\n")

    print("\nThe task successfully recorded 📝", end='\n\n')

def clear_file() -> None:
    while (answer := input("Do you really want to clear all data? (yes, no): ")) not in ('yes', 'no'):
        print('\nError: wrong answer. Try again 😔', end='\n\n')

    if answer == 'yes':
        location = get_current_location()

        with open(location, mode='w') as file:
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