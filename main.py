import auxiliary_functions as axl_func
import text

def get_help() -> None:
    """print text_help
    """    
    print(text.text_help)

def read_file() -> None:
    """
    Prompts the user to enter a day in 'DD.MM.YY' format, reads data from 'db.txt',
    filters lines by the specified day, and prints the filtered lines.
    """
    while not axl_func.correct_format_day((day := input("Enter the day in \"DD.MM.YY\" format: "))):
        print('\nError: wrong format. Try again 😔', end='\n\n')
        
    with open('db.txt', mode='a+', encoding='utf-8') as file:
        file.seek(0)
        lines = file.readlines()
            
    axl_func.print_lines(axl_func.filter_lines(lines, day))

def write_file() -> None:
    """
    Prompts the user to input a day in 'DD.MM.YY' format, a task name, and a result 
    percentage (0, 25, 50, 75, 100). Validates the input and appends the task 
    information to 'db.txt'.
    """
    while not axl_func.correct_format_day((day := input("Enter the day in \"DD.MM.YY\" format: "))):
        print('\nError: wrong format. Try again 😔', end='\n\n')

    task = input('Enter a task name: ')

    while not axl_func.correct_result((result := input("Enter result (0, 25, 50, 75, 100): "))):
        print('\nError: wrong result. Try again 😔', end='\n\n')

    with open('db.txt', mode='a', encoding='utf-8') as file:
        file.write(f"{day} {task} {result}%\n")

    print("\nThe task successfully recorded 📝", end='\n\n')

def clear_file() -> None:
    """
    Prompts the user for confirmation to clear all data from 'db.txt'.
    If the user confirms with 'y', the file is cleared. Otherwise, no action is taken.
    """
    while (answer := input("\nDo you really want to clear all data? (y, n): ")) not in ('y', 'n'):
        print('\nError: wrong answer. Try again 😔', end='\n\n')

    if answer == 'y':
        with open('db.txt', mode='w') as file:
            file.write('')

        print("\nThe file cleaned successfully 🗑️", end='\n\n')

def main() -> None:
    """
    Main function to handle user commands.

    Provides a command-line interface for the following commands:
    - 'help': Display help information.
    - 'read': Read data from the file.
    - 'write': Write new data to the file.
    - 'clear': Clear all data from the file.
    - 'exit': Exit the program.
    """
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