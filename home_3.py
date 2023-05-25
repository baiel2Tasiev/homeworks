class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __str__(self):  
        return f"лимит: {self.__cpu}, симит: {self.__memory}"        

    def get_cpu(self):
        return self.__cpu

    def get_memory(self):
        return self.__memory

    def set_cpu(self, cpu):
        self.__cpu = cpu
        print("Set:", self.__cpu)

    def set_memory(self, memory):
        self.__memory = memory
        print("Set:", self.__memory)

    def make_computations(self):
        return f"{self.__cpu}, {self.__memory}"

    def __eq__(self, other):
        return self.__cpu == other.__cpu and self.__memory == other.__memory
    
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        return self.__cpu < other.__cpu and self.__memory < other.__memory
    
    def __gt__(self, other):
        return self.__cpu > other.__cpu and self.__memory > other.__memory
    
    def __le__(self, other):
        return self.__cpu <= other.__cpu and self.__memory <= other.__memory
    
    def __ge__(self, other):
        return self.__cpu >= other.__cpu and self.__memory >= other.__memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = [sim_cards_list]
    
    def __str__(self):
        return f"Симкарта: {self.__sim_cards_list[-1]}"

    def get_sim(self):
        return self.__sim_cards_list

    def call(self, sim_card_number, call_to_number):
        if sim_card_number == 1:
            return f"Идет поиск номера {call_to_number} с сим-карты-1 - Beel"
        elif sim_card_number == 2:
            return f"Идет звонок на номер {call_to_number} с сим-карты-2 - O!"
        elif sim_card_number == 3:
            return f"Идет звонок на номер {call_to_number} с сим-карты-3 - Megaffon"
        else:
            print("Не правильно")
    
class Smartphone(Computer, Phone):
    
    def __init__(self, cpu, memory):
        super().__init__(cpu, memory)

    def __str__(self):
        return super().__str__()

    def use_gps(self, location):
        print(f"Ищем маршрут до локации: {location}")

pc = Computer("Intel core-i9", "32 GB")
pc2 = Computer("AMD Ryzen 7", "64 GB")
print(pc)
print("Лимит:", pc.get_cpu())
print("Симимт:", pc.get_memory())
pc.set_cpu("AMD Ryzen-7")
pc.set_memory("64 GB")
print(pc.make_computations())

print(pc == pc2)
print(pc != pc2)
print(pc < pc2)
print(pc > pc2)
print(pc <= pc2)
print(pc >= pc2)


phone = Phone("Beel, O!, Megaffon")
print(phone)
phone.get_sim()
phone._Phone__sim_cards_list
print(phone.call(1, '+99674353544545354547'))
print(phone.call(2, '+99670654543545354353'))
print(phone.call(3, '+99650535345345433788'))

smart = Smartphone("1 параметр", "2 параметр")
print(smart)
smart.use_gps("Юго-Восток")