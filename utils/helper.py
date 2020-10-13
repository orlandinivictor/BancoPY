from datetime import date, datetime


def date_str(data):
    return data.strftime('%d/%m/%Y')


def str_date(data):
    return datetime.strptime(data, '%d/%m/%Y')


def formata_valor(valor):
    return f'R$ {valor:,.2f}'
