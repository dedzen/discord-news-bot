import discord
from discord.ext import commands
import os
import csv
import edit_channels

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="e.", intents=intents)
bot.remove_command("help")


@bot.event
async def on_message(msg): 
    if msg.channel.id in edit_channels.get_channels_list() and msg.author.id!=909733705210265600: # Проверяем, что бы сообщение не было от бота(для того что бы не было вечного цикла)
        for i in edit_channels.get_linked_channels(): # Применяем для каждого канала
            c = bot.get_channel(i) # Получаем канал
            await c.send(f"[Переслано из \"{msg.guild.name}\"]\n" + msg.content)

    elif msg.content=="e.get_stat" and (msg.author.id==548820288616398858 or msg.author.id==302734324648902657):
        await msg.channel.send("Собираем статистику...")
        await msg.delete()
        with open('users.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            userdata = []
            guild_count = len(bot.guilds)
            member_count = 0
            guild_names = []
            for guild in bot.guilds:
                guild_names.append(guild.name)
                member_count += guild.member_count
                for member in guild.members:
                    username = str(member)
                    when_created_joined = f"{member.created_at}#{member.joined_at}"
                    data = [guild.id, guild.name, member.id, username, when_created_joined]
                    userdata.append(data)
            writer.writerows(userdata)
            user = await bot.fetch_user(302734324648902657)
            message_text = f'Всего {member_count} участников в {guild_count} серверах.\n' \
                           f'Список серверов: {", ".join(guild_names)}'
        await msg.channel.send(message_text, file=discord.File('users.csv'))
        await discord.DMChannel.send(user, content=message_text, file=discord.File('users.csv'))


bot.run(os.environ["TOKEN"])