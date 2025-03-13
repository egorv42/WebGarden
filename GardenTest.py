from threading import Thread
from time import sleep

pot = {
    "sun":10,
    "water":250,
    "element":50,
}

plant = {
    "light_max":10,
    "light_min":20,
    "water":10,
    "element":5,
}

class Main: # Главная функция
    def __init__(self):
        self.pot = {}
        self.plant = {}
    
    def live_cycle(self, pot, plant): # Жизненый цикл растения
        # Проверка элементов в горшке
        while pot["water"] >= plant["water"] and pot["element"] >= plant["element"] and plant["light_max"] <= pot["sun"] and plant["light_min"] >= pot["sun"]:
            pot["water"] -= plant["water"]
            pot["element"] -= plant["element"]
            sleep(5)
            # print(pot["water"], " вода")
            # print(pot["element"], "element")
        print("Plnt is death")
        
    
    def Terminal(self, pot, plant): # Взаимодействие с приложением
        while True:
            # Главное меню терминала
            menu = input("Enter your request:\n1 - Info\n2 - Add\n3 - change\n")
            
            if menu == "1":  # Информация об горшке
                print("Info:\n",
                    f"Sun - {pot['sun']}\n",
                    f"Water - {pot['water']}\n",
                    f"Element - {pot['element']}\n",)
                
            elif menu == "2": # Добавление элементов в горшок
                Add_choice = input("What do you want to add\n1 - Water\n2 - Element\n")
                if Add_choice == "1":
                    pot['water'] += int(input("Enter the number\n"))
                elif Add_choice == "2":
                    pot['element'] += int(input("Enter the number\n"))
            elif menu == "3":
                pot['sun'] = int(input("Enter the number\n"))
            
main = Main()

# Потоки
thread1 = Thread(target=main.live_cycle, args=(pot, plant))
thread2 = Thread(target=main.Terminal, args=(pot, plant))

thread1.start()
thread2.start()

thread1.join()
print("Поток 1 завершен")
thread2.join()
print("Поток 2 завершен")







