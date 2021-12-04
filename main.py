import discord
from discord import channel
from discord.ext import commands
from discord.utils import get
import os
import csv
import edit_channels

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="e.", intents=intents)

emojiLetters = [
    "\U00000031\U0000FE0F\U000020E3",
    "\U00000032\U0000FE0F\U000020E3",
    "\U00000033\U0000FE0F\U000020E3",
    "\U00000034\U0000FE0F\U000020E3",
    "\U00000035\U0000FE0F\U000020E3",
    "\U00000036\U0000FE0F\U000020E3",
    "\U00000037\U0000FE0F\U000020E3",
    "\U00000038\U0000FE0F\U000020E3",
    "\U00000039\U0000FE0F\U000020E3",
    "\U0001F51F",
    "\N{REGIONAL INDICATOR SYMBOL LETTER A}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER B}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER C}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER D}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER E}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER F}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER G}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER H}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER I}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER J}",
]

@bot.command(rest_is_raw=True)
async def post(ctx: commands.Context, *, arg:str):
    if ctx.message.channel.id in (edit_channels.get_channels_list()[0] + edit_channels.get_channels_list()[1])  and ctx.message.author.id!=909733705210265600: # Проверяем, что бы сообщение не было от бота(для того что бы не было вечного цикла)
        for i in edit_channels.get_linked_channels(ctx.message.channel.id): # Применяем для каждого канала
            c = bot.get_channel(i) # Получаем канал
            print(c.guild)
            await c.send(f"[Переслано из \"{ctx.message.guild.name}\"]\n" + arg)
    
@bot.command()
async def get_stat(ctx:commands.Context, verbose="F"):
    if ctx.message.author.id==548820288616398858 or ctx.message.author.id==302734324648902657:
        await ctx.message.channel.send("Собираем статистику...")
        await ctx.message.delete()
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

            if verbose=="F":
                message_text = f'Всего {member_count} участников в {guild_count} серверах.\n' \
                            f'Список серверов: {", ".join(guild_names)}'

            if verbose in ["Y", "T", "Yes", "True", "On"]:
                server_names_work = []
                server_names_announcments = []
                for id in edit_channels.get_channels_list()[0]:
                    channel = await bot.fetch_channel(id)
                    server_names_work.append(channel.guild.name)
                for id in edit_channels.get_channels_list()[1]:
                    channel = await bot.fetch_channel(id)
                    server_names_announcments.append(channel.guild.name)

                message_text = f'Всего {member_count} участников в {guild_count} серверах.\n' \
                            f'Список серверов: {", ".join(guild_names)}\n' \
                                f'Сервера с каналом работы: {", ".join(server_names_work)}\n' \
                                    f'Сервера с каналом объявлений: {", ".join(server_names_announcments)}'
        await ctx.message.channel.send(message_text, file=discord.File('users.csv'))
        await discord.DMChannel.send(user, content=message_text, file=discord.File('users.csv'))


#@bot.event
#async def on_message(msg: discord.Message): 
#
#    elif msg.content=="e.get_stat" and (msg.author.id==548820288616398858 or msg.author.id==302734324648902657):
#        await msg.channel.send("Собираем статистику...")
#        await msg.delete()
#        with open('users.csv', 'w', encoding='utf-8') as file:
#            writer = csv.writer(file)
#            userdata = []
#            guild_count = len(bot.guilds)
#            member_count = 0
#            guild_names = []
#            for guild in bot.guilds:
#                guild_names.append(guild.name)
#                member_count += guild.member_count
#                for member in guild.members:
#                    username = str(member)
#                    when_created_joined = f"{member.created_at}#{member.joined_at}"
#                    data = [guild.id, guild.name, member.id, username, when_created_joined]
#                    userdata.append(data)
#            writer.writerows(userdata)
#            user = await bot.fetch_user(302734324648902657)
#            message_text = f'Всего {member_count} участников в {guild_count} серверах.\n' \
#                           f'Список серверов: {", ".join(guild_names)}'
#        await msg.channel.send(message_text, file=discord.File('users.csv'))
#        await discord.DMChannel.send(user, content=message_text, file=discord.File('users.csv'))
#    elif msg.content == "e.poll":
#        if msg.reference:
#            message_poll = await  msg.channel.fetch_message(id=msg.reference.message_id)  # получить сообщение
#            text = message_poll.content
#            reactions_amount = len(text.split('\n'))
#            if reactions_amount <= 20:
#                for reaction in emojiLetters[:reactions_amount]:
#                    await message_poll.add_reaction(emoji=reaction)
#            else:
#                await msg.channel.send('Слишком много вариантов. Максимум 20')
#        else:
#            await msg.channel.send("Нужно ответить на существующее сообщение")
#    elif msg.content=="e.poll_check":
#        if msg.reference:
#            msg_poll = await msg.channel.fetch_message(id=msg.reference.message_id)  # получить сообщение
#            msg_reactions = msg_poll.reactions  # получить список реакций
#            if len(msg_reactions) == 0:
#                await msg.channel.send('На сообщении нет реакций')
#            else:
#                reactions = []
#                user_list = []
#                for reaction in msg_reactions:
#                    buff_users_list = []
#                    async for user in reaction.users():  # получить список отреагироваших юзеров
#                        buff_users_list.append(user)
#                    buff_reactions = [reaction.emoji, buff_users_list]
#                    reactions.append(buff_reactions)
#                    for user in buff_users_list:
#                        if user.id != 909733705210265600:  # ID бота
#                            user_list.append(user.id)
#
#                for_stack = lambda array: sorted(list(set([x for x in array if array.count(x) > 1])))  # отсортировать повторы
#                user_list = for_stack(user_list)  # список с юзерами проголосовавшими >1 раза
#
#                # удаление реакций
#                for reaction in msg_reactions:
#                    for user_id in user_list:
#                        await msg_poll.remove_reaction(reaction, await bot.fetch_user(user_id))
#
#                # Отправить сообщение в ЛС автору голосования (тому, на чье сообщение вызвали голосование)
#                if len(user_list):
#                    buff_users_list = []
#                    for user_id in user_list:
#                        user = await bot.fetch_user(user_id)
#                        buff_users_list.append(f'{user.name}#{user.discriminator} | ID: {user.id}')
#                    await discord.DMChannel.send(msg_poll.author, content='Пользователи, проголосовавшие больше одного раза: ' +
#                                                                    ', '.join(buff_users_list))
#        else:
#            await msg.channel.send("Нужно ответить на существующее сообщение")
#



bot.run(os.environ["TOKEN"])