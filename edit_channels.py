def get_channels_list(): #Просто получить все каналы из файла
    with open("channels.txt", "r") as file:
        lines = file.readlines()
        return [list(map(int, line.split())) for line in lines] #! 1 - Работа, 2 - объявления, 3 - флудилка
def get_linked_channels(id):  # Получить все каналы, кроме заданного(то есть каналы, в которые нужно пересылать)
    res = get_channels_list()
    for i in res:
        if id in i: 
            i.remove(id)
            return i
