from _datetime import datetime, timedelta


def get_upcoming_birthdays(user_list):
    today = datetime.today().date()
    future_birthdays = []
    for user in user_list:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)

            future_birthdays.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})

    return future_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.04.27"},
    {"name": "John Smith", "birthday": "1985.04.22"},
    {"name": "Jane Smith", "birthday": "1990.04.30"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
