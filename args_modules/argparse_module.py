# argparse.ArgumentParser for complex arguments
# Oficial Tutorial:
# https://docs.python.org/pt-br/3/howto/argparse.html

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b',
    '--basic',
    help='basic value to run code',
    type=str,
    metavar='',
    default=0,
    # nargs='+',  # Receive multiple args
)

parser.add_argument(
    '-s',
    '--sum',
    help='sum values in a list',
    action='store_true'
)

parser.add_argument(
    '-S',
    '--subtract',
    help='subtract values in a list',
    action='store_true'
)

parser.add_argument(
    '-m',
    '--multiplicate',
    help='multiplicate values in a list',
    action='store_true'
)

parser.add_argument(
    '-d',
    '--division',
    help='divide values in a list',
    action='store_true'
)

args = parser.parse_args()

if args.basic is None:
    print("You didn't pass basic value.")
    print(args.basic)
else:
    print(f"basic value: {args.basic}")

if args.sum:
    n1 = input('insert the first number: ')
    n2 = input('insert the second number: ')
    n1 = int(n1)
    n2 = int(n2)
    n_sum = n1 + n2
    print(n_sum)

if args.subtract:
    n1 = input('insert the first number: ')
    n2 = input('insert the second number: ')
    n1 = int(n1)
    n2 = int(n2)
    n_sub = n1 - n2
    print(n_sub)

if args.multiplicate:
    n1 = input('insert the first number: ')
    n2 = input('insert the second number: ')
    n1 = int(n1)
    n2 = int(n2)
    n_multiplicate = n1 * n2
    print(n_multiplicate)

if args.division:
    n1 = input('insert the first number: ')
    n2 = input('insert the second number: ')
    n1 = int(n1)
    n2 = int(n2)
    n_division = n1 // n2
    print(n_division)
