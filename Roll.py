from random import randint


class Roll:

    def __init__(self, input):
        self.input = self.remove_space(input)
        self.bonus = self.get_bonus()
        self.dice = self.get_dice()
        self.roll_values = self.roll_values()
        self.sum = self.get_sum()

    def remove_space(self, input):
        input = input.lower().replace(' ', '')
        return input

    def get_bonus(self):
        if '+' not in self.input:
            return 0
        else:
            bonus = self.input.split('+')[1]
            return bonus

    def get_dice(self):
        split_input = self.input.split('+')[0]
        rolls = split_input.split('d')
        return rolls

    def roll_values(self):
        roll_values = []
        for dice in range(0, int(self.dice[0])):
            roll_values.append((randint(1, int(self.dice[1]))))
        return roll_values

    def get_sum(self):
        total = sum(self.roll_values) + int(self.bonus)
        return total

    def format_rolls(self):
        string_rolls = list(map(str, self.roll_values))
        values = list(' + '.join(string_rolls))
        values = ''.join(values)
        values = "({0})".format(values)

        if self.bonus:
            values += " + {0} = {1}".format(self.bonus, self.sum)
        else:
            values += " = {0}".format(self.sum)
        return values

    def print_sum(self):
        if len(self.roll_values) == 1 and self.bonus == 0:
            return self.sum
        elif len(self.roll_values) == 1 and self.bonus:
            return "{0} + {1} = {2}".format(self.roll_values[0], self.bonus, self.sum)
        else:
            return self.format_rolls()
