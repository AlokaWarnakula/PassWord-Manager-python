import random


class PasswordGenerator:
    def __init__(self):
        self.letters = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        self.numbers = [str(i) for i in range(10)]
        self.special_characters = [
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=',
            '[', ']', '{', '}', '|', ';', ':', ',', '.', '/', '?', '<', '>', '_'
        ]

    def get_password(self, letter_count, number_count, special_char_count):
        shuffle_list = []

        for _ in range(letter_count):
            shuffle_list.append(random.choice(self.letters))
        for _ in range(number_count):
            shuffle_list.append(random.choice(self.numbers))
        for _ in range(special_char_count):
            shuffle_list.append(random.choice(self.special_characters))
        random.shuffle(shuffle_list)
        return ''.join(shuffle_list)

# Example usage:
# pg = PasswordGenerator()
# password = pg.get_password(5, 3, 2)
# print("Generated password:", password)
