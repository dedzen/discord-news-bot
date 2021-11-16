import discord
from discord.ext import commands
import os
import csv

intents = discord.Intents.default()
intents.members = True
links={909732611621023774:[909732849333194762],
        909732849333194762:[909732611621023774],
        910178688698552351:[910177947497951252],
        910177947497951252:[910178688698552351]} #Список новостных каналов, и куда они должны перенаправлятся
bot = commands.Bot(command_prefix="e.", intents=intents) #Префикс пока не используется
bot.remove_command("help")


@bot.event
async def on_message(msg): 
    if msg.channel.id in links.keys() and msg.author.id!=909733705210265600: # Проверяем, что бы сообщение не было от бота(для того что бы не было вечного цикла)
        for i in links[msg.channel.id]: # Применяем для каждого канала
            c = bot.get_channel(i) # Получаем канал
            await c.send(f"[Переслано из \"{msg.guild.name}\"]\n" + msg.content)
@bot.command
async def get_stat(msg): #Никто не знает что тут творится, я этого не писал
    with open('users.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        userdata = []
        guild_count = len(bot.guilds)
        member_count = 0
        for guild in bot.guilds:
            member_count += guild.member_count
            for member in guild.members:
                username = f'{member.name}#{member.discriminator}'
                data = [guild.id, guild.name, member.id, username]
                userdata.append(data)
        writer.writerows(userdata)
bot.run(os.environ["TOKEN"])