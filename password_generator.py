import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters= 8
    nr_symbols = 4
    nr_numbers = 4
    letter_sum = nr_letters + nr_symbols + nr_numbers
    position = [i for i in range(0, letter_sum)]
    password_list = [0 for _ in range(0, letter_sum)]

    for i in range(0, letter_sum):
        if i < nr_letters:
            cell = random.choice(position)
            password_list[cell] = random.choice(letters)
            position.remove(cell)
        elif i < nr_letters + nr_symbols:
            cell = random.choice(position)
            password_list[cell] = random.choice(symbols)
            position.remove(cell)		
        else:
            cell = random.choice(position)
            password_list[cell] = random.choice(numbers)
            position.remove(cell)
    return ''.join(password_list)