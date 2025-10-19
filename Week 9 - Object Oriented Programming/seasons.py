from datetime import date
import sys
import inflect
import re


def main():
    p = inflect.engine()
    today = date.today()

    try:
        birthday = input("Birthday: ")
        print(get_minutes(today, date.fromisoformat(inspect_birthday(birthday)), p))

    except ValueError:
        print("Invalid Date Format")
        sys.exit(1)

def get_minutes(today, b_day, p):
    days = today - b_day
    minutes = ((days.days * 24) * 60)
    return f"{p.number_to_words(minutes, andword ='')} minutes"


def inspect_birthday(b_day):
    if re.search(r"\d{4}-+\d{2}-+\d{2}", b_day):
        d_day = b_day.split('-')
        if int(d_day[0]) < 2025:
            return b_day
        else:
            return f"Invalid Date Format"
    else:
        return f"Invalid Date Format"
    


if __name__ == "__main__":
    main()