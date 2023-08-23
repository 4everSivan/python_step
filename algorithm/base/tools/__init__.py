import random


def generate_random_list(length, minimum, maximum):
    random_list = []
    for _ in range(length):
        random_number = random.randint(minimum, maximum)
        random_list.append(random_number)
    return random_list
