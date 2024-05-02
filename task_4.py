import datetime

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    today = datetime.date.today()
    upcoming_date = today + datetime.timedelta(7)
    

    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = datetime.date(today.year, birthday.month, birthday.day)
        upcoming_birthday_date = birthday_this_year
        if birthday_this_year < today:
            upcoming_birthday_date = datetime.date(today.year + 1, birthday.month, birthday.day)

        if today <= upcoming_birthday_date < upcoming_date:
            congratulation_date = upcoming_birthday_date
            weekends = (5, 6)
            if upcoming_birthday_date.weekday() in weekends:
                congratulation_date = upcoming_birthday_date + datetime.timedelta(days = 7 - upcoming_birthday_date.weekday())

            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    sorted_upcoming_birthdays = sorted(upcoming_birthdays, key=lambda x: x["congratulation_date"])
    return sorted_upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.04.19"},
    {"name": "Jane Smith", "birthday": "1985.04.20"},
    {"name": "Bibop", "birthday": "1988.04.21"},
    {"name": "Picka Picka", "birthday": "2002.04.22"},
    {"name": "Mr. Anderson", "birthday": "2000.04.26"},
    {"name": "Trinity", "birthday": "1999.04.27"},
    {"name": "Alex", "birthday": "1980.05.07"},
    {"name": "Sergii", "birthday": "1980.05.06"},
    {"name": "Maks", "birthday": "1980.05.05"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)