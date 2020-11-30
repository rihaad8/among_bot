import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
from UserHandling import User
from UserHandling import UserList

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix="!")

global USERSTOCK
USERSTOCK = UserList.UserList()
USERSTOCK.loadListFromFile()

global COLORS
COLORS = ["red", "dark_blue", "dark_green", "pink", "orange", "yellow", "black", "white", "purple", "brown", "light_blue", "light_green"]

global MAPS
MAPS = ["Mira-HQ", "The Skeld", "Polus"]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def m(ctx):
    voice_channel = ctx.author.voice.channel
    for member in voice_channel.members:
        if (member.name == "Rythm"):
            await member.edit(mute=False)
        else:
            await member.edit(mute=True)

@client.command()
async def u(ctx):
    voice_channel = ctx.author.voice.channel

    for member in voice_channel.members:
        if (member.name == "Rythm"):
            await member.edit(mute=True)
        else:
            await member.edit(mute=False)

@client.command()
async def map(ctx):
    mapChoice = sorted(MAPS, key=lambda k: random.random())
    await ctx.send("Diese Runde spielen wir: {}".format(mapChoice[0]))

@client.command()
async def wish1(ctx, args):
    await ctx.send("Hey {}, hast dir {} als erste Option gewünscht.".format(ctx.author.name,args))
    userNameList = USERSTOCK.getNameList()
    if(not ctx.author.name in userNameList):
        USERSTOCK.addUser(User.User(ctx.author.name, "", "", "", 0))
    for user in USERSTOCK.users:
        if (ctx.author.name == user.name):
            user.color_wish1 = args
    USERSTOCK.saveListToFile()

@client.command()
async def wish2(ctx, args):
    await ctx.send("Hey {}, hast dir {} als zweite Option gewünscht.".format(ctx.author.name,args))
    userNameList = USERSTOCK.getNameList()
    if(not ctx.author.name in userNameList):
        USERSTOCK.addUser(User.User(ctx.author.name, "", "", "", 0))
    for user in USERSTOCK.users:
        if (ctx.author.name == user.name):
            user.color_wish2 = args
    USERSTOCK.saveListToFile()

@client.command()
async def wish3(ctx, args):
    await ctx.send("Hey {}, hast dir {} als dritte Option gewünscht.".format(ctx.author.name,args))
    userNameList = USERSTOCK.getNameList()
    if(not ctx.author.name in userNameList):
        USERSTOCK.addUser(User.User(ctx.author.name, "", "", "", 0))
    for user in USERSTOCK.users:
        if (ctx.author.name == user.name):
            user.color_wish3 = args
    USERSTOCK.saveListToFile()

@client.command()
async def wish_info(ctx):
    for user in USERSTOCK.users:
        if (ctx.author.name == user.name):
            if not(user.color_wish1 == ""):
                myWish1 = user.color_wish1
            else:
                myWish1 = "kein erster Wunsch festgelegt"
            if not(user.color_wish2 == ""):
                myWish2 = user.color_wish2
            else:
                myWish2 = "kein zweiter Wunsch festgelegt"
            if not(user.color_wish3 == ""):
                myWish3 = user.color_wish3
            else:
                myWish3 = "kein dritter Wunsch festgelegt"
    await ctx.send("Du kannst dir bis zu 3 Farben wünschen. Dazu nutze !wish1, !wish2 oder !wish3. \n 1. Wunsch: {} \n 2. Wunsch: {} \n 3. Wunsch: {} \n Folgende Farben sind möglich: \n {} \n Beispiel-Syntax: !wish1 dark_blue".format(myWish1, myWish2, myWish3, COLORS))
    USERSTOCK.saveListToFile()

@client.command()
async def get_colors(ctx):
    activeUsers = []
    takenColors = [""]
    availableColors = COLORS
    voice_channel = ctx.author.voice.channel
    for member in voice_channel.members:
        activeUsers.append(member.name)
    randUsers = sorted(USERSTOCK.users, key=lambda k: random.random())

    for user in randUsers:
        if(user.name in activeUsers):
            if not(user.color_wish1 in takenColors):
                await ctx.send("{} deine Farbe für heute ist deine erste Wahl: {}".format(user.name, user.color_wish1))
                takenColors.append(user.color_wish1)
            elif not(user.color_wish2 in takenColors):
                await ctx.send("{} deine Farbe für heute ist deine zweite Wahl: {}".format(user.name, user.color_wish2))
                takenColors.append(user.color_wish2)
            elif not(user.color_wish3 in takenColors):
                await ctx.send("{} deine Farbe für heute ist deine dritte Wahl: {}".format(user.name, user.color_wish3))
                takenColors.append(user.color_wish3)
            else:
                await ctx.send("{}, leider sind deine gewünschten Farben alle bereits vergeben bzw. hast du keine gewählt.")
    leftColors = [color for color in availableColors if color not in takenColors]
    await ctx.send("Freie Farben: {}".format(leftColors))

@client.command()
async def commands(ctx):
    await ctx.send("Command List: \n !m Schaltet alle Teilnehmer-innen in dem Voice Channel in dem Du dich befindest stumm. \n !u Schaltet alle Teilnehmer-innen in dem Voice Channel in dem Du dich befindest laut.\n !get_colors -> Verteilt die Character Farben für die nächste Runde nach den mit !wish gewünschnten Farben. \n !wish1 -> legt den Wunsch erster Priorität fest \n !wish2 -> legt den Wunsch zweiter Priorität fest \n !wish3 -> legt den Wunsch dritter Priorität fest \n !wish_info -> Alles Infos zu deinen wishes \n !map -> Wählt zufällig eine Map aus")
client.run(TOKEN)
