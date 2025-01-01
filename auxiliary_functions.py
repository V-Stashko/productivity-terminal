import os

def get_current_location() -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, 'db.txt')
    return db_path

def correct_format_day(day: str) -> bool:
    if (count := day.count('.') == 2):
        lst = day.split('.')
        digits = tuple(map(lambda el: el.isdigit, lst))
        res = digits + (count,)
        return any(res)
    else:
        return False

def correct_result(result: str) -> bool:
    return int(result) in (0, 25, 50, 75, 100) if result.isdigit() else False

def filter_lines(lines: list, day: str) -> list:
    lst = [line.strip() for line in lines if day in line]
    return lst

def print_lines(lines: list) -> None:
    if len(lines):
        print('-' * 30)
        for line in lines:
            print(line)
        print('-' * 30)
    else:
        print('\nError: day not found. Try again 😔', end='\n\n')