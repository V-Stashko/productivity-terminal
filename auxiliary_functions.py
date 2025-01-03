def correct_format_day(day: str) -> bool:
    """
    Validates if the given day string is in the format 'DD.MM.YY' and represents a valid date.

    Args:
        day (str): The date string to validate.

    Returns:
        bool: True if the format is correct and the date is valid, otherwise False.
    """
    if day.count('.') != 2:
        return False

    try:
        day_parts = list(map(int, day.split('.')))
        day_valid = 1 <= day_parts[0] <= 31
        month_valid = 1 <= day_parts[1] <= 12
        year_valid = day_parts[2] == 25 
        return day_valid and month_valid and year_valid
    except ValueError:
        return False

def correct_result(result: str) -> bool: 
    """
    Validates if the given result is a string representation of an integer
    and belongs to the numbers (0, 25, 50, 75, 100).

    Args:
        result (str): The input string to validate.

    Returns:
        bool: True if the result is valid, otherwise False.
    """
    return int(result) in (0, 25, 50, 75, 100) if result.isdigit() else False

def filter_lines(lines: list, day: str) -> list:
    """
    Filters the lines in the list, returning only those that contain the specified day.

    Arguments:
        lines (list): A list of strings to filter.
        day (str): The day in the "DD.MM.YY" format to search for in the strings.

    Returns:
        list: A list of strings that contain the specified day.
    """
    lst = [line.strip() for line in lines if day in line]
    return lst

def print_lines(lines: list) -> None:
    """
    Prints the lines in a formatted manner. If no lines are provided, an error message is displayed.

    Arguments:
        lines (list): A list of strings to be printed. Each string will be printed on a new line.

    Returns:
        None: This function does not return anything, it only prints to the console.
    """
    if len(lines):
        print('-' * 30)
        for line in lines:
            print(line)
        print('-' * 30)
    else:
        print('\nError: day not found. Try again 😔', end='\n\n')