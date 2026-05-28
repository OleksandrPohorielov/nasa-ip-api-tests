from datetime import date, timedelta


def get_yesterday_date():
    yesterday = date.today() - timedelta(days=1)
    return yesterday.isoformat()