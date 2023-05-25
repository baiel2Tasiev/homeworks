import random

numbers = []
for i in range(0, 31):
    numbers.append(i)
my_number = input("Введите ваше число: ")

class Casino:
    def __init__(self, my_money) -> None:
        self.my_money = my_money

    def __str__(self) -> str:
        return {self.my_money}

    def casino(self):
        global numbers
        random_number = random.choice(numbers[::-1])
        global my_number
        if my_number == random_number:
            self.my_money * 2
            print("Вы выиграли x2!!!")
        elif self.my_money != random_number:
            self.my_money * 0
            print("Вы проиграли ваши деньги")