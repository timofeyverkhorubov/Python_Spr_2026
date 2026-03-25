import re

def is_valid_date(year, month, day):
    if not (2000 <= year <= 2099):
        return False
    if not (1 <= month <= 12):
        return False
    days_in_month = [31, 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28,
                     31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 1 <= day <= days_in_month[month - 1]

def is_valid_time(hour, minute, second):
    return 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59

def main():
    text = input()
    pattern = re.compile(r'\b(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2}):(\d{2})\b')
    matches = []
    for match in pattern.finditer(text):
        year, month, day, hour, minute, second = map(int, match.groups())
        if is_valid_date(year, month, day) and is_valid_time(hour, minute, second):
            matches.append(match.group())
    for m in matches:
        print(m)

if __name__ == "__main__":
    main()