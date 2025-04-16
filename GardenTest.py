from threading import Thread
from time import sleep

pots = {}
pot_threads = {}

plant1 = {
    "light_max":10,
    "light_min":20,
    "water":10,
    "element":5,
    "max_stage":3,
    "stage_time":30,
}

plant2 = {
    "light_max":15,
    "light_min":30,
    "water":4,
    "element":1,
    "max_stage":5,
    "stage_time":25,
}


class Pot:
    def __init__(self, pot, plant):
        self.pot = pot
        self.plant = plant
        
        
    def LiveCycle(self):
        growth = 0
        while (self.pot["water"] >= self.plant["water"] and
               self.pot["element"] >= self.plant["element"] and
               (self.pot["sun"] >= self.plant["light_max"] and
               self.pot["sun"] <= self.plant["light_min"])):
            self.pot["water"] -= self.plant["water"]
            self.pot["element"] -= self.plant["element"]
            if self.pot["stage"] != self.plant["max_stage"]:
                growth += 1
            if growth >= self.plant["stage_time"]:
                growth = 0
                self.pot["stage"] += 1
            sleep(5)
        print("plant dead!")

def Terminal():
    while True:
        # Главное меню терминала
        menu = input("Enter your request:\n"
                     "1 - Info\n"
                     "2 - Add\n"
                     "3 - change\n"
                     "4 - Create new pot\n")
        
        if menu == "1":  # Информация об горшке
            pot_name = input("Enter pot name:\n")
            pot_info = pots.get(pot_name)
            if pot_info:
                print("Info:\n"
                    f"Sun - {pot_info.pot['sun']}\n"
                    f"Water - {pot_info.pot['water']}\n"
                    f"Element - {pot_info.pot['element']}\n"
                    f"Plant - {pot_info.pot['plant']}\n"
                    f"Stage - {pot_info.pot['stage']}\n")
            else:
                print("Pot not found")
        
        elif menu == "2": # Добавление элементов в горшок
            pot_name = input("Enter pot name:\n")
            pot_info = pots.get(pot_name)
            if pot_info:
                Add_choice = input("What do you want to add\n"
                                   f"1 - Water\n"
                                   f"2 - Element\n")
                if Add_choice == "1":
                    pot_info.pot['water'] += int(input("Enter the number\n"))
                elif Add_choice == "2":
                    pot_info.pot['element'] += int(input("Enter the number\n"))
            else:
                print("Pot not found")
        
        elif menu == "3": # Меняем освещение у горшка
            pot_name = input("Enter pot name:\n")
            pot_info = pots.get(pot_name)
            if pot_info:
                pot.info.pot['sun'] = int(input("Enter the number\n"))
            else:
                print("Pot not found")
        
        elif menu == "4": # Создание нового горшка
            # Выбор имени нового горшка
            new_pot_name = input("Enter name for new pot:\n")
            # Выбор характеристик нового горшка
            new_pot_sun = int(input("Chooice sun level in pot\n"))
            new_pot_water = int(input("Chooice water level in pot\n"))
            new_pot_element = int(input("Chooice element level in pot\n"))
            
            # Выбор растения для нового горшка
            plant_choice = input("Choose plant type:\n"
                                 "1 - Plant1\n"
                                 "2 - plant2\n")
            if plant_choice == "1":
                new_plant = plant1
                plant = "plant1"
            elif plant_choice == "2":
                new_plant = plant2
                plant = "plant2"
            else:
                print("Invalid choice")
                
            new_pot = {
                    "sun":new_pot_sun,
                    "water":new_pot_water,
                    "element":new_pot_element,
                    "plant":plant,
                    "stage":1,
            }
            NewPot = Pot(new_pot, new_plant)
            pots[new_pot_name] = NewPot
            
            # Выделение в отдельный поток
            pot_thread = Thread(target=NewPot.LiveCycle)
            pot_thread.start()
            pot_threads[new_pot_name] = pot_thread
            



# Запуск терминала
ThreadTerminal = Thread(target=Terminal)
ThreadTerminal.start()
ThreadTerminal.join()
