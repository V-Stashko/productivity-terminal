def correct_format_day(day: str) -> bool:
    if day.count('.') == 2 and tuple(map(lambda el: el.isdigit(), day.split('.'))):
        tpl = tuple(map(int, day.split('.')))
        days = 1 <= tpl[0] <= 31
        months = 1 <= tpl[1] <= 12
        years = tpl[2] == 25
        res = days, months, years
        return all(res)
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