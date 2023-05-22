# Solved exercise: calculating the dates and installments of a loan
# Maria took a loan of 1,000,000 to make the payment in 5 years.
# The date she took the loan was 12/20/2020 and
# each installment is due on the 20th of each month.
# - Create the loan date
# - Create the loan end date
# - Show all due dates and the value of each installment

from datetime import datetime, timedelta

loan = 1_000_000
number_of_installments = 12 * 5
installment_value = loan / number_of_installments

date_start = datetime.strptime(f'20/12/2022', '%d/%m/%Y')
month = 0
date_end = date_start

print(number_of_installments)

while month < number_of_installments:

    date_end += timedelta(days=1)
    
    if date_end.day == 20:
        month += 1
        print(date_end.strftime('%d/%m/%Y'), f'R$ {installment_value:,.2f}')
    

