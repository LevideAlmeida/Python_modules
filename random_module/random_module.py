# the random_module have pseudo-random numbers generators.
# pseudo-random numbers: numbers that look randons, but are not.
# documentarion: https://docs.python.org/pt-br/3/library/random.html
import random

# Functions:
# seed
#   -> define the value that the random_module "choose" a random number
# random.seed(0)

# random.randrange(start, end, step)
#   -> Generates a int random number in (start-end) range

# random number in (10-20) range with step = 2
r_range = random.randrange(10, 20, 2)
# print(r_range)

# random.randint(start, end)
#   -> Generates a int random number in a (start-end) range, "without step"
r_int = random.randint(10, 20)
# print(r_int)

# random.uniform(início, fim)
#   -> Generates a float random number in a (start-end) range, "without step"
r_uniform = random.uniform(10, 20)
# print(r_uniform)

# random.shuffle(list or similar) -> shuffle list, modifying the original list
names = ['Luiz', 'Maria', 'Helena', 'Joana']
random.shuffle(names)
# print(names)

# random.sample(Iterable, k=N)
#   -> shuffle a iterable and returns a new iterable (no repeats values)
new_names = random.sample(names, k=3)
# print(new_names)

# random.choices(Iterable, k=N)
#   -> shuffle a iterable and returns a new iterable (repeats values)
new_names = random.choices(names, k=3)
# print(names)
# print(new_names)

# random.choice(Iterable) -> Choice one iterable element
# print(random.choice(names))
