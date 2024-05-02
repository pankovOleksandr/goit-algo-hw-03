# Завдання 1

# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

import datetime

def get_days_from_today(date):
    today = datetime.date.today();
    try:
        fomattedDate = datetime.datetime.fromisoformat(date).date();
        return (today - fomattedDate).days
    except ValueError:
        print("Invalid format. Date should be in in format 'YYYY-MM-DD'")