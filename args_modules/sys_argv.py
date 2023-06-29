import sys

arguments = sys.argv
qtd_arguments = len(arguments)

# print(arguments, qtd_arguments)

if qtd_arguments <= 1:
    print("you didn't pass arguments")
else:
    print(f"you passed this arguments: {arguments[1:]}")

if '-sum' in arguments:
    n1 = input('insert the first number: ')
    n2 = input('insert the second number: ')
    n1 = int(n1)
    n2 = int(n2)
    n_sum = n1 + n2
    print(n_sum)

if '-sub' in arguments:
    n1 = input('insert the first number: ')
    n2 = input('insert the second number: ')
    n1 = int(n1)
    n2 = int(n2)
    n_sub = n1 - n2
    print(n_sub)

if '-multi' in arguments:
    n1 = input('insert the first number: ')
    n2 = input('insert the second number: ')
    n1 = int(n1)
    n2 = int(n2)
    n_multi = n1 * n2
    print(n_multi)

if '-division' in arguments:
    n1 = input('insert the first number: ')
    n2 = input('insert the second number: ')
    n1 = int(n1)
    n2 = int(n2)
    n_division = n1 / n2
    print(n_division)
