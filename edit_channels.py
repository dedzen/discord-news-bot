def get_channels_list(): #Просто получить все каналы из файла
    with open("channels.txt", "r") as file:
        lines = file.readlines()
        return [list(map(int, lines[0].split())),  list(map(int, lines[1].split())), list(map(int, lines[2].split()))] #! 1 - Работа, 2 - объявления, 3 - флудилка
def get_linked_channels(id):  # Получить все каналы, кроме заданного(то есть каналы, в которые нужно пересылать)
    res = get_channels_list()
    if id in res[0]:
        res[0].remove(id)
        return res[0]
    elif id in res[1]:
        res[0].remove(id)
        return res[1]
    else: 
        res[2].remove(id)
        return res[2]
print(get_channels_list()[2])