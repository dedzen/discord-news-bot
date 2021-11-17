def get_channels_list(): #Просто получить все каналы из файла
    with open("channels.txt", "r") as file:
        return list(map(int, file.readline().split()))
def get_linked_channels(id):  # Получить все каналы, кроме заданного(то есть каналы, в которые нужно пересылать)
    res = get_channels_list()
    res.remove(id)
    return res
def add_channel(id): #Добавить канал
    with open("channels.txt", "a") as file:
        file.write(" "+ str(id))
