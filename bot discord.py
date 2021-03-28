# imports
import discord
from discord.ext import commands
# this library allows you to make a frame to the left of the message
# for color you can use HEX colors with the addition of a prefix "0x"
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord.utils import get

Bot = commands.Bot(command_prefix = "!")
client = discord.Client()

prog = 'Программист'
noob = 'Начинающий'
geymer = 'Геймер'

class MyClient(discord.Client):
    # displays the message "Bot connection!" when the bot is online
    async def on_ready(self):
        # bot connection
        print('Bot connection!')

    @Bot.event
    @client.event
    async def on_message(self, message):

        # displays server rules
        if message.content == '!правила':
            embed = discord.Embed(title='''Правила:
    1) быть активным
    2) не токсичить и не оскарблять кого-либо
    3) и так далее
            ''', color=0xFF0000)
            await message.channel.send(embed=embed)

        # outputs server commands
        if message.content == '!команды':
            embed = discord.Embed(title='''Команды:
    1) !правила - выводит правила сервера 
    2) дай роль: "название роли" - дает роль автору сообщения 
    3) удали роль: "название роли" - удаляет роль у автора сообщения
    4) два сектретных сообщения от бота)
                    ''', color=0xfcf403)
            await message.channel.send(embed=embed)

        if 'барак' in message.content:
            await message.reply('Обама', mention_author=True)

        # adds a role to the author of the message.
        # If the author of the post already has this role, then the bot warns about this
        if message.content == 'дай роль: Программист':

            if get(message.author.roles, id=823093564211986462):
                embed = discord.Embed(title="У вас уже есть такая роль!", color=0x0000FF)
                await message.channel.send(embed=embed)

            else:
                embed = discord.Embed(title=f"Дана роль: {prog}.", color=0x00ff40)
                await message.channel.send(embed=embed)
                await message.author.add_roles(discord.utils.get(message.guild.roles, id=823093564211986462))

        elif message.content == 'дай роль: Начинающий':

            if get(message.author.roles, id=821727656877097073):
                embed = discord.Embed(title="У вас уже есть такая роль!", color=0x0000FF)
                await message.channel.send(embed=embed)

            else:
                embed = discord.Embed(title=f"Дана роль: {noob}", color=0x00ff40)
                await message.channel.send(embed=embed)
                await message.author.add_roles(discord.utils.get(message.guild.roles, id=821727656877097073))

        elif message.content == 'дай роль: Геймер':

            if get(message.author.roles, id=821727553159954432):
                embed = discord.Embed(title="У вас уже есть такая роль!", color=0x0000FF)
                await message.channel.send(embed=embed)

            else:
                embed = discord.Embed(title=f"Дана роль: {geymer}", color=0x00ff40)
                await message.channel.send(embed=embed)
                await message.author.add_roles(discord.utils.get(message.guild.roles, id=821727553159954432))

        # removes the role from the author of the post.
        # If he does not have this role, then the bot warns about this.
        if message.content == 'удали роль: Геймер':

            if get(message.author.roles, id=821727553159954432):
                role = get(message.author.guild.roles, id=821727553159954432)
                embed = discord.Embed(title=f"Удаленна роль: {geymer}.", color=0x20B2AA)
                await message.channel.send(embed=embed)
                await message.author.remove_roles(role, reason=None)

            else:
                embed = discord.Embed(title="У вас нету данной роли!", color=0x0000FF)
                await message.channel.send(embed=embed)

        if message.content == 'удали роль: Начинающий':

            if get(message.author.roles, id=821727656877097073):
                role = get(message.author.guild.roles, id=821727656877097073)
                embed = discord.Embed(title=f"Удаленна роль: {noob}.", color=0x20B2AA)
                await message.channel.send(embed=embed)
                await message.author.remove_roles(role, reason=None)

            else:
                embed = discord.Embed(title="У вас нету данной роли!", color=0x0000FF)
                await message.channel.send(embed=embed)

        if message.content == 'удали роль: Программист':

            if get(message.author.roles, id=823093564211986462):
                role = get(message.author.guild.roles, id=823093564211986462)
                embed = discord.Embed(title=f"Удаленна роль: {prog}.", color=0x20B2AA)
                await message.channel.send(embed=embed)
                await message.author.remove_roles(role, reason=None)

            else:
                embed = discord.Embed(title="У вас нету данной роли!", color=0x0000FF)
                await message.channel.send(embed=embed)

        if 'ам' in message.content:
            await message.reply('ogus', mention_author=True)


# bot launch
client = MyClient()
client.run('TOKEN')