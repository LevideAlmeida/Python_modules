# string.Template for replace variables in texts
# doc: https://docs.python.org/3/library/string.html#template-strings

import string
import locale
from pathlib import Path
from datetime import datetime

locale.setlocale(locale.LC_ALL, '')

FILE_PATH = Path(__file__).parent / 'template-ex.txt'


def convert_to_brl(value: float) -> str:
    brl = locale.currency(value, symbol=False, grouping=True)
    return brl


date = datetime(2023, 8, 1)
datas = dict(
    name='Levi',
    amount=convert_to_brl(1_423_998),
    date=date.strftime('%d/%m/%Y'),
    company='Unitask',
    telephone="+55 85 966126626"
)

with open(FILE_PATH, 'r') as file:
    text = file.read()
    template = string.Template(text)
    print(template.substitute(datas))
