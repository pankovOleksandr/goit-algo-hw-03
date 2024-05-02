import random

def get_numbers_ticket(min, max, quantity):
    try:
        if min < 1:
            raise ValueError("Min number should more than 1")
        if max > 1000:
            raise ValueError("Max number should less than 1000")
        if min > max:
            raise ValueError("Min number should be less or equal to max number")
        
        ticket_numbers = random.sample(range(min, max+1), k=quantity)
        ticket_numbers.sort()
        return ticket_numbers
    except ValueError as error:
        print(f"{error}")
        return []

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)