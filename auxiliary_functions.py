def correct_format_date(date: str) -> bool:
    """
    Validates if the given day string is in the format 'DD.MM.YY' and represents a valid date.

    Args:
        date (str): The date string to validate.

    Returns:
        bool: True if the format is correct and the date is valid, otherwise False.
    """
    if date.count('.') != 2:
        return False

    try:
        date_parts = list(map(int, date.split('.')))
        date_valid = 1 <= date_parts[0] <= 31
        month_valid = 1 <= date_parts[1] <= 12
        year_valid = date_parts[2] == 25 
        return date_valid and month_valid and year_valid
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

def filter_lines(lines: list, filter_read: str, fltr: str) -> list:
    """
    Filters a list of lines based on a specified criterion and value.

    This function processes a list of strings (`lines`) and filters them based 
    on the value of the filter (`fltr`) provided by the user. The filter type 
    is determined by `filter_read`, which can be 'date', 'task', or 'result'.

    Args:
        lines (list): A list of strings where each line is expected to have 
                      components separated by '--->'.
        filter_read (str): The filter criterion ('date', 'task', or 'result') 
                           to determine which component of each line to check.
        fltr (str): The value to match within the specified filter's component.

    Returns:
        list: A list of filtered lines that match the specified criterion and value.

    Raises:
        KeyError: If `filter_read` is not a valid key ('date', 'task', 'result') 
                  in the filter dictionary.
        IndexError: If a line does not have the expected format with '--->' separators.
    """
    dct_filter = {'date': 0, 'task': 1, 'result': 2}
    lst = [line for line in lines if fltr.lower() in line.split('--->')[dct_filter[filter_read]].lower()]

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
            print(' '.join(line.strip().split('--->')))
        print('-' * 30)
    else:
        print('\nError: Not found. Try again 😔', end='\n\n')