from os import write
a = 0
file_data = {
    "0": "inventory_data/0slot.txt",
    "1": "inventory_data/1slot.txt",
    "2": "inventory_data/2slot.txt",
    "3": "inventory_data/3slot.txt",
    "4": "inventory_data/4slot.txt",
    "5": "inventory_data/5slot.txt",
    "6": "inventory_data/6slot.txt",
    "7": "inventory_data/7slot.txt",
    "8": "inventory_data/8slot.txt",
    "9": "inventory_data/9slot.txt"
}

def open_inventory():
    for i in file_data:
        file = open(file_data[i], "r")
        print(f"{i}-ый Слот: {file.read()}")
        file.close()

action_ask = input("Выберите действие:\n 1) Открыть инвентарь\n")
check_inventory = input("Ты хочешь открыть инвентарь? Ответ принимается только в 'y' или 'n':")

if check_inventory == "y":
    for i in file_data:
        file = open(file_data[i], "r")
        print(f"{i}-ый Слот: {file.read()}")
        file.close()

action_ask1 = input("Выберите действие:\n 1) Изменить данные\n")
change_inventory = input("Ты хочешь сделать действие с каким то слотом? Ответ принимается только в 'y' или 'n':")

if change_inventory == "y":
    slot_number = input("Введите слот с которым хотите произвести действие, Поддерживается только цифра:")
    slot_action = input("Выберите действие:\n 1) Изменить данные\n")
    if slot_action == "1":
        file = open(file_data[slot_number], "w")
        file.write(input("Введите данные:"))
        print("Данные успешно изменены!")
    else:
        print("Перезапустите программу, и следуйте инструкции программы")
elif change_inventory == "n":
    print("Хорошо")
else:
    print("Ответ принимается только 'y' или 'n', Перезапустите программу")