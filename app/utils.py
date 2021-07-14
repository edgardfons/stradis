from datetime import datetime

def parse_date(str_date):
    return datetime.strptime(str_date, '%d/%m/%Y')

def sql_date_format(date):
    return date.strftime('%Y-%m-%d')

def sql_ilike_format(value):
    return "%{}%".format(value)

def parse_hour(value):
    return int(value.replace(':', ''))

def format_hour(value):
    value = str(value)
    return ('0' + value[:1] if len(value) == 3 else value[:2]) + ':' + value[-2:]