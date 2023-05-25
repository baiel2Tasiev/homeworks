Janysh, [22.05.2023 18:00]
import random

total_rounds = 0

class GameEntity:
    def __init__(self, name, health, damage) -> None:
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name
    
    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value
    
    def __str__(self) -> str:
        return f'{self.name} health: {self.health} [{self.damage}]'
    

class Boss(GameEntity):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage)
    
    def hit(self, heroes: list):
        for hero in heroes:
            if hero.health > 0 and self.health > 0:
                hero.health -= self.damage

    def __str__(self) -> str:
        return "BOSS " + super().__str__()

class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability) -> None:
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    @super_ability.setter
    def super_ability(self, value):
        self.__super_ability = value
    
    def hit(self, boss: Boss):
        if boss.health > 0 and self.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss: Boss, heroes: list):
        pass

class Medic(Hero):
    def __init__(self, name, health, damage, heal_point) -> None:
        super().__init__(name, health, damage, "HEAL")
        self.__heal_point = heal_point

    def apply_super_power(self, boss: Boss, heroes: list):
        print(f"Medic: {self.name} heal {self.__heal_point}")
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_point

class Berserk(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, "Part Damage")
    
    def apply_super_power(self, boss: Boss, heroes: list):
        coef = random.randint(0, 50)
        boss.health -= self.damage - coef
        print(f"Warrior {self.name} hits Part Damage : {boss.damage - coef}\n")

class Golem(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, "BLOCK")

    def apply_super_power(self, boss: Boss, heroes: list):
        for hero in heroes:
            if hero.health > 0 and self.health > 0:
                self.health -= boss.damage * 0.2
                hero.health += boss.damage * 0.2
            if hero.health <= 0 and self.health <= 0:
                self.health *= 0
                hero.health *= 0
        print("Голем погасил урон от босса")
        

def is_game_finished(boss: Boss, heroes):
    if boss.health <= 0:
        print("Heroes WON!")
        return True

    all_heroes_dead = True
    for hero in heroes:
        if int(hero.health) > 0:
            all_heroes_dead = False
    
    if all_heroes_dead:
        print("Boss WON!")

    return all_heroes_dead
    

def print_statistic(boss: Boss, heroes):
    print(f"___________{total_rounds} Round___________")
    print(boss)
    for hero in heroes:
        print(hero)


def heroes_power(boss: Boss, heroes: list):
    boss_ability = random.choice([" "])
    print(f"Boss {boss.name} blocked {boss_ability}")
    for hero in heroes:
        if boss_ability != hero.super_ability and boss.health > 0 and hero.health > 0:
            hero.apply_super_power(boss, heroes)


def play_round(boss: Boss, heroes: list):
    print_statistic(boss, heroes)
    global total_rounds
    total_rounds += 1
    boss.hit(heroes)
    for hero in heroes:
        hero.hit(boss)
    heroes_power(boss, heroes)

Janysh, [22.05.2023 18:00]


def main():
    boss = Boss("Nurbolot", 2000, 50)
    berserk = Berserk("Berserk", 400, 50)
    golem = Golem("Голем", 1000, 15)
    medic = Medic("LOK", 300, 0, 0)


    heroes = [berserk, golem, medic]

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)
    
    print_statistic(boss, heroes)


main()