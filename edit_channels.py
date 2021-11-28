def get_channels_list(): #Просто получить все каналы из файла
    with open("channels.txt", "r") as file:
        lines = file.readlines()
        return [list(map(int, lines[0].split())),  list(map(int, lines[1].split()))] #! 1 - Работа, 2 - объявления
def get_linked_channels(id):  # Получить все каналы, кроме заданного(то есть каналы, в которые нужно пересылать)
    res = get_channels_list()
    if id in res[0]:
        res[0].remove(id)
        return res[0]
    else: 
        res[1].remove(id)
        return res[1]
def add_channel(id): #Добавить канал
    with open("channels.txt", "a") as file:
        file.write(" "+ str(id))

print(get_linked_channels(908658239942574102))