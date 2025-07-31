import datetime


def get_current_year():
    now_date = datetime.datetime.now()
    return now_date.year

def get_year_days_ago(count_days):
    now_date = datetime.datetime.now()
    goal = now_date - datetime.timedelta(days=count_days)
    return goal.year
