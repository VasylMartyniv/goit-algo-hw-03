import random


def get_numbers_ticket(minimum, maximum, quantity):
    if not (1 <= minimum):
        print("Error: Minimum should be over 1.")
        return []

    if not (maximum <= 1000):
        print("Error: Maximum should be up to a 1000.")
        return []

    if not (minimum < maximum):
        print("Error: Range is inverted.")
        return []

    if quantity > (maximum - minimum + 1):
        print("Error: Quantity is to big for selected rnge.")
        return []

    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(minimum, maximum))

    return sorted(list(numbers_set))


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)
