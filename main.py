import auxiliary_functions as axl_func
import text

def get_help() -> None:
    """
    Displays the help text stored in the `text.text_help` variable.

    This function retrieves and prints a predefined help message. 
    The `text.text_help` variable should contain the help text as a string.
    """
    print(text.text_help)

def read_file() -> None:
    """
    Filters and displays data from 'db.txt' based on user input.

    The user selects a filter type (date, task, result, all) to view specific data:
        - 'date': Filter by a specific date ("DD.MM.YY").
        - 'task': Filter by a task name.
        - 'result': Filter by a numeric result (0, 25, 50, 75, 100).
        - 'all': Display all data.

    Uses helper functions `axl_func.filter_lines` and `axl_func.print_lines` 
    for filtering and displaying lines.
    """
    filter_read = input("Select a data sorting filter (date, task, result, all): ")
    while filter_read not in ('date', 'task', 'result', 'all'):
        print('\nError: wrong filter. Try again 😔', end='\n\n')
        filter_read = input("Select a data sorting filter (date, task, result, all): ")

    with open('db.txt', mode='a+', encoding='utf-8') as file:
        file.seek(0)
        lines = file.readlines()

    if filter_read == 'date':
        while not axl_func.correct_format_date((fltr := input("Enter the day in \"DD.MM.YY\" format: "))):
            print('\nError: wrong format. Try again 😔', end='\n\n')
    elif filter_read == 'task':
        fltr = input('Enter a task name: ')
    elif filter_read == 'result':
        while not axl_func.correct_result((fltr := input("Enter result (0, 25, 50, 75, 100): "))):
            print('\nError: wrong result. Try again 😔', end='\n\n')
    else:
        axl_func.print_lines(lines)
        return

    axl_func.print_lines(axl_func.filter_lines(lines, filter_read, fltr))

def write_file() -> None:
    """
    Prompts the user to input a date in 'DD.MM.YY' format, a task name, and a result 
    percentage (0, 25, 50, 75, 100). Validates the input and appends the task 
    information to 'db.txt'.
    """
    while not axl_func.correct_format_date((date := input("Enter the date in \"DD.MM.YY\" format: "))):
        print('\nError: wrong format. Try again 😔', end='\n\n')

    task = input('Enter a task name: ')

    while not axl_func.correct_result((result := input("Enter result (0, 25, 50, 75, 100): "))):
        print('\nError: wrong result. Try again 😔', end='\n\n')

    with open('db.txt', mode='a', encoding='utf-8') as file:
        file.write(f"{date}--->{task}--->{result}%\n")

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