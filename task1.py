from datetime import datetime


def get_days_from_today(date):
    try:
        specified_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        difference = current_date - specified_date
        return difference.days
    except ValueError:
        print("Error: Incorrect date format. Please use the format 'YYYY-MM-DD'.")
        return None


print(get_days_from_today('2024-04-30'))
