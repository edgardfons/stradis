from datetime import datetime

def parse_date(str_date):
    return datetime.strptime(str_date, '%d/%m/%Y')

def sql_date_format(date):
    return date.strftime('%Y-%m-%d')

def sql_ilike_format(value):
    return "%{}%".format(value)