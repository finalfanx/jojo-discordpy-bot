import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import datetime
import random
import os
import pickle
import time

#ПРЕФИКС БОТА (МЕНЯ ЕСЛИ НУЖНО)
bot = commands.Bot(command_prefix='~')

#ПОМЕНЯЙТЕ ЭТИ ЗНАЧЕНИЯ
BOT_TOKEN = "" #ТОКЕН БОТА

#ПОМЕНЯЙТЕ ЭТИ ЗНАЧЕНИЯ
global BOT_ID
BOT_ID = "" #АЙДИ БОТА










bot.remove_command("help")

#Переменные
global muted_all_users
muted_all_users = 0

global ignited_all_users
ignited_all_users = 0

global user_bomb
user_bomb = ""

global sha_bomb
sha_bomb = ""

global star_stop
star_stop = 0

global ripple_id
ripple_id = ""

global ignite_id
ignite_id = ""

global puppet
puppet = ""

global jawed
jawed = ""

global top_speed
top_speed = 0

global barn
barn = ""

global barned
barned = 0

global attackship
attackship = 0

global mutesec
mutesec = 1

global mutesec2
mutesec2 = 2

global skilling
skilling = 0

global hanged
hanged = ""

global canshoot
canshoot = 0

global shooting
shooting = ""

global emp_w
emp_w = ""

global parazit
parazit = ""

global paraziting
paraziting = ""

global word_need
word_need = ""

global justly
justly = ""

global loved
loved = ""

global loving
loving = ""

global charges
charges = 0

global posses
posses = ""

global target
target = ""

global brat
brat = ""

global oblik
oblik = ""

global tooksword
tooksword = ""

global shocked
shocked = ""

global baby
baby = ""

global playing_with
playing_with = ""

global randomnum
randomnum = 0

global randomnum2
randomnum2 = 0

global ready
ready = 0

global ready2
ready2 = 0

global darbi
darbi = ""

global froze
froze = ""

global playcar
playcar = ""

global darbis
darbos = ""

global car1pos
car1pos = 0

global car2pos
car2pos = 0

global carready
carready = 0

global carready2
carready2 = 0

global game_started
game_started = 0

global race
race = ""

global race2
race2 = ""

global voided
voided = ""

global evolving
evolving = 0

global sound
sound = ""

global soundword
soundword = ""

global act2
act2 = 0

global act3freeze
act3freeze = ""

global booked
booked = ""

global bookab
bookab = 0

global watered
watered = ""

global badtarget
badtarget = ""

global voicecharge
voicecharge = 0

global locked
locked = ""

global mon
mon = 0

global maniq
maniq = ""

global mimi
mimi = ""

global lovedel
lovedel = ""

global achtung
achtung = 0

global poisoned
poisoned = 0

global messagoison
messagoison = ""

global harvatiya
harvatiya = 0

global changenickcan
changenickcan = ""

global bites_dust
bites_dust = ""

global rps
rps = ""

global player1choose
player1choose = ""

global player2choose
player2choose = ""

global readyplay
readyplay = ""

global choosed
choosed = ""

global readyplayer1
readyplayer1 = 0

global readyplayer2
readyplayer2 = 0

global randomrock
randomrock = ""

global randompaper
randompaper = ""

global randomscissors
randomscissors = ""

global randomrock2
randomrock2 = ""

global randompaper2
randompaper2 = ""

global randomscissors2
randomscissors = ""

global reflecting
reflecting = ""

global wutface
wutface = ""

global degrod
degrod = ""

global highw
highw = ""

global zeroed
zeroed = ""

global zipped_channel
zipped_channel = ""

global zipped
zipped = ""

global recording
recording = ""

global wrec
wrec = ""

global aero
aero = 0

global virus
virus = ""

global virus_S
virus_S = 0

global currentHour
currentHour = 0

global littled
littled = ""

global meme
meme = ""

global zerkal_kanal
zerkal_kanal = ""

global hidden
hidden = ""

global hooked
hooked = 0

global aging
aging = ""

global muting
muting = 0

global iceduser
iceduser = ""

global ici
ici = 0

global user_lie
user_lie = ""

global lie_word
lie_word = ""

global lie_to
lie_to = ""

global invisiblity
invisiblity = ""

global molded
molded = ""

global molding
molding = ""

global stoned
stoned = ""

global nitka
nitka = ""

global ghost
ghost = ""

global invade
invade = ""

global invading
invading = ""

global weather
weather = 0

global dcharge
dcharge = 1

global disc
disc = ""

global disced
disced = ""

global discmute
discmute = 0

global gravitied
gravitied = 0

global evolvedd
evolvedd = 0

global oi
oi = ""

global spinning
spinning = 0

global spinin
spinin = ""

global spini
spini = 0

global spinner
spinner = ""

global spinenergy
spinenergy = 0

global tickettoride
tickettoride = 0

global takingstand
takingstand = 0

global stealed
stealed = 5

global degrodi
degrodi = 0

global newlife
newlife = ""

global degradations
degradations = 0

global degradations2
degradations2 = 0

global standname
standname = ""

global standability
standability = ""

global standpic
standpic = ""

global ujeusing
ujeusing = 0

global gayporn
gayporn = ""

global stopped_mgs
stopped_mgs = []

global sha_bombe
sha_bombe = ""

global sha_bombe2
sha_bombe2 = ""

global sha_bombe3
sha_bombe3 = ""

global sha_bombe4
sha_bombe4 = ""

global rippleenergy
rippleenergy = 0

global rippleenergy2
rippleenergy2 = 0

global karss
karss = 3

global nextthing
nextthing = ""

async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name='IT JUST WORKS | ~help'))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name='СТИРАНИЕ ВРЕМЕНИ | ~help'.format(len(bot.servers))))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name='ВАЖЕН ТОЛЬКО РЕЗУЛЬТАТ | ~help'.format(len(bot.servers))))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name='ПИДОРАСТИЮ | ~help'.format(len(bot.servers))))
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    print ("---------------\n")
    print ("Дискорд-бот Кира запущен.\n")
    print ("---------------\n")
    print ("Список команд - ~help\n")
    print ("---------------\n\n\n")
    

    bot.loop.create_task(status_task())
   
    
@bot.event
async def on_message_delete(message):
    global invade
    global invading
    if message.author.id == invade:
        invader = discord.Server.get_member(message.server, user_id=invading)
        await bot.send_message(invader, "{} : {}".format(message.author.name, message.content))

#Сообщение
@bot.event
async def on_message(message):
    global shooting
    global canshoot
    global emp_w
    global parazit
    global paraziting
    global word_need
    global justly
    global target
    global oblik
    global brat
    global baby
    global froze
    global sound
    global soundword
    global evolving
    global act3freeze
    global booked
    global bookab
    global locked
    global mon
    global watered
    global lovedel
    global achtung
    global poisoned
    global messagoison
    global harvatiya
    global muted_all_users
    global bites_dust
    global reflecting
    global wutface
    global degrod
    global highw
    global zeroed
    global zipped_channel
    global zipped
    global recording
    global wrec
    global whorec
    global aero
    global star_stop
    global littled
    global hidden
    global aging
    global muting
    global iceduser
    global ici
    global user_lie
    global lie_word
    global lie_to
    global invisiblity
    global molding
    global molded
    global stoned
    global nitka
    global ghost
    global dcharge
    global gravitied
    global evolvedd
    global weather
    global spinner
    global spinin
    global spini
    global tickettoride
    global degrodi
    global newlife
    global gayporn
    global stopped_mgs
    global virus
    global virus_S
    global rippleenergy
    global rippleenergy2
    global BOT_ID
    global nextthing
    global sha_bombe
    global sha_bombe2
    global sha_bombe3
    global sha_bombe4
    
    if "Jonathan Joestar" in (role.name for role in message.author.roles):
        rippleenergy += 1
        
    if "Joseph Joestar" in (role.name for role in message.author.roles):
        rippleenergy2 += 2
    
    if "<@{}>".format(BOT_ID) in message.content: #Упоминание бота
        await bot.send_message(message.channel, "Список доступных команд:\n ``~help``")
        
    if message.author.id == BOT_ID:
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.remove_roles(message.author, mute_role)
        return
        
    if "Kars" in (role.name for role in message.author.roles):
        if "Ultimate" in (role.name for role in message.author.roles):
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.remove_roles(message.author, mute_role)
            
            if message.author.id == parazit:
                parazit = ""
                
            if message.author.id == justly:
                justly = ""
                word_need = ""
                
            if message.author.id == froze:
                froze = ""
                
            if message.author.id == act3freeze:
                act3freeze = ""
            
            if message.author.id == sound:
                sound = ""
            
            if message.author.id == booked:
                booked = ""
                
            if message.author.id == watered:
                watered = ""
                
            if message.author.id == poisoned:
                poisoned = ""
                
            if message.author.id == degrod:
                degrod = ""
                
            if message.author.id == highw:
                highw = ""
                
            if message.author.id == user_lie:
                user_lie = ""
                
            if message.author.id == invisiblity:
                invisiblity = ""
                
            if message.author.id == stoned:
                stoned = ""
                
            if message.author.id == ghost:
                ghost = ""
                
            if message.author.id == littled:
                littled = ""
                
            if message.author.id == zeroed:
                zeroed = ""
                
            if message.author.id == gayporn:
                gayporn = ""
                
            if message.author.id == virus:
                virus = ""
                
            if message.author.id == spinner:
                spinner = ""
                
            if message.author.id == spinin:
                spinin = ""
                
            if message.author.id == spini:
                spini = ""
                
            if message.author.id == aging:
                aging = ""
                
            if message.author.id == hidden:
                hidden = ""
        
    if message.content.lower().replace(",", "").replace(".", "") == nextthing.lower().replace(",", "").replace(".", ""):
        if nextthing != "":
            if message.author.id != BOT_ID:
                await bot.send_message(message.channel, "Вы угадали, что напишет пользователь и получили 100 зарядов хамона.")
                rippleenergy2 += 100
                nextthing = ""
                
    else:
        nextthing = ""
        
    if ici == 1:
        if "White Album" not in (role.name for role in message.author.roles):
            if iceduser == "":
                embed = discord.Embed(title = "{} заморожен.".format(message.author.name), description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/7b/WAGWFirst.jpg/revision/latest/scale-to-width-down/390?cb=20170430040628")
                await bot.send_message(message.channel, embed=embed)
                iceduser = message.author.id
                ici = 0
        
    if ":roflanebalo:" in message.content.lower():
        if "Harvest" not in (role.name for role in message.author.roles):
            harvatiya += 2
            
    if ":wutface:" in message.content.lower():
        if "Enigma" not in (role.name for role in message.author.roles):
            wutface = message.author.id
            
    if ":wutface:" not in message.content.lower():
        if "Enigma" not in (role.name for role in message.author.roles):
            wutface = ""
            
    if "Green Day" in (role.name for role in message.author.roles):
        molding = message.author.id
        
    if "Whitesnake" in (role.name for role in message.author.roles):
        evolvedd += 1
        
        if evolvedd >= 200:
            whitesnake = discord.utils.find(lambda r: r.name == "Whitesnake", message.server.roles)
            await bot.remove_roles(message.author, whitesnake)
            cmoon = discord.utils.find(lambda r: r.name == "C-Moon", message.server.roles)
            await bot.add_roles(message.author, cmoon)
        
            evolvedd = 0
        
    if "C-Moon" in (role.name for role in message.author.roles):
        evolvedd += 1
        
        if evolvedd >= 200:
            cmoon = discord.utils.find(lambda r: r.name == "C-Moon", message.server.roles)
            await bot.remove_roles(message.author, cmoon)
            mih = discord.utils.find(lambda r: r.name == "Made in Heaven", message.server.roles)
            await bot.add_roles(message.author, mih)
        
            evolvedd = 0
        
        
    if "Echoes Egg" in (role.name for role in message.author.roles):
        if evolving == 0:
            
            evolving = 1
            await asyncio.sleep(1800)
        
            evolving = 0
        
            echoes_egg = discord.utils.find(lambda r: r.name == 'Echoes ACT1', message.server.roles)
            await bot.remove_roles(message.author, echoes_egg)
            echoes_act1 = discord.utils.find(lambda r: r.name == 'Echoes ACT1', message.server.roles)
            await bot.add_roles(message.author, echoes_act1)
            echoes_egg = discord.utils.find(lambda r: r.name == 'Echoes ACT1', message.server.roles)
            await bot.remove_roles(message.author, echoes_egg)
        
            embed = discord.Embed(title = "*Первая версия* **Эхо** пробудилась.", description = "*{}, у вас новый Эхо.*".format(message.author.name), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/4b/Echoes_hatches.png/revision/latest/scale-to-width-down/640?cb=20160506192008")
            await bot.send_message(message.channel, embed=embed)
        
    if "Echoes ACT1" in (role.name for role in message.author.roles):
        if evolving == 0:
            evolving = 1
            await asyncio.sleep(1800)
        
            evolving = 0
        
            echoes_act1 = discord.utils.find(lambda r: r.name == 'Echoes ACT1', message.server.roles)
            await bot.remove_roles(message.author, echoes_act1)
            echoes_act2 = discord.utils.find(lambda r: r.name == 'Echoes ACT2', message.server.roles)
            await bot.add_roles(message.author, echoes_act2)
            echoes_act1 = discord.utils.find(lambda r: r.name == 'Echoes ACT1', message.server.roles)
            await bot.remove_roles(message.author, echoes_act1)
        
            embed = discord.Embed(title = "*Вторая версия* **Эхо** пробудилась.", description = "*{}, Эхо эволюционировал.*".format(message.author.name), color = 0xffff00)
            embed.set_image(url=    "https://vignette.wikia.nocookie.net/jjba/images/4/49/EchoesACT2_is_born.png/revision/latest/scale-to-width-down/640?cb=20160527174007")
            await bot.send_message(message.channel, embed=embed)
        
    if "Echoes ACT2" in (role.name for role in message.author.roles):
        if evolving == 0:
            evolving = 1
            await asyncio.sleep(1800)
        
            evolving = 0
        
            echoes_act2 = discord.utils.find(lambda r: r.name == 'Echoes ACT2', message.server.roles)
            await bot.remove_roles(message.author, echoes_act2)
            echoes_act3 = discord.utils.find(lambda r: r.name == 'Echoes ACT3', message.server.roles)
            await bot.add_roles(message.author, echoes_act3)
            echoes_act2 = discord.utils.find(lambda r: r.name == 'Echoes ACT2', message.server.roles)
            await bot.remove_roles(message.author, echoes_act2)
        
            embed = discord.Embed(title = "*Третья версия* **Эхо** пробудилась.", description = "*{}, Эхо эволюционировал.*".format(message.author.name), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/ff/Echoes_ACT3_initial.png/revision/latest/scale-to-width-down/640?cb=20160904163228")
            await bot.send_message(message.channel, embed=embed)
        
    if word_need != "":
        if message.author.id == justly:
            if "{}".format(word_need) not in message.content.lower():
                embed = discord.Embed(title = "**{}** был атакован стендом справедливости.".format(message.author.name), description = "*Попал в мут на 3 минуты, не написав нужное слово.*", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/37/Justice_with_Enya.png/revision/latest/scale-to-width-down/640?cb=20140716122650")
                await bot.send_message(message.channel, embed=embed)
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                await bot.add_roles(message.author, mute_role)
                word_need = ""
                justly = ""
                
                await asyncio.sleep(180)
                
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                await bot.remove_roles(message.author, mute_role)
            else:
                embed = discord.Embed(title = "**{}** был атакован.".format(message.author.name), description = "*Не попал в мут.*", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/82/Justice_polnareff_ruled.jpg/revision/latest/scale-to-width-down/317?cb=20140817045354")
                await bot.send_message(message.channel, embed=embed)
                word_need = ""
                justly = ""
                
    if message.author.id == locked:
        if "The Lock" in (role.name for role in message.author.roles):
            return
        if "езвени" in message.content.lower():
            mon += 5
            embed = discord.Embed(title = "В замке теперь **{} монет**.".format(mon), description = "*Проверить сколько у тебя монет и команды за них:* ``~mcheck``", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(message.channel, embed=embed)
        if "извени" in message.content.lower():
            mon += 5
            embed = discord.Embed(title = "В замке теперь **{} монет**.".format(mon), description = "*Проверить сколько у тебя монет и команды за них:* ``~mcheck``", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(message.channel, embed=embed)
        if "сорян" in message.content.lower():
            mon += 5
            embed = discord.Embed(title = "В замке теперь **{} монет**.".format(mon), description = "*Проверить сколько у тебя монет и команды за них:* ``~mcheck``", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(message.channel, embed=embed)
        if "сорре" in message.content.lower():
            mon += 5
            embed = discord.Embed(title = "В замке теперь **{} монет**.".format(mon), description = "*Проверить сколько у тебя монет и команды за них:* ``~mcheck``", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(message.channel, embed=embed)
        if "соре" in message.content.lower():
            mon += 5
            embed = discord.Embed(title = "В замке теперь **{} монет**.".format(mon), description = "*Проверить сколько у тебя монет и команды за них:* ``~mcheck``", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(message.channel, embed=embed)
        if "сорри" in message.content.lower():
            mon += 5
            embed = discord.Embed(title = "В замке теперь **{} монет**.".format(mon), description = "*Проверить сколько у тебя монет и команды за них:* ``~mcheck``", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(message.channel, embed=embed)
        if "сори" in message.content.lower():
            mon += 5
            embed = discord.Embed(title = "В замке теперь **{} монет**.".format(mon), description = "*Проверить сколько у тебя монет и команды за них:* ``~mcheck``", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(message.channel, embed=embed)
        if "прости" in message.content.lower():
            mon += 5
            embed = discord.Embed(title = "В замке теперь **{} монет**.".format(mon), description = "*Проверить сколько у тебя монет и команды за них:* ``~mcheck``", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(message.channel, embed=embed)
        if "прасти" in message.content.lower():
            mon += 5
            embed = discord.Embed(title = "В замке теперь **{} монет**.".format(mon), description = "*Проверить сколько у тебя монет и команды за них:* ``~mcheck``", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(message.channel, embed=embed)
        if "извени" in message.content.lower():
            mon += 5
            embed = discord.Embed(title = "В замке теперь **{} монет**.".format(mon), description = "*Проверить сколько у тебя монет и команды за них:* ``~mcheck``", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(message.channel, embed=embed)
        if "sorry" in message.content.lower():
            mon += 5
            embed = discord.Embed(title = "В замке теперь **{} монет**.".format(mon), description = "*Проверить сколько у тебя монет и команды за них:* ``~mcheck``", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(message.channel, embed=embed)
        if "sorri" in message.content.lower():
            mon += 5
            embed = discord.Embed(title = "В замке теперь **{} монет**.".format(mon), description = "*Проверить сколько у тебя монет и команды за них:* ``~mcheck``", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(message.channel, embed=embed)
        if "sory" in message.content.lower():
            mon += 5
            embed = discord.Embed(title = "В замке теперь **{} монет**.".format(mon), description = "*Проверить сколько у тебя монет и команды за них:* ``~mcheck``", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(message.channel, embed=embed)
        if "sori" in message.content.lower():
            mon += 5
            embed = discord.Embed(title = "В замке теперь **{} монет**.".format(mon), description = "*Проверить сколько у тебя монет и команды за них:* ``~mcheck``", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(message.channel, embed=embed)
                
    if message.author.id == brat:
        if target == oblik:
            if "я пидорас галимый" in message.content.lower():
                cel = discord.Server.get_member(message.server, user_id=target)
                
                target = ""
                
                embed = discord.Embed(title = "*Предсказание сбылось.*", description = "***``Вам удалось замутить цель на 10 минут.``***", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/31/Tohth_jotarodeath01.png/revision/latest/scale-to-width-down/640?cb=20150207174400")
                await bot.send_message(message.channel, embed=embed)
            
            
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                await bot.add_roles(cel, mute_role)
                
                await asyncio.sleep(600)
                
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                await bot.remove_roles(cel, mute_role)
            

    if "В муте" not in (role.name for role in message.author.roles):
        if message.author.id != ripple_id:
            if shooting == message.author.id: #ТОТ, В КОГО СТРЕЛЯЛИ
                if canshoot == 1:
                    embed = discord.Embed(title = "Снова можно **стрелять**.", description = "*Вы вернули пулю.*", color = 0xffff00)
                    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b4/Megyan.png/revision/latest/scale-to-width-down/640?cb=20140606213118")
                    await bot.send_message(message.channel, embed=embed)
                    canshoot = 0
                    shooting = ""
                    
    if message.author.id == shocked:
        embed = discord.Embed(title = "*Вы получили удар током.*", description = "*К вам* **прилипло** *очередное сообщение.*", color = 0xffff00)
        randpic = ["https://vignette.wikia.nocookie.net/jjba/images/3/3b/Bastet_magnet.png/revision/latest/scale-to-width-down/640?cb=20150216073109", "https://vignette.wikia.nocookie.net/jjba/images/c/c8/Bastet_stronger.png/revision/latest/scale-to-width-down/400?cb=20150223053044"]
        embed.set_image(url=random.choice(randpic))
        await bot.send_message(message.author, embed=embed)
        await bot.send_message(message.author, embed=embed)
        await bot.send_message(message.author, embed=embed)
        await bot.send_message(message.author, embed=embed)
        await bot.send_message(message.author, embed=embed)
        await bot.send_message(message.author, embed=embed)
        
    if message.author.id == recording:
        whorec = discord.Server.get_member(message.server, user_id=wrec)
        await bot.send_message(whorec, "{} : {}".format(message.author.name, message.content))
        
    if "White Album" in (role.name for role in message.author.roles):
        if iceduser == "":
            ici = 1
        
    if "Здоровый" in (role.name for role in message.author.roles):
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.remove_roles(message.author, mute_role)
        
        zdorovii = discord.utils.find(lambda r: r.name == 'Здоровый', message.server.roles)
        await bot.remove_roles(message.author, zdorovii)
            
    if "На корабле" in (role.name for role in message.author.roles):
        if attackship == 1:
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.add_roles(message.author, mute_role)
            
    if message.author.id == hidden:
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.remove_roles(message.author, mute_role)
            
    if "На корабле" in (role.name for role in message.author.roles):
        if attackship == 0:
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.remove_roles(message.author, mute_role)
            
    if message.author.id == loving:
        lovermem = discord.Server.get_member(message.server, user_id=loved)
        if "В муте" in (role.name for role in message.author.roles):
            if loved != "":
                if "В муте" not in (role.name for role in lovermem.roles):
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                    await bot.add_roles(lovermem, mute_role)
                    
    if "В муте" in (role.name for role in message.author.roles):
        if "Achtung Baby" in (role.name for role in message.author.roles):
            achtung = 1
            
    if "В муте" in (role.name for role in message.author.roles):
        if "Super Fly" in (role.name for role in message.author.roles):
            if ripple_id != reflecting:
                superflying = discord.Server.get_member(message.server, user_id=reflecting)
            
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                await bot.add_roles(superflying, mute_role)
        if "Diver Down" in (role.name for role in message.author.roles):
            dcharge += 1
                
    if "В муте" in (role.name for role in message.author.roles):
        if "Earth Wind and Fire" in (role.name for role in message.author.roles):
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.remove_roles(message.author, mute_role)
            
        if "Gold Experience" in (role.name for role in message.author.roles):
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.remove_roles(message.author, mute_role)
            
        if "Лёгкий" in (role.name for role in message.author.roles):
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.remove_roles(message.author, mute_role)
            
            mutes_role = discord.utils.find(lambda r: r.name == 'Лёгкий', message.server.roles)
            await bot.remove_roles(message.author, mutes_role)
            
    if "В муте" in (role.name for role in message.author.roles):
        if "Highway Star" in (role.name for role in message.author.roles):
            if highw != "":
                highwayed = discord.Server.get_member(message.server, user_id=highw)
                embed = discord.Embed(title = "**{}** высосал жизненную энергию **{}**.".format(message.author.name, highwayed.name), description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/75/HS_sucks_out_Rohan%27s_nutrients.png/revision/latest/scale-to-width-down/640?cb=20161007225428")
                await bot.send_message(message.channel, embed=embed)
                
                highw = ""

                mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                await bot.remove_roles(message.author, mute_role)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                await bot.add_roles(highwayed, mute_role)
        
                await asyncio.sleep(420)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                await bot.remove_roles(highwayed, mute_role)
                
    if "Sticky Fingers" in (role.name for role in message.author.roles):
        if message.channel == zipped_channel:
            zipper = discord.Server.get_member(message.server, user_id=zipped)
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.add_roles(zipper, mute_role)
        
            await asyncio.sleep(5)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.remove_roles(zipper, mute_role)
            
    if message.author.id == stoned:
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.add_roles(message.author, mute_role)
        
    if tickettoride == 1:
        if "Dirty Deeds Done Dirt Cheap" in (role.name for role in message.author.roles):
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.remove_roles(message.author, mute_role)
        
    if message.author.id == nitka:
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.remove_roles(message.author, mute_role)
        
    if "Silver Chariot" in (role.name for role in message.author.roles):
        if "Requiem" in (role.name for role in message.author.roles):
            if "В муте" in (role.name for role in message.author.roles):
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                await bot.remove_roles(message.author, mute_role)
                
    if muted_all_users == 4:
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.remove_roles(message.author, mute_role)
                    
    if "В муте" in (role.name for role in message.author.roles): #Мут одного человека
        if message.author.id == aging:
            aging = ""
            return
        if message.author.id == ghost:
            return
        if message.author.id != ripple_id:
            if "Silver Chariot" in (role.name for role in message.author.roles):
                if top_speed != 1:
                    await bot.delete_message(message)
                    await bot.delete_message(message)
                    await bot.delete_message(message)
                    await bot.delete_message(message)
                    await bot.delete_message(message)
                else:
                    embed = discord.Embed(title = "{} удалось увернуться от атаки.".format(message.author.name), description = "", color = 0xffff00)
                    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f3/Silver_Chariot_no_armor.png/revision/latest/scale-to-width-down/640?cb=20160410022457")
                    await bot.send_message(message.channel, embed=embed)
            
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                    await bot.remove_roles(message.author, mute_role)
            else:
                await bot.delete_message(message)
                await bot.delete_message(message)
                await bot.delete_message(message)
                await bot.delete_message(message)
                await bot.delete_message(message)
                
    if muted_all_users == 2:
        if "King Crimson" not in (role.name for role in message.author.roles):
            await bot.delete_message(message)
                
    if muted_all_users == 1:
        if "The World" not in (role.name for role in message.author.roles):
            if "Star Platinum" not in (role.name for role in message.author.roles):
                stopped_mgs.append(message)
        
        
    if muted_all_users == 1: #Мут всех юзеров
        if "King Crimson" in (role.name for role in message.author.roles):
            if star_stop == 3:
                return
        if "Star Platinum" in (role.name for role in message.author.roles):
            if star_stop == 2:
                return
        if "The World" in (role.name for role in message.author.roles):
            if star_stop == 1:
                return
        if message.author.id == BOT_ID:
            return
        if star_stop == 4:
            await bot.delete_message(message)
            lol = "      ".join(message.content)
            ebatb = await bot.send_message(message.channel, "{} : {}".format(message.author.name, lol))
        
            await asyncio.sleep(1)
            
            lol2 = "      ".join(lol)
            await bot.edit_message(ebatb, "{} : {}".format(message.author.name, lol2))
            
            await asyncio.sleep(2)
            
            lol3 = "      ".join(lol2)
            await bot.edit_message(ebatb, "{} : {}".format(message.author.name, lol3))
            
            await asyncio.sleep(3)
            
            await bot.delete_message(ebatb, "{} : {}".format(message.author.name, lol3))
            return
        await bot.delete_message(message)
            
    if ignited_all_users == 1: #Зажечь всех
        if muted_all_users == 1:
            return
        if "Превращён в бумагу" in (role.name for role in message.author.roles):
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if message.author.id == BOT_ID:
            return
        if gravitied == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        
        content_lol = str(message.content)
        lol = " 🔥 ".join(content_lol)
        content_lol2 = str(message.author.name)
        lol2 = " 🔥 ".join(content_lol2)
        await bot.send_message(message.channel, "{} : {}".format(lol2, lol))
        
        
        
    if weather == 1:
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users ==1:
            return
        if message.author.id == BOT_ID:
            return
        if gravitied == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        xyis = await bot.send_message(message.channel, "<@{}> : {}".format(message.author.id, message.content))
        lolpizdass = message.content
        for i in range(len(message.content)):
            pizdass = ":droplet: " + lolpizdass + " :droplet:"
            await bot.edit_message(xyis, "<@{}> : {}".format(message.author.id, pizdass))
            await asyncio.sleep(0.3)
            lolpizdass = ":droplet: " + pizdass + " :droplet:"
            
    if gravitied == 1:
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users ==1:
            return
        if message.author.id == BOT_ID:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        
        newmesg = message.content.lower().replace('а', 'ɐ').replace('б', 'ƍ').replace('в', 'ʚ').replace('г', 'ɹ').replace('д', 'ɓ').replace('е', 'ǝ').replace('ё', 'ǝ').replace('ж', 'ж').replace('з', 'ε').replace('и', 'и').replace('к', 'ʞ').replace('л', 'v').replace('м', 'w').replace('н', 'н').replace('о', 'о').replace('п', 'u').replace('р', 'd').replace('с', 'ɔ').replace('т', 'ɯ').replace('у', 'ʎ').replace('ф', 'ф').replace('х', 'х').replace('ц', 'ǹ').replace('ч', 'Һ').replace('ш', 'm').replace('щ', 'm').replace('ь', 'q').replace('ъ', 'q').replace('ы', 'ıq').replace('э', 'є').replace('ю', 'oı').replace('я', 'ʁ')
        await bot.send_message(message.channel, "<@{}> : {}".format(message.author.id, newmesg[::-1]))
        
    if ignite_id == message.author.id: #Зажечь
        if muted_all_users == 1:
            return
        if "Превращён в бумагу" in (role.name for role in message.author.roles):
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if message.author.id == BOT_ID:
            return
        if sound == message.author.id:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        
        content_lol = str(message.content)
        lol = " 🔥 ".join(content_lol)
        content_lol2 = str(message.author.name)
        lol2 = " 🔥 ".join(content_lol2)
        await bot.send_message(message.channel, "{} : {}".format(lol2, lol))
        
    if puppet == message.author.id: #Зажечь
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if ignite_id == message.author.id:
            return
        if message.author.id == BOT_ID:
            return
        if sound == message.author.id:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        await bot.send_message(message.channel, "<@{}> : {}".format(message.author.id, message.content))
        
    if poisoned == message.author.id:
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if ignite_id == message.author.id:
            return
        if message.author.id == BOT_ID:
            return
        if sound == message.author.id:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        messagoison = "{}{}".format(message.content, messagoison)
        await bot.delete_message(message)
        await bot.send_message(message.channel, "<@{}> : {}".format(message.author.id, messagoison))
        
    if mimi == message.author.id: #Зажечь
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if ignite_id == message.author.id:
            return
        if message.author.id == BOT_ID:
            return
        if sound == message.author.id:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        await bot.send_message(message.channel, "<@{}> : {}".format(message.author.id, message.content))
        
    if littled == message.author.id: #Зажечь
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if ignite_id == message.author.id:
            return
        if message.author.id == BOT_ID:
            return
        if sound == message.author.id:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        await bot.send_message(message.channel, "<@{}> : {}".format(message.author.id.lower(), message.content.lower()))
        
    if degrod == message.author.id: #ДЕГРАДАЦИЯ
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if ignite_id == message.author.id:
            return
        if message.author.id == BOT_ID:
            return
        if sound == message.author.id:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        
        degr_content = message.content.lower()
        degr_content2 = degr_content.replace('.', '')
        degr_content3 = degr_content2.replace(', ', '')
        degr_content4 = degr_content3.replace(',', '')
        degr_content5 = degr_content4.replace('-', '')
        degr_content6 = degr_content5.replace('о', 'а')
        degr_content7 = degr_content6.replace('е', 'и')
        degr_content8 = degr_content7.replace('привет', 'здарова')
        degr_content9 = degr_content8.replace('маника', 'кисель')
        degr_content10 = degr_content9.replace('моника', 'кисель')
        degr_content11 = degr_content10.replace('нацуки', 'кисель')
        degr_content12 = degr_content11.replace('юри', 'кисель')
        degr_content13 = degr_content12.replace('саёри', 'кисель')
        degr_content14 = degr_content13.replace('саири', 'кисель')
        degr_content15 = degr_content14.replace('саери', 'кисель')
        degr_content16 = degr_content15.replace('сайори', 'кисель')
        degr_content17 = degr_content16.replace('сайари', 'кисель')
        await bot.send_message(message.channel, "<@{}> : {}".format(message.author.id, degr_content17))
        
    if degrodi == 1: #ДЕГРАДАЦИЯ
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users == 1:
            return
        if weather == 1:
            return
        if gravitied == 1:
            return
        if message.author.id == BOT_ID:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        
        degr_content = message.content.lower()
        degr_content2 = degr_content.replace('.', '')
        degr_content3 = degr_content2.replace(', ', '')
        degr_content4 = degr_content3.replace(',', '')
        degr_content5 = degr_content4.replace('-', '')
        degr_content6 = degr_content5.replace('о', 'а')
        degr_content7 = degr_content6.replace('е', 'и')
        degr_content8 = degr_content7.replace('привет', 'здарова')
        degr_content9 = degr_content8.replace('маника', 'кисель')
        degr_content10 = degr_content9.replace('моника', 'кисель')
        degr_content11 = degr_content10.replace('нацуки', 'кисель')
        degr_content12 = degr_content11.replace('юри', 'кисель')
        degr_content13 = degr_content12.replace('саёри', 'кисель')
        degr_content14 = degr_content13.replace('саири', 'кисель')
        degr_content15 = degr_content14.replace('саери', 'кисель')
        degr_content16 = degr_content15.replace('сайори', 'кисель')
        degr_content17 = degr_content16.replace('сайари', 'кисель')
        await bot.send_message(message.channel, "<@{}> : {}".format(message.author.id, degr_content17))
        
    if user_lie == message.author.id: #ДЕГРАДАЦИЯ
        if lie_to == "":
            return
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if ignite_id == message.author.id:
            return
        if message.author.id == BOT_ID:
            return
        if sound == message.author.id:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        
        lietent = message.content.lower().replace(lie_word.lower(), lie_to.lower())
        await bot.send_message(message.channel, "<@{}> : {}".format(message.author.id, lietent))
        
    if maniq == message.author.id: #Зажечь
        if mimi != "":
            if muted_all_users == 1:
                return
            if "В муте" in (role.name for role in message.author.roles):
                if message.author.id != ripple_id:
                    return
            if ignited_all_users ==1:
                return
            if weather == 1:
                return
            if ignite_id == message.author.id:
                return
            if message.author.id == BOT_ID:
                return
            if sound == message.author.id:
                return
            if gravitied == 1:
                return
            if degrodi == 1:
                return
            if newlife != "":
                if newlife != message.author.id:
                    return
            await bot.delete_message(message)
            chelikrolfna = discord.Server.get_member(message.server, user_id=mimi)
            await bot.send_message(message.channel, "<@{}> : {}".format(chelikrolfna.id, message.content))
        
    if jawed == message.author.id: #JAW
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if ignite_id == message.author.id:
            return
        if message.author.id == BOT_ID:
            return
        if puppet == message.author.id:
            return
        if sound == message.author.id:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        xyi = await bot.send_message(message.channel, "<@{}> : {}".format(message.author.id, message.content))
        lolpizda = message.content
        for i in range(len(message.content)):
            pizda = lolpizda[:-1]
            await bot.edit_message(xyi, "<@{}> : {}".format(message.author.id, pizda))
            await asyncio.sleep(0.3)
            lolpizda = pizda[:-1]
            
    if newlife != "":
        if message.author.id != newlife:
            if muted_all_users == 1:
                return
            if "В муте" in (role.name for role in message.author.roles):
                if message.author.id != ripple_id:
                    return
            await bot.delete_message(message)
            await asyncio.sleep(5)
            await bot.send_message(message.channel, "<@{}> : {}".format(message.author.id, message.content))
            
            
            
    if voided == message.author.id: #VOIDED
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if ignite_id == message.author.id:
            return
        if message.author.id == BOT_ID:
            return
        if puppet == message.author.id:
            return
        if sound == message.author.id:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        content_lol = str(message.content)
        lol = " __~~**~~__ ".join(content_lol)
        content_lol2 = str(message.author.name)
        lol2 = " __~~**~~__ ".join(content_lol2)
        await bot.send_message(message.channel, "{} : {}".format(lol2, lol))
        
    if watered == message.author.id: #WATERED
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if ignite_id == message.author.id:
            return
        if message.author.id == BOT_ID:
            return
        if puppet == message.author.id:
            return
        if sound == message.author.id:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        xyis = await bot.send_message(message.channel, "<@{}> : {}".format(message.author.id, message.content))
        lolpizdas = message.content
        for i in range(len(message.content)):
            pizdas = ":droplet: " + lolpizdas + " :droplet:"
            await bot.edit_message(xyis, "<@{}> : {}".format(message.author.id, pizdas))
            await asyncio.sleep(0.3)
            lolpizdas = ":droplet: " + pizdas + " :droplet:"
            
    if spinner == message.author.id:
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if ignite_id == message.author.id:
            return
        if message.author.id == BOT_ID:
            return
        if sound == message.author.id:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        
        mesg = "  ".join(message.content)
        ad = await bot.send_message(message.channel, "<@{}> : {}".format(message.author.id, message.content))
        await asyncio.sleep(3)
        await bot.edit_message(ad, "<@{}> : {}".format(message.author.id, mesg))
        await asyncio.sleep(3)
        mesg2 = "  ".join(mesg)
        await bot.edit_message(ad, "<@{}> : {}".format(message.author.id, mesg2))
        await asyncio.sleep(3)
        await bot.delete_message(ad)
        
        for i in range(spinning):
            if spinning > 0:
                await bot.send_message(message.author, "<@{}>".format(message.author.id))
                
    if spinin == message.author.id:
        spini += 5
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.add_roles(message.author, mute_role)
        await asyncio.sleep(spini)
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.remove_roles(message.author, mute_role)
        
    if "Крутится" in (role.name for role in message.author.roles):
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.add_roles(message.author, mute_role)
        
        await asyncio.sleep(8)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.remove_roles(message.author, mute_role)
            
    if lovedel != "":
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if ignite_id == message.author.id:
            return
        if message.author.id == BOT_ID:
            return
        if puppet == message.author.id:
            return
        if sound == message.author.id:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        loldel = lovedel.lower()
        if "{}".format(loldel) in message.content.lower():
            await bot.delete_message(message)
            await bot.send_message(message.channel, "<@{}> : {}".format(message.author.id, message.content.replace('{}'.format(loldel), '')))
        
    if sound == message.author.id: #ЗВУК
        if act2 == 1:
            if "гнев" in soundword.lower():
                embed = discord.Embed(title = "**{}** **{}** **{}** **{}** **{}**".format(soundword, soundword, soundword, soundword, soundword), description = "**{}** **{}** **{}** **{}** **{}**".format(soundword, soundword, soundword, soundword, soundword), color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a8/SHA_chasing_sizzle.png/revision/latest/scale-to-width-down/640?cb=20160904163227")
                await bot.send_message(message.author, embed=embed)
                await bot.send_message(message.author, embed=embed)
                await bot.send_message(message.author, embed=embed)
                await bot.send_message(message.author, embed=embed)
                await bot.send_message(message.author, embed=embed)
                await bot.send_message(message.author, embed=embed)
                await bot.send_message(message.author, embed=embed)
                await bot.send_message(message.author, embed=embed)
            if "громкий" not in soundword.lower():
                return
        if soundword == "":
            return
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if message.author.id == BOT_ID:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        content_lol = str(message.content)
        lol = " **{}** ".format(soundword).join(content_lol)
        await bot.send_message(message.channel, "<@{}> : {}".format(message.author.id, lol))
        
        embed = discord.Embed(title = "**{}** **{}** **{}** **{}** **{}**".format(soundword, soundword, soundword, soundword, soundword), description = "**{}** **{}** **{}** **{}** **{}**".format(soundword, soundword, soundword, soundword, soundword), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/eb/Koichi%27s_mom_believing.png/revision/latest/scale-to-width-down/640?cb=20160506192624")
        await bot.send_message(message.author, embed=embed)
            
    if hanged == message.author.id: #ОТЗЕРКАЛЕННОСТЬ
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                await bot.delete_message(message)
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if ignite_id == message.author.id:
            return
        if message.author.id == BOT_ID:
            return
        if puppet == message.author.id:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        await bot.send_message(message.channel, "{} : {}".format(message.author.name[::-1], message.content[::-1]))
        
    if achtung == 1: #АХТУНГ
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                await bot.delete_message(message)
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if ignite_id == message.author.id:
            return
        if message.author.id == BOT_ID:
            return
        if puppet == message.author.id:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        lol = "                              ".join(message.content)
        ebatb = await bot.send_message(message.channel, "{} : {}".format(message.author.name, lol))
        
        achtung = 0
        
        await asyncio.sleep(5)
        
        await bot.delete_message(ebatb)
        
    if message.author.id == invisiblity:
        if muted_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                await bot.delete_message(message)
                return
        if ignited_all_users ==1:
            return
        if weather == 1:
            return
        if ignite_id == message.author.id:
            return
        if message.author.id == BOT_ID:
            return
        if puppet == message.author.id:
            return
        if gravitied == 1:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        lol = "                              ".join(message.content)
        ebatb = await bot.send_message(message.channel, "{} : {}".format(message.author.name, lol))
        
        await asyncio.sleep(5)
        
        await bot.delete_message(ebatb)
        
    if "Превращён в бумагу" in (role.name for role in message.author.roles):
        if muted_all_users == 1:
            return
        if gravitied == 1:
            return
        if weather == 1:
            return
        if ignited_all_users == 1:
            return
        if "В муте" in (role.name for role in message.author.roles):
            if message.author.id != ripple_id:
                await bot.delete_message(message)
                return
        if message.author.id == BOT_ID:
            return
        if puppet == message.author.id:
            return
        if degrodi == 1:
            return
        if newlife != "":
            if newlife != message.author.id:
                return
        await bot.delete_message(message)
        await bot.send_message(message.channel, "{} : ~~{}~~".format(message.author.name, message.content))
                
    if sound == message.author.id: #ЗВУК
        if act2 == 1:
            if "оглушён" in soundword.lower():
                
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                await bot.add_roles(message.author, mute_role)
        
                await asyncio.sleep(5)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                await bot.remove_roles(message.author, mute_role)
                
    if weather == 2:
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.add_roles(message.author, mute_role)
        
        await asyncio.sleep(6)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.remove_roles(message.author, mute_role)
        
    if weather == 3:
        await bot.send_message(message.author, ":snowflake: :snowflake: :snowflake:")
        await bot.send_message(message.author, ":snowflake: :snowflake: :snowflake:")
        await bot.send_message(message.author, ":snowflake: :snowflake: :snowflake:")
        await bot.send_message(message.author, ":snowflake: :snowflake: :snowflake:")
        await bot.send_message(message.author, ":snowflake: :snowflake: :snowflake:")
        await bot.send_message(message.author, ":snowflake: :snowflake: :snowflake:")
        await bot.send_message(message.author, ":snowflake: :snowflake: :snowflake:")
        await bot.send_message(message.author, ":snowflake: :snowflake: :snowflake:")
        await bot.send_message(message.author, ":snowflake: :snowflake: :snowflake:")
        await bot.send_message(message.author, ":snowflake: :snowflake: :snowflake:")
        await bot.send_message(message.author, ":snowflake: :snowflake: :snowflake:")
        await bot.send_message(message.author, ":snowflake: :snowflake: :snowflake:")
        await bot.send_message(message.author, ":snowflake: :snowflake: :snowflake:")
        await bot.send_message(message.author, ":snowflake: :snowflake: :snowflake:")
        await bot.send_message(message.author, ":snowflake: :snowflake: :snowflake:")
                
    if "{}".format(emp_w) in message.content:
        if emp_w != "":
            parazit = message.author.id
            emp_w = ""
            
            embed = discord.Embed(title = "Теперь *паразит* на **{}**.".format(message.author.name), description = "*Им может управлять* **``Императрица.``**".format(message.author.name), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/02/Empresssmall.png/revision/latest/scale-to-width-down/623?cb=20140620174046")
            await bot.send_message(message.channel, embed=embed)
            
            await asyncio.sleep(1500)
            
            userNena = discord.Server.get_member(message.server, user_id=paraziting)
                        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.add_roles(userNena, mute_role)
            
            mute2_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.add_roles(userNena, mute2_role)
            
            mute3_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.add_roles(userNena, mute3_role)
            
            mute4_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.add_roles(userNena, mute4_role)
            
            empre_role = discord.utils.find(lambda r: r.name == 'Empress', message.server.roles)
            await bot.remove_roles(userNena, empre_role)
            
            empre2_role = discord.utils.find(lambda r: r.name == 'Empress', message.server.roles)
            await bot.remove_roles(userNena, empre2_role)
            
            empre3_role = discord.utils.find(lambda r: r.name == 'Empress', message.server.roles)
            await bot.remove_roles(userNena, empre3_role)
            
            await asyncio.sleep(1800)
            
            userNena = discord.Server.get_member(message.server, user_id=paraziting)
            
            muted_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.remove_roles(userNena, mute_role)
            
            mutedd_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.remove_roles(userNena, mutedd_role)
            
            muteddd_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.remove_roles(userNena, muteddd_role)
            
    if "<@{}>".format(user_bomb) in message.content:
        embed = discord.Embed(title = "{} взорвался.".format(message.author.name), description = "*{} был взорван и отправлен в мут на 10 минут.*".format(message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/73/KQ_explosion_aftermath.png/revision/latest/scale-to-width-down/640?cb=20170226213702")
        await bot.send_message(message.channel, embed=embed)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.add_roles(message.author, mute_role)
        
        await asyncio.sleep(600)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.remove_roles(message.author, mute_role)
            
    if "<@{}>".format(bites_dust) in message.content:
        if "Heaven's Door" in (role.name for role in message.author.roles):
            if "~book" not in message.content.lower():
                if bites_dust != "":
                    if muted_all_users == 1:
                        return
                    if "В муте" in (role.name for role in message.author.roles):
                        return
                    if "Killer Queen" in (role.name for role in message.author.roles):
                        return
                    muted_all_users = 1
                    star_stop = 0
                    embed = discord.Embed(title = "ТРЕТЬЯ БОМБА СМЕРТЕЛЬНОЙ КОРОЛЕВЫ: **ПЫЛЬНЫЙ УКУС**.", description = "「KILLER QUEEN」 DAISAN NO BAKUDAN 「BITES ZA DUSTO」", color = 0xffff00)
                    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e8/RidingHayato.gif")
                    await bot.send_message(message.channel, embed=embed)

                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                    await bot.add_roles(message.author, mute_role)

                    muted_all_users = 0
        else:
            if bites_dust != "":
                if muted_all_users == 1:
                    return
                if "В муте" in (role.name for role in message.author.roles):
                    return
                if "Killer Queen" in (role.name for role in message.author.roles):
                    return
                muted_all_users = 1
                star_stop = 0
                embed = discord.Embed(title = "ТРЕТЬЯ БОМБА СМЕРТЕЛЬНОЙ КОРОЛЕВЫ: **ПЫЛЬНЫЙ УКУС**.", description = "「KILLER QUEEN」 DAISAN NO BAKUDAN 「BITES ZA DUSTO」", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e8/RidingHayato.gif")
                await bot.send_message(message.channel, embed=embed)

                mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                await bot.add_roles(message.author, mute_role)

                muted_all_users = 0
        
    if message.author.id == virus:
        if virus_S == 1:
            await bot.send_message(message.author, "Вас разъедает вирус.")
        if virus_S == 2:
            await bot.send_message(message.author, "Вас разъедает вирус.")
            
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.add_roles(message.author, mute_role)
        
            await asyncio.sleep(7)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.remove_roles(message.author, mute_role)

    if message.author.id == sha_bomb: #вторая бомба
    
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.add_roles(message.author, mute_role)
        
        await asyncio.sleep(5)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.remove_roles(message.author, mute_role)
        
    if message.author.id == sha_bombe:
    
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.add_roles(message.author, mute_role)
        
        await asyncio.sleep(5)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.remove_roles(message.author, mute_role)
        
    if message.author.id == sha_bombe2:
    
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.add_roles(message.author, mute_role)
        
        await asyncio.sleep(5)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.remove_roles(message.author, mute_role)
        
    if message.author.id == sha_bombe3:
    
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.add_roles(message.author, mute_role)
        
        await asyncio.sleep(5)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.remove_roles(message.author, mute_role)
        
    if message.author.id == sha_bombe4:
    
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.add_roles(message.author, mute_role)
        
        await asyncio.sleep(5)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
        await bot.remove_roles(message.author, mute_role)
        
    if message.author.id == barn: #БАРНЕД
        if barned == 3:
            if message.author.id == sha_bomb:
                return
            if "В муте" in (role.name for role in message.author.roles):
                return
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.add_roles(message.author, mute_role)
        
            await asyncio.sleep(10)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.remove_roles(message.author, mute_role)
        if barned == 2:
            await bot.send_message(message.author, "<@{}>".format(message.author.id))
            await bot.send_message(message.author, "<@{}>".format(message.author.id))
            if message.author.id == sha_bomb:
                return
            if "В муте" in (role.name for role in message.author.roles):
                return
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.add_roles(message.author, mute_role)
        
            await asyncio.sleep(4)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.remove_roles(message.author, mute_role)
        if barned == 1:
            await bot.send_message(message.author, "<@{}>".format(message.author.id))
            if message.author.id == sha_bomb:
                return
            if "В муте" in (role.name for role in message.author.roles):
                return
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.add_roles(message.author, mute_role)
        
            await asyncio.sleep(2)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.remove_roles(message.author, mute_role)
        if barned == 0:
            await bot.send_message(message.author, "<@{}>".format(message.author.id))
            
    if message.author.id == gayporn:
        gaty = ["https://www.xvideos.com/video16327169/leche_calentita_en_la_cara_-_gay_sex_-_semen", "https://www.xvideos.com/video20454221/cuddle_up_scene_2", "https://www.xvideos.com/video31813769/army_men_huge_dicks_and_straight_russian_military_boys_gay_xxx", "https://www.xvideos.com/video19444539/dando_gostoso", "https://www.xvideos.com/video13895159/sexy_friends_best_dick_riding", "https://www.xvideos.com/video37040281/dude_tries_gayporn_for_gf", "https://www.xvideos.com/video13960049/hot_cub_brutal_anal_gangbang", "https://www.xvideos.com/video22672265/docking", "https://www.xvideos.com/video23703588/hot_gay_anal_sex", "https://www.xvideos.com/video20624999/passivo_pidao", "https://www.xvideos.com/video13940451/horny_friends_deep_penetration"]
        await bot.send_message(message.author, "{}".format(random.choice(gaty)))
            
    if message.author.id == booked:
        if bookab == "1":
            booksay = ["https://www.xvideos.com/video16327169/leche_calentita_en_la_cara_-_gay_sex_-_semen", "https://www.xvideos.com/video20454221/cuddle_up_scene_2", "https://www.xvideos.com/video31813769/army_men_huge_dicks_and_straight_russian_military_boys_gay_xxx", "https://www.xvideos.com/video19444539/dando_gostoso", "https://www.xvideos.com/video13895159/sexy_friends_best_dick_riding", "https://www.xvideos.com/video37040281/dude_tries_gayporn_for_gf", "https://www.xvideos.com/video13960049/hot_cub_brutal_anal_gangbang", "https://www.xvideos.com/video22672265/docking", "https://www.xvideos.com/video23703588/hot_gay_anal_sex", "https://www.xvideos.com/video20624999/passivo_pidao", "https://www.xvideos.com/video13940451/horny_friends_deep_penetration"]
            await bot.send_message(message.author, "{}".format(random.choice(booksay)))
        if bookab == "2":
            embed = discord.Embed(title = "**{}** читается.".format(message.author.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/be/RohanTalkingthroughHeaven%27sDoor.png/revision/latest/scale-to-width-down/640?cb=20170110203011")
            await bot.send_message(message.channel, embed=embed)
            
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.add_roles(message.author, mute_role)
        
            await asyncio.sleep(3)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
            await bot.remove_roles(message.author, mute_role)
        if bookab == "3":
            await bot.send_message(message.author, "<@{}>".format(message.author.id))
        if bookab == "4":
            await bot.send_message(message.channel, "**{}** : {}".format(message.author.name, message.content))
        
    if "Baby Face" not in (role.name for role in message.author.roles):
        if message.content.startswith('~'):
            muting += 1
    if message.author.id == baby:
        return
    if message.author.id == froze:
        if message.content.startswith('~'):
            embed = discord.Embed(title = "**{}** был разморожен.".format(message.author.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/5b/Pet_Shop_and_Horus.png/revision/latest/scale-to-width-down/640?cb=20150411064101")
            await bot.send_message(message.channel, embed=embed)
            
            froze = ""
            return
    if message.author.id == act3freeze:
        if message.content.startswith('~'):
            return
    if "Превращён в бумагу" in (role.name for role in message.author.roles):
        if message.content.startswith('~'):
            return
    if message.author.id == zeroed:
        if message.content.startswith('~'):
            return
    if message.author.id == littled:
        if message.content.startswith('~'):
            return
    if message.author.id == iceduser:
        if message.content.startswith('~'):
            return
    if muted_all_users == 2:
        if "King Crimson" not in (role.name for role in message.author.roles):
            if message.content.startswith('~'):
                return
            
    if aero == 1:
        if "Aerosmith" in (role.name for role in message.author.roles):
            if message.content.startswith('~'):
                return
    if "Смягчён" in (role.name for role in message.author.roles):
        if message.content.startswith('~'):
            soften_role = discord.utils.find(lambda r: r.name == 'Смягчён', message.server.roles)
            await bot.remove_roles(message.author, soften_role)
            return
            
    if "Лёгкий" in (role.name for role in message.author.roles):
        if message.content.startswith('~'):
            return

    if "В муте" in (role.name for role in message.author.roles):
        if "Enigma" in (role.name for role in message.author.roles):
            role_delete = discord.utils.find(lambda r: r.name == "Превращён в бумагу", message.server.roles)
            
            if role_delete is not None:
                await bot.delete_role(message.author.server, role_delete)
                
    if zerkal_kanal != "":
        if meme != "":
            if message.channel == zerkal_kanal:
                if message.author.id == meme:
                    return
                    
    if "В муте" in (role.name for role in message.author.roles):
        if "Notorious B.I.G" in (role.name for role in message.author.roles):
            await bot.process_commands(message)
            
    if message.author.id == molded:
        if message.content.startswith('~'):
            if "<@{}>".format(molding) in message.content.lower():
                return
                
    if message.author.id == nitka:
        if message.content.startswith('~'):
            return
            
    if message.author.id == ghost:
        if message.content.startswith('~'):
            return
            
    if message.author.id == spinner:
        if message.content.startswith('~'):
            return
            
    if "King Crimson" not in (role.name for role in message.author.roles):
        if muted_all_users == 2:
            return
            
    if "В муте" not in (role.name for role in message.author.roles): #Процесс
        if muted_all_users != 1:
            await bot.process_commands(message)
            if message.author.id == aging:
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                await bot.add_roles(message.author, mute_role)
                aging = ""
        elif "Star Platinum" in (role.name for role in message.author.roles):
            if star_stop == 2:
                await bot.process_commands(message)
                if message.author.id == aging:
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                    await bot.add_roles(message.author, mute_role)
                    aging = ""
        elif "The World" in (role.name for role in message.author.roles):
            if star_stop == 1:
                await bot.process_commands(message)
                if message.author.id == aging:
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', message.server.roles)
                    await bot.add_roles(message.author, mute_role)
                    aging = ""
        
@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        await cooldown_mesg(ctx)
        
async def cooldown_mesg(ctx):
    if ctx.invoked_subcommand:
        await bot.send_message(ctx.message.channel, "Между *некоторыми командами* есть задержка. **Подождите...**")
    else:
        await bot.send_message(ctx.message.channel, "Между *некоторыми командами* есть задержка. **Подождите...**")
        
async def kila(ctx):
    global muted_all_users
    if ctx.invoked_subcommand:
        if muted_all_users == 2:
            async for x in bot.logs_from(ctx.message.channel, limit = 1):
                await bot.delete_message(x)
            await asyncio.sleep(1)
        else:
            pass
    else:
        if muted_all_users == 2:
            async for x in bot.logs_from(ctx.message.channel, limit = 1):
                await bot.delete_message(x)
            await asyncio.sleep(1)
        else:
            pass
        
@bot.command(pass_context=True) #Помощь
async def help(ctx):
    if ctx.message.author.server_permissions.administrator:
        await bot.send_message(ctx.message.channel, "Список команд отправлен в ЛС.")
        await bot.send_message(ctx.message.author, "Список команд для настройки этого бота:\n\n``~setrole - поставить все нужные для стендов слоты (убедитесь, что у вас достаточно слотов для этого)``\n``~removerole - удалить все добавленные ботом роли``")
        await bot.send_message(ctx.message.author, "Список доступных всем команд:\n\n``~info - посмотреть информацию о вашем стенде``\n``~creator - создатель этого бота``\n``~github - посмотреть репоситри этого бота на гит-хабе``")
    else:
        await bot.send_message(ctx.message.channel, "Список команд отправлен в ЛС.")
        await bot.send_message(ctx.message.author, "Список доступных команд:\n\n``~info - посмотреть информацию о вашем стенде``\n``~creator - создатель этого бота``\n``~github - посмотреть репоситри этого бота на гит-хабе``")
        
    if "Star Platinum" in (role.name for role in ctx.message.author.roles):
        await bot.send_message(ctx.message.author, "Команды голосового чата:\n\n``~yare - ЯРЕ ЯРЕ ДАЗЕ``\n``~warudo - ЗА ВАРУДО``")
    if "Thе World" in (role.name for role in ctx.message.author.roles):
        await bot.send_message(ctx.message.author, "Команды голосового чата:\n\n``~wry - ВРИИИИИИИИИИ``\n``~warudo - ЗА ВАРУДО``\n``~rr - РОАД РОЛЛА ДА``")
    if "Killer Queen" in (role.name for role in ctx.message.author.roles):
        if "Matured" in (role.name for role in ctx.message.author.roles):
            await bot.send_message(ctx.message.author, "Команды голосового чата:\n\n``~kq - КИРА КВИН``\n``~bd - БАЙТ ЗА ДАСТО")
        else:
            await bot.send_message(ctx.message.author, "Команды голосового чата:\n\n``~kq - КИРА КВИН``")
    if "Echoes ACT3" in (role.name for role in ctx.message.author.roles):
        await bot.send_message(ctx.message.author, "Команды голосового чата:\n\n``~act3 - АКТО СРИ ФРИФРИИИИИИЗ``\n``~shit - ЭС-ЭЙЧ-АЙ-ТИ``")
        
        
#ГОЛОСОВОЙ
@bot.command(pass_context=True)
async def shit(ctx):
    if "Echoes ACT3" in (role.name for role in ctx.message.author.roles):
        if ctx.message.author.voice_channel != None:
            voice = await bot.join_voice_channel(ctx.message.author.voice_channel)
            player = voice.create_ffmpeg_player('shit.mp3')
            player.start()
            await asyncio.sleep(2)
            voice_client = bot.voice_client_in(ctx.message.server)
            await voice_client.disconnect()

@bot.command(pass_context=True)
async def act3(ctx):
    if "Echoes ACT3" in (role.name for role in ctx.message.author.roles):
        if ctx.message.author.voice_channel != None:
            voice = await bot.join_voice_channel(ctx.message.author.voice_channel)
            player = voice.create_ffmpeg_player('3freeze.mp3')
            player.start()
            await asyncio.sleep(4)
            voice_client = bot.voice_client_in(ctx.message.server)
            await voice_client.disconnect()

@bot.command(pass_context=True)
async def bd(ctx):
    if "Killer Queen" in (role.name for role in ctx.message.author.roles):
        if "Matured" in (role.name for role in ctx.message.author.roles):
            if ctx.message.author.voice_channel != None:
                voice = await bot.join_voice_channel(ctx.message.author.voice_channel)
                player = voice.create_ffmpeg_player('dusto.mp3')
                player.start()
                await asyncio.sleep(5)
                voice_client = bot.voice_client_in(ctx.message.server)
                await voice_client.disconnect()

@bot.command(pass_context=True)
async def kq(ctx):
    if "Killer Queen" in (role.name for role in ctx.message.author.roles):
        if ctx.message.author.voice_channel != None:
            voice = await bot.join_voice_channel(ctx.message.author.voice_channel)
            player = voice.create_ffmpeg_player('kq.mp3')
            player.start()
            await asyncio.sleep(2)
            voice_client = bot.voice_client_in(ctx.message.server)
            await voice_client.disconnect()

@bot.command(pass_context=True)
async def rr(ctx):
    if "The World" in (role.name for role in ctx.message.author.roles):
        if ctx.message.author.voice_channel != None:
            voice = await bot.join_voice_channel(ctx.message.author.voice_channel)
            player = voice.create_ffmpeg_player('rr.mp3')
            player.start()
            await asyncio.sleep(3)
            voice_client = bot.voice_client_in(ctx.message.server)
            await voice_client.disconnect()
            
@bot.command(pass_context=True)
async def wry(ctx):
    if "The World" in (role.name for role in ctx.message.author.roles):
        if ctx.message.author.voice_channel != None:
            voice = await bot.join_voice_channel(ctx.message.author.voice_channel)
            player = voice.create_ffmpeg_player('wry.mp3')
            player.start()
            await asyncio.sleep(3)
            voice_client = bot.voice_client_in(ctx.message.server)
            await voice_client.disconnect()
        
@bot.command(pass_context=True)
async def yare(ctx):
    if "Star Platinum" in (role.name for role in ctx.message.author.roles):
        if ctx.message.author.voice_channel != None:
            voice = await bot.join_voice_channel(ctx.message.author.voice_channel)
            player = voice.create_ffmpeg_player('yare.mp3')
            player.start()
            await asyncio.sleep(2)
            voice_client = bot.voice_client_in(ctx.message.server)
            await voice_client.disconnect()

@bot.command(pass_context=True)
async def warudo(ctx):
    if "Star Platinum" in (role.name for role in ctx.message.author.roles):
        if ctx.message.author.voice_channel != None:
            voice = await bot.join_voice_channel(ctx.message.author.voice_channel)
            player = voice.create_ffmpeg_player('sp warudo.mp3')
            player.start()
            await asyncio.sleep(4)
            voice_client = bot.voice_client_in(ctx.message.server)
            await voice_client.disconnect()
    elif "The World" in (role.name for role in ctx.message.author.roles):
        if ctx.message.author.voice_channel != None:
            voice = await bot.join_voice_channel(ctx.message.author.voice_channel)
            player = voice.create_ffmpeg_player('za warudo.mp3')
            player.start()
            await asyncio.sleep(4)
            voice_client = bot.voice_client_in(ctx.message.server)
            await voice_client.disconnect()
        
@bot.command(pass_context=True)
async def creator(ctx):
    await bot.send_message(ctx.message.channel, "Создатель этого бота: <@274809987837198346> (Чара Хиросе).")

@bot.command(pass_context=True) #роли
async def setrole(ctx):
    if ctx.message.author.server_permissions.administrator:
        await bot.create_role(ctx.message.author.server, name="Здоровый", colour=discord.Colour(0xe81414))
        await bot.create_role(ctx.message.author.server, name="В муте", colour=discord.Colour(0xc5c5c5))
        await bot.create_role(ctx.message.author.server, name="На корабле")
        await bot.create_role(ctx.message.author.server, name="Смягчён")
        await bot.create_role(ctx.message.author.server, name="Лёгкий")
        await bot.create_role(ctx.message.author.server, name="Requiem")
        await bot.create_role(ctx.message.author.server, name="Крутится")
        await bot.create_role(ctx.message.author.server, name="Over Heaven")
        await bot.create_role(ctx.message.author.server, name="Alternate")
        await bot.create_role(ctx.message.author.server, name="Ultimate")
        
        #1 ЧАСТЬ
        await bot.create_role(ctx.message.author.server, name="Jonathan Joestar", colour=discord.Colour(0xFFFF00))
        
        #2 ЧАСТЬ
        await bot.create_role(ctx.message.author.server, name="Joseph Joestar", colour=discord.Colour(0xFFFF00))
        await bot.create_role(ctx.message.author.server, name="Kars", colour=discord.Colour(0x8E7CC3))
        
        await bot.create_role(ctx.message.author.server, name="Roflan Crusader", colour=discord.Colour(0xFFD966))
        
        #3 ЧАСТЬ
        await bot.create_role(ctx.message.author.server, name="The World", colour=discord.Colour(0xffff00))
        await bot.create_role(ctx.message.author.server, name="Star Platinum", colour=discord.Colour(0x9d1ef2))
        await bot.create_role(ctx.message.author.server, name="Hermit Purple", colour=discord.Colour(0xcda7e7))
        await bot.create_role(ctx.message.author.server, name="Magician's Red", colour=discord.Colour(0xff0000))
        await bot.create_role(ctx.message.author.server, name="Hierophant Green", colour=discord.Colour(0x33cc3e))
        await bot.create_role(ctx.message.author.server, name="Silver Chariot", colour=discord.Colour(0xdad8f6))
        await bot.create_role(ctx.message.author.server, name="The Fool", colour=discord.Colour(0xecec4e))
        await bot.create_role(ctx.message.author.server, name="Tower of Gray", colour=discord.Colour(0x988e85))
        await bot.create_role(ctx.message.author.server, name="Dark Blue Moon", colour=discord.Colour(0x4444ae))
        await bot.create_role(ctx.message.author.server, name="Strength", colour=discord.Colour(0xb7b7c1))
        await bot.create_role(ctx.message.author.server, name="Ebony Devil", colour=discord.Colour(0xc95555))
        await bot.create_role(ctx.message.author.server, name="Yellow Temperance", colour=discord.Colour(0xf4e317))
        await bot.create_role(ctx.message.author.server, name="Hanged Man", colour=discord.Colour(0xf6f3da))
        await bot.create_role(ctx.message.author.server, name="Emperor", colour=discord.Colour(0xf6f3da))
        await bot.create_role(ctx.message.author.server, name="Empress", colour=discord.Colour(0x6d6739))
        await bot.create_role(ctx.message.author.server, name="Wheel of Fortune", colour=discord.Colour(0x999999))
        await bot.create_role(ctx.message.author.server, name="Justice", colour=discord.Colour(0xf3f3f3))
        await bot.create_role(ctx.message.author.server, name="Lovers", colour=discord.Colour(0xffb7b7))
        await bot.create_role(ctx.message.author.server, name="Sun", colour=discord.Colour(0xffe103))
        await bot.create_role(ctx.message.author.server, name="Death 13", colour=discord.Colour(0x5c1a5c))
        await bot.create_role(ctx.message.author.server, name="Judgement", colour=discord.Colour(0xdddd92))
        await bot.create_role(ctx.message.author.server, name="High Priestess", colour=discord.Colour(0x0000ff))
        await bot.create_role(ctx.message.author.server, name="Geb", colour=discord.Colour(0x8484f7))
        await bot.create_role(ctx.message.author.server, name="Khnum", colour=discord.Colour(0xff00ff))
        await bot.create_role(ctx.message.author.server, name="Tohth", colour=discord.Colour(0x7d7dca))
        await bot.create_role(ctx.message.author.server, name="Anubis", colour=discord.Colour(0xcfc3d8))
        await bot.create_role(ctx.message.author.server, name="Bastet", colour=discord.Colour(0xe3e3c4))
        await bot.create_role(ctx.message.author.server, name="Sethan", colour=discord.Colour(0x8d67a7))
        await bot.create_role(ctx.message.author.server, name="Osiris", colour=discord.Colour(0xf72020))
        await bot.create_role(ctx.message.author.server, name="Horus", colour=discord.Colour(0xc6ffff))
        await bot.create_role(ctx.message.author.server, name="Atum", colour=discord.Colour(0xe31ee3))
        await bot.create_role(ctx.message.author.server, name="Cream", colour=discord.Colour(0xb9b9db))
        
        
        #4 ЧАСТЬ
        await bot.create_role(ctx.message.author.server, name="Crazy Diamond", colour=discord.Colour(0xff00b4))
        await bot.create_role(ctx.message.author.server, name="Killer Queen", colour=discord.Colour(0xe1dada))
        await bot.create_role(ctx.message.author.server, name="Matured", colour=discord.Colour(0xdb1878))
        await bot.create_role(ctx.message.author.server, name="The Hand", colour=discord.Colour(0x0083ff))
        await bot.create_role(ctx.message.author.server, name="Echoes Egg", colour=discord.Colour(0xb6d7a8))
        await bot.create_role(ctx.message.author.server, name="Echoes ACT1", colour=discord.Colour(0xb6d7a8))
        await bot.create_role(ctx.message.author.server, name="Echoes ACT2", colour=discord.Colour(0xb6d7a8))
        await bot.create_role(ctx.message.author.server, name="Echoes ACT3", colour=discord.Colour(0xb6d7a8))
        await bot.create_role(ctx.message.author.server, name="Heaven's Door", colour=discord.Colour(0xf3f3f3))
        await bot.create_role(ctx.message.author.server, name="Aqua Necklace", colour=discord.Colour(0xc3c3f6))
        await bot.create_role(ctx.message.author.server, name="Bad Company", colour=discord.Colour(0x557a44))
        await bot.create_role(ctx.message.author.server, name="Red Hot Chili Pepper", colour=discord.Colour(0xffec00))
        await bot.create_role(ctx.message.author.server, name="The Lock", colour=discord.Colour(0xd41d1d))
        await bot.create_role(ctx.message.author.server, name="Surface", colour=discord.Colour(0x9a5e21))
        await bot.create_role(ctx.message.author.server, name="Love Deluxe", colour=discord.Colour(0xf015cd))
        await bot.create_role(ctx.message.author.server, name="Pearl Jam", colour=discord.Colour(0xe81414))
        await bot.create_role(ctx.message.author.server, name="Achtung Baby", colour=discord.Colour(0xeee5f4))
        await bot.create_role(ctx.message.author.server, name="Ratt", colour=discord.Colour(0x80a96e))
        await bot.create_role(ctx.message.author.server, name="Harvest", colour=discord.Colour(0xe1e11d))
        await bot.create_role(ctx.message.author.server, name="Cinderella", colour=discord.Colour(0xff9fce))
        await bot.create_role(ctx.message.author.server, name="Atom Heart Father", colour=discord.Colour(0xdb1878))
        await bot.create_role(ctx.message.author.server, name="Boy II Man", colour=discord.Colour(0x76768e))
        await bot.create_role(ctx.message.author.server, name="Earth Wind and Fire", colour=discord.Colour(0x3535c5))
        await bot.create_role(ctx.message.author.server, name="Highway Star", colour=discord.Colour(0x313178))
        await bot.create_role(ctx.message.author.server, name="Stray Cat", colour=discord.Colour(0xeebdbd))
        await bot.create_role(ctx.message.author.server, name="Super Fly", colour=discord.Colour(0x909090))
        await bot.create_role(ctx.message.author.server, name="Enigma", colour=discord.Colour(0x070707))
        await bot.create_role(ctx.message.author.server, name="Cheap Trick", colour=discord.Colour(0xb0773d))
        
        
        #5 ЧАСТЬ
        await bot.create_role(ctx.message.author.server, name="Gold Experience", colour=discord.Colour(0xfdd400))
        await bot.create_role(ctx.message.author.server, name="Sticky Fingers", colour=discord.Colour(0x0000ff))
        await bot.create_role(ctx.message.author.server, name="Moody Blues", colour=discord.Colour(0x7b7bb2))
        await bot.create_role(ctx.message.author.server, name="Sex Pistols", colour=discord.Colour(0xffcc05))
        await bot.create_role(ctx.message.author.server, name="Aerosmith", colour=discord.Colour(0x10caff))
        await bot.create_role(ctx.message.author.server, name="Purple Haze", colour=discord.Colour(0xce18ce))
        await bot.create_role(ctx.message.author.server, name="Spice Girl", colour=discord.Colour(0xf5acbc))
        await bot.create_role(ctx.message.author.server, name="King Crimson", colour=discord.Colour(0xecc6c6))
        await bot.create_role(ctx.message.author.server, name="Black Sabbath", colour=discord.Colour(0x032b60))
        await bot.create_role(ctx.message.author.server, name="Soft Machine", colour=discord.Colour(0x032b60))
        await bot.create_role(ctx.message.author.server, name="Kraft Work", colour=discord.Colour(0x0571c7))
        await bot.create_role(ctx.message.author.server, name="Little Feet", colour=discord.Colour(0x9e86ea))
        await bot.create_role(ctx.message.author.server, name="Man in the Mirror", colour=discord.Colour(0xda18f0))
        await bot.create_role(ctx.message.author.server, name="Mr.President", colour=discord.Colour(0xe06666))
        await bot.create_role(ctx.message.author.server, name="Beach Boy", colour=discord.Colour(0xf3f3f3))
        await bot.create_role(ctx.message.author.server, name="The Grateful Dead", colour=discord.Colour(0x8a0ba9))
        await bot.create_role(ctx.message.author.server, name="Baby Face", colour=discord.Colour(0x009aff))
        await bot.create_role(ctx.message.author.server, name="White Album", colour=discord.Colour(0xecfbfb))
        await bot.create_role(ctx.message.author.server, name="Clash", colour=discord.Colour(0x289cbd))
        await bot.create_role(ctx.message.author.server, name="Talking Head", colour=discord.Colour(0xdf6969))
        await bot.create_role(ctx.message.author.server, name="Notorious B.I.G", colour=discord.Colour(0xea60a9))
        await bot.create_role(ctx.message.author.server, name="Metallica", colour=discord.Colour(0xc4ccd6))
        await bot.create_role(ctx.message.author.server, name="Green Day", colour=discord.Colour(0x80a76e))
        await bot.create_role(ctx.message.author.server, name="Oasis", colour=discord.Colour(0xba9936))
        await bot.create_role(ctx.message.author.server, name="Rolling Stones", colour=discord.Colour(0x3e3b3b))
        
        #6 ЧАСТЬ
        await bot.create_role(ctx.message.author.server, name="Stone Free", colour=discord.Colour(0x12ffff))
        await bot.create_role(ctx.message.author.server, name="Kiss", colour=discord.Colour(0xe83be8))
        await bot.create_role(ctx.message.author.server, name="Burning Down the House", colour=discord.Colour(0x131212))
        await bot.create_role(ctx.message.author.server, name="Foo Fighters", colour=discord.Colour(0x494949))
        await bot.create_role(ctx.message.author.server, name="Weather Report", colour=discord.Colour(0xf0ffff))
        await bot.create_role(ctx.message.author.server, name="Diver Down", colour=discord.Colour(0x6dc3ac))
        await bot.create_role(ctx.message.author.server, name="Whitesnake", colour=discord.Colour(0x535387))
        await bot.create_role(ctx.message.author.server, name="C-Moon", colour=discord.Colour(0x03d603))
        await bot.create_role(ctx.message.author.server, name="Made in Heaven", colour=discord.Colour(0xffffff))
        
        #7 ЧАСТЬ
        await bot.create_role(ctx.message.author.server, name="Tusk ACT1", colour=discord.Colour(0xFFB5FF))
        await bot.create_role(ctx.message.author.server, name="Tusk ACT2", colour=discord.Colour(0xFFB5FF))
        await bot.create_role(ctx.message.author.server, name="Tusk ACT3", colour=discord.Colour(0xFFB5FF))
        await bot.create_role(ctx.message.author.server, name="Tusk ACT4", colour=discord.Colour(0xFFB5FF))
        await bot.create_role(ctx.message.author.server, name="Ball Breaker", colour=discord.Colour(0xB6D7A8))
        await bot.create_role(ctx.message.author.server, name="Dirty Deeds Done Dirt Cheap", colour=discord.Colour(0x9BF2FF))
        
        #8 ЧАСТЬ
        await bot.create_role(ctx.message.author.server, name="Soft and Wet", colour=discord.Colour(0xE6FDFD))
        await bot.create_role(ctx.message.author.server, name="Paisley Park", colour=discord.Colour(0xC55252))

        await bot.send_message(ctx.message.author, "Все роли для стендов должны быть добавлены. Можете проверить это в настройках сервера. Выдавать роли нужно самостоятельно. Не рекомендуется выдавать один и тот же стенд сразу двум или более людям.")
        
@bot.command(pass_context=True) #роли
async def removerole(ctx):
    if ctx.message.author.server_permissions.administrator:
        await bot.send_message(ctx.message.author, "Все роли для стендов удалены. Можете проверить это в настройках сервера. Если это не произошло, попробуйте написать эту команду ещё несколько раз.")
        role_delete = discord.utils.find(lambda r: r.name == "Здоровый", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "В муте", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "На корабле", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Смягчён", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Лёгкий", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Requiem", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Крутится", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Over Heaven", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Alternate", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Ultimate", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        
        #1 ЧАСТЬ
        role_delete = discord.utils.find(lambda r: r.name == "Jonathan Joestar", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        
        #2 ЧАСТЬ
        role_delete = discord.utils.find(lambda r: r.name == "Joseph Joestar", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Kars", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        
        role_delete = discord.utils.find(lambda r: r.name == "Roflan Crusader", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        
        #3 ЧАСТЬ
        role_delete = discord.utils.find(lambda r: r.name == 'The World', ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == 'Star Platinum', ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == 'Hermit Purple', ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Magician's Red", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Hierophant Green", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Silver Chariot", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "The Fool", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Tower of Gray", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Dark Blue Moon", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Strength", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Ebony Devil", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Yellow Temperance", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Hanged Man", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Emperor", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Empress", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Wheel of Fortune", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Justice", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Lovers", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Sun", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Death 13", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Judgement", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "High Priestess", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Geb", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Khnum", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Tohth", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Anubis", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Bastet", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Sethan", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Osiris", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Horus", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Atum", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Cream", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        
        #4 ЧАСТЬ
        role_delete = discord.utils.find(lambda r: r.name == 'Crazy Diamond', ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == 'Killer Queen', ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Matured", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == 'The Hand', ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == 'Echoes Egg', ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == 'Echoes ACT1', ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == 'Echoes ACT2', ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == 'Echoes ACT3', ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Heaven's Door", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Aqua Necklace", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Bad Company", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Red Hot Chili Pepper", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "The Lock", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Surface", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Love Deluxe", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Pearl Jam", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Achtung Baby", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Ratt", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Harvest", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Cinderella", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Atom Heart Father", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Boy II Man", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Earth Wind and Fire", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Highway Star", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Stray Cat", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Super Fly", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Enigma", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Cheap Trick", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        
        #5 ЧАСТЬ
        role_delete = discord.utils.find(lambda r: r.name == "Gold Experience", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Sticky Fingers", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Moody Blues", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Sex Pistols", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Aerosmith", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Purple Haze", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Spice Girl", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "King Crimson", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Black Sabbath", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Soft Machine", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Kraft Work", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Little Feet", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Man in the Mirror", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Mr.President", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Beach Boy", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "The Grateful Dead", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Baby Face", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "White Album", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Clash", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Talking Head", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Notorious B.I.G", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Metallica", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Green Day", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Oasis", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Rolling Stones", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        
        
        #6 ЧАСТЬ
        role_delete = discord.utils.find(lambda r: r.name == "Stone Free", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Burning Down the House", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Foo Fighters", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Weather Report", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Diver Down", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Whitesnake", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "C-Moon", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Made in Heaven", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        
        
        #7 ЧАСТЬ
        role_delete = discord.utils.find(lambda r: r.name == "Tusk ACT1", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Tusk ACT2", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Tusk ACT3", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Tusk ACT4", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Ball Breaker", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Dirty Deeds Done Dirt Cheap", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        
        
        #8 ЧАСТЬ
        role_delete = discord.utils.find(lambda r: r.name == "Soft and Wet", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        role_delete = discord.utils.find(lambda r: r.name == "Paisley Park", ctx.message.server.roles)
        await bot.delete_role(ctx.message.author.server, role_delete)
        
        
        
        
        
        
@bot.command(pass_context=True) #Инфа о стендах
async def info(ctx):
    global mutesec
    global charges
    global voicecharge
    global maniq
    global matured
    global muting
    global dcharge
    global stealed
    global degradations
    global degradations2
    global stand_name
    global standability
    global standpic
    global rippleenergy
    global rippleenergy2
    global karss
    if ctx.message.author.id == maniq:
        embed = discord.Embed(title = "Информация о вас:", description = "``Манекен {}``\n``Вами может управлять`` **``Поверхность``**".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a0/SurfaceAnime.png/revision/latest/scale-to-width-down/227?cb=20160513182613")
        await bot.send_message(ctx.message.channel, embed=embed)
        
    #ХАМОН
    if "Jonathan Joestar" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о персонаже **{}**:".format(ctx.message.author.name), description = "Имя: ``Джонатан Джостар``\n``~overdrive (тип) (юзер)``\n``~ovlist - список доступных вам овердрайвов хамона``\n``Энергии хамона: {}``".format(rippleenergy), color = 0xFFFF00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/3f/JonathanP2.png/revision/latest/scale-to-width-down/342?cb=20170223113043")
        await bot.send_message(ctx.message.channel, embed=embed)
        
    elif "Joseph Joestar" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о персонаже **{}**:".format(ctx.message.author.name), description = 'Имя: ``Джозеф Джостар``\n``~overdrive (тип) (юзер)``\n``~ovlist - список доступных вам овердрайвов хамона``\n``Энергии хамона: {}``\n``~s (текст) - "И следующее, что ты скажешь: "``'.format(rippleenergy2), color = 0xFFFF00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/43/JosephJoestar123.png/revision/latest/scale-to-width-down/270?cb=20170521193900")
        await bot.send_message(ctx.message.channel, embed=embed)
        
    elif "Kars" in (role.name for role in ctx.message.author.roles):
        if "Ultimate" in (role.name for role in ctx.message.author.roles):
            embed = discord.Embed(title = "Информация о персонаже **{}**:".format(ctx.message.author.name), description = "Имя: ``Карс, ставший совершенным существом``\n``Пассивка: вас нельзя замутить, использовать на вас любую абилку``\n``~attacker - замутить на {} секунд и получить энергию``".format(karss), color = 0xFFFF00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/43/KarsExposed.png/revision/latest?cb=20131127012039")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о персонаже **{}**:".format(ctx.message.author.name), description = "Имя: ``Карс``\n``~aja - надеть красный камень эйша в маску``\n``~attacker - замутить на {} секунд``\n``~posseser (юзер) - поглотить пользователя хамона (Джонатан или Джозеф)``".format(karss), color = 0xFFFF00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/18/KarsA.png/revision/latest/scale-to-width-down/270?cb=20161029000057")
        await bot.send_message(ctx.message.channel, embed=embed)
        
    #ОСОБЫЙ СТЕНД
    elif "Roflan Crusader" in (role.name for role in ctx.message.author.roles): #РОФЛАНОСЕЦ
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Рофланосец Реквием``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~rofl - случайное рофланебало в чат``\n``~degr - заставить человека деградировать 45 секунд``\n``~ultradegr - заставить деградировать всех 7 секунд``".format(ctx.message.author.name), color = 0x000000)
            embed.set_image(url="https://cdn.discordapp.com/attachments/472313657661980672/474521075846348800/unknown.png")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        if "Over Heaven" in (role.name for role in ctx.message.author.roles):
            degradations2 = round(degradations / 2.5)
            if degradations2 < 0:
                degradations2 = 0
            embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Рофланосец: Над небом``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~rofl - случайное рофланебало в чат``\n``~degr - заставить человека деградировать {} секунд``\n``~ultradegr - заставить деградировать всех {} секунд``\n``~charge - зарядить деградацию``".format(ctx.message.author.name, degradations, degradations2), color = 0x000000)
            embed.set_image(url="https://cdn.discordapp.com/attachments/472313657661980672/474521075846348800/unknown.png")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Рофланосец``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~rofl - случайное рофланебало в чат``\n``~degr - заставить человека деградировать 35 секунд``".format(ctx.message.author.name), color = 0x000000)
        embed.set_image(url="https://cdn.discordapp.com/attachments/472313657661980672/474521075846348800/unknown.png")
        await bot.send_message(ctx.message.channel, embed=embed)
        
    #3 ЧАСТЬ
    elif "The World" in (role.name for role in ctx.message.author.roles): #МИР
        if "Over Heaven" in (role.name for role in ctx.message.author.roles):
            embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Мир: Над небом``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~world - «остановить время» на 12 секунд в чате``\n``~muda - замутить человека на 9 секунд`` **``МУДА МУДА МУДА``**".format(ctx.message.author.name), color = 0x9494e5)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b2/Twoh.png/revision/latest/scale-to-width-down/350?cb=20151229005251")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Мир``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~world - «остановить время» на 6 секунд в чате``\n``~muda - замутить человека на 7 секунд`` **``МУДА МУДА МУДА``**".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/41/TheWorld_AnimeAV.png/revision/latest/scale-to-width-down/270?cb=20160414095701")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Star Platinum" in (role.name for role in ctx.message.author.roles): #СП
        if "Over Heaven" in (role.name for role in ctx.message.author.roles):
            embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Платиновая звезда: Мир над небом``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~ora - замутить человека на 8 секунд`` **``ORA ORA ORA``**\n``~world - «остановить время» на 9 секунды в чате``".format(ctx.message.author.name), color = 0x9494e5)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/ae/SPTW_AV.png/revision/latest/scale-to-width-down/270?cb=20160715195842")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Платиновая звезда``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~ora - замутить человека на 5 секунд`` **``ORA ORA ORA``**\n``~world - «остановить время» на 4 секунды в чате``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/ae/SPTW_AV.png/revision/latest/scale-to-width-down/270?cb=20160715195842")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Hermit Purple" in (role.name for role in ctx.message.author.roles): #ХП
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Лиловый проповедник``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~divine - получить информацию о стенде кого-нибудь``\n``~ripple - защитить себя или кого-то от атак``\n``~unripple - снять защиту``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/1f/PurpleHermit_AnimeAV.png/revision/latest?cb=20160414095805")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Magician's Red" in (role.name for role in ctx.message.author.roles): #МР
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Алый Маг``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~ignite - зажечь кого-нибудь``\n``~crossfire - зажечь всех на 5 секунд (ураган)``\n``~unignite - потушить``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/9/97/Magician%27s_Red_AnimeAV.png/revision/latest/scale-to-width-down/327?cb=20160414185722")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Hierophant Green" in (role.name for role in ctx.message.author.roles): #ХГ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Зелёный проповедник``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~splash - замутить на 4 секунды``\n``~marionette - сделать человека марионеткой``\n``~mar (слова) - писать от его имени``\n``~unpuppet - снять марионетку``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d0/HierophantGreen_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414185638")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Silver Chariot" in (role.name for role in ctx.message.author.roles): #СЧ
        if "Requiem" in (role.name for role in ctx.message.author.roles): #СЧР
            embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Колесница Реквием``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: пытаясь писать в муте, вы размутите себя``\n``~self (юзер) - заставить стенд кого-то атаковать владельца (работает не на всех)``\n``~swordr (юзер 1) (юзер 2) (юзер 3) - замутить на 4 секунды``".format(ctx.message.author.name), color = 0x9494e5)
            embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/482449676495355904/unknown.png")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Серебряная колесница``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~speed - даёт возможность увернуться от мута (5 секунд)``\n``~sword - замутить на 4 секунды``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/88/SilverChariot_AnimeAV.png/revision/latest/scale-to-width-down/270?cb=20160414095744")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "The Fool" in (role.name for role in ctx.message.author.roles): #ШУТ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Шут``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~shift - взять имя у кого-нибудь``\n``~nshift - взять ник``\n``~unshift - вернуть свой ник``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/07/Fool_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101341")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Tower of Gray" in (role.name for role in ctx.message.author.roles): #ТАВЕР ОФ ГРЕЙ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Башня Сумерек``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: шанс 1/2 увернуться от атаки``\n``~jaw - отравить человека``\n``~unjaw - снять отраву``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414185549")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Dark Blue Moon" in (role.name for role in ctx.message.author.roles): #ДБМ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Тёмно-синяя Луна``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~barn - прицепить моллюск``\n``~unbarn - убрать моллюск``\n``~barninfo - проверить моллюска``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e9/DarkBlueMoon_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414192329")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Strength" in (role.name for role in ctx.message.author.roles): #СИЛА
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Сила``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: те, кто на корабле имеют защиту от остальных атак, но их можно атаковать этим стендом.``\n``~join - зайти на корабль (ВСЕМ)``\n``~shiptack - убрать возможность писать всем, кто на корабле``\n``~unshiptack - вернуть возможность писать всем, кто на корабле``\n``~take - выбросить с корабля``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/ec/Strength_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414095727")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Ebony Devil" in (role.name for role in ctx.message.author.roles): #ДЬЯВОЛ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Дьявол``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: чем больше вас атакуют, тем на большее время вы можете мутить``\n``~dev - замутить на`` **``{}``** ``секунд``".format(ctx.message.author.name, mutesec), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/57/Ebony_Devil-AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414185656")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Yellow Temperance" in (role.name for role in ctx.message.author.roles): #ЕТ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Жёлтая Умеренность``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~skill - написав это, вы не сможете использовать этот стенд, но подождав 5 минут, вы станете сильнее и снова сможете его использовать``\n``~slime - атаковать слизью``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/fb/YellowTemperance_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414185535")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Hanged Man" in (role.name for role in ctx.message.author.roles): #ПОВЕШЕННЫЙ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Повешенный``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~hang - отзеркалить сообщения``\n``~unhang - убрать зеркало``\n``~mirror - напасть на зазеркаленного``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d3/HangedMan_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101324")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Emperor" in (role.name for role in ctx.message.author.roles): #ЭМПЕРОР
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Император``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: если тот, кого вы атаковали напишет хоть одно сообщение - вы сможете атаковать снова``\n``~emp - выстрелить (шанс 1/2)``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/9/9d/Emperor_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101400")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Empress" in (role.name for role in ctx.message.author.roles): #ИМПРЕСС
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Императрица``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: начав паразитировать на ком-то, через некоторое время у вас спадёт стенд и вы попадёте в мут на 30 минут.``\n``~empress (слово) - если человек напишет это`` **``СЛОВО``**, ``вы начнёте паразитировать на нём``\n``~harm - замутить на 5 секунд человека, на котором паразитируете``\n``~unempress - снять слово``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/10/Empress_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101349")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Wheel of Fortune" in (role.name for role in ctx.message.author.roles): #ВОФ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Колесо Фортуны``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~atrandom - замутить себя или кого на 10 минут (шанс 1/2).``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/28/WOF_AnimeAV.png/revision/latest/scale-to-width-down/340?cb=20160414095637")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Justice" in (role.name for role in ctx.message.author.roles): #ДЖАСТИС
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Справедливость``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~manipulate (юзер) (слова) - манипулировать кем-то (заставить написать слова)``\n``~unman - перестать манипулировать``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/4d/Justice_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101110")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Lovers" in (role.name for role in ctx.message.author.roles): #ЛАВЕРС
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Влюблённые``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: если вы попадёте в мут, то в мут попадёт и человек, в которого вы переместили свой стенд``\n``~love - переместить свой стенд в кого-то``\n``~lovemute - замутить себя на 5 минут``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/06/Lovers_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414185608")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Sun" in (role.name for role in ctx.message.author.roles): #СОЛНЦЕ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Солнце``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~charge - зарядить энергией``\n``~hot - прислать {} уведомлений в ЛС``\n``~sun - опалить лучом на {} секунд``".format(ctx.message.author.name, charges, charges), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/ff/Sun_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414095719")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Death 13" in (role.name for role in ctx.message.author.roles): #СМЕРТЬ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Смерть тринадцать``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~scythe - замутить на минуту себя или кого-то (шанс 1/2)``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/34/Death13_AnimeAV.png/revision/latest/scale-to-width-down/322?cb=20160414101418")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Judgement" in (role.name for role in ctx.message.author.roles): #КАМЕО
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Суд``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~hail (юзер) - исполнить`` ~~**``?!желание?!``**~~".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/8e/Judgment_AnimeAV.png/revision/latest/scale-to-width-down/340?cb=20160414192321")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "High Priestess" in (role.name for role in ctx.message.author.roles): #ЖРИЦА
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Жрица``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~posses - ненадолго завладеть кем-то``\n``~unposses - перестать владеть``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/11/Priestess_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414095813")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Geb" in (role.name for role in ctx.message.author.roles): #ГЕБ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Геб``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~unignite - потушить всё пламя``\n``~water - атаковать водой человека в войсе``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/c7/Geb_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101332")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Khnum" in (role.name for role in ctx.message.author.roles): #ХНУМ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Хнум``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~transfigure - преобразоваться в кого-то``\n``~unfigure - войти в нормальную форму``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/84/Khnum_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101100")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Tohth" in (role.name for role in ctx.message.author.roles): #ТОТ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Тот``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~comics (человек со стендом`` **``Хнума``**``) - получить в ЛС комикс, контроллирующий пользователей``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/82/Tohth_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414095654")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Anubis" in (role.name for role in ctx.message.author.roles): #АНУБИС
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Анубис``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: вы не можете пользоваться своим стендом, пока его не возьмёт другой человек``\n``~anubis - написав эту команду, активируется ваш стенд и можно будет использовать меч (для остальных)``\n``~swordbis - можно атаковать мечом, если стенд активен (для остальных)``\n``~destroy - замутить человека, взявшего меч, и деактивировать стенд (обладатель стенда)``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f0/Anubis_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101457")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Bastet" in (role.name for role in ctx.message.author.roles): #ТОТ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Баст``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~shock - после каждого сообщения, этому человеку будут спамить в ЛС``\n``~unshock - убрать шок``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/5b/Bastet_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101441")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Sethan" in (role.name for role in ctx.message.author.roles): #СЕТ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Сет``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~babys - убрать у кого-нибудь возможность использовать свой стенд на 10 минут, отключив свой на это время``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/29/Sethan_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414185518")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Osiris" in (role.name for role in ctx.message.author.roles): #ОСИРИС
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Осирис``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~play - сыграть в угадайку с кем-нибудь``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/7b/Osiris_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101007")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Horus" in (role.name for role in ctx.message.author.roles): #ПЕТ ШОП
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Хор``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~freeze - заморозить одну команду``\n``~ice - атаковать льдом``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/64/Horus_AnimeAV.png/revision/latest/scale-to-width-down/348?cb=20160414101249")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Atum" in (role.name for role in ctx.message.author.roles): #ДАРБИ СТАРШИЙ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Атум``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~vplay - сыграть в гонку с кем-нибудь``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/bd/Atum_AnimeAV.png/revision/latest/scale-to-width-down/333?cb=20160414101449")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Cream" in (role.name for role in ctx.message.author.roles): #КРЕМ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Крем``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~void - затягивать в пустоту сообщения``\n``~unvoid - выпустить из пустоты``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/57/Cream_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101433")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        
    #4 ЧАСТЬ
    
    
    elif "Crazy Diamond" in (role.name for role in ctx.message.author.roles): #ББ
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Безумный Алмаз Реквием``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~dorara - замутить на 5 секунд и размутить``\n``~untime - отменить все остановки времени``".format(ctx.message.author.name), color = 0xff00ff)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/c5/Crazy_Diamond_Anime.png/revision/latest/scale-to-width-down/350?cb=20160414081459")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Безумный Алмаз``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~heal - размутить и вылечить яд крысы``\n``~dorara - замутить на 5 секунд``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/c5/Crazy_Diamond_Anime.png/revision/latest/scale-to-width-down/350?cb=20160414081459")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Killer Queen" in (role.name for role in ctx.message.author.roles): #КК
        if "Alternate" in (role.name for role in ctx.message.author.roles):
            embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Смертельная королева (Альтернативная)``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~bubble - замутить на 10 секунд (задержка 60 секунд)``\n``~bombcheck - проверить бомбы``\n``~sha - если этот человек что-то напишет - попадёт в мут на 5 секунд``\n``~sha2 - если этот человек что-то напишет - попадёт в мут на 5 секунд``\n``~sha3 - если этот человек что-то напишет - попадёт в мут на 5 секунд``\n``~sha4 - если этот человек что-то напишет - попадёт в мут на 5 секунд``".format(ctx.message.author.name), color = 0xff00ff)
            embed.set_image(url="https://cdn.discordapp.com/attachments/473403386599964672/483485245086105630/unknown.png")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        if "Matured" not in (role.name for role in ctx.message.author.roles):
            embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Смертельная королева``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~shibo - замутить на 3 секунды``\n``~bomb - поставить бомбу на человека, и тот, кто его упомянёт попадёт в мут на 10 минут (первая бомба)``\n``~bombcheck - проверить первую бомбу``\n``~sha - если этот человек что-то напишет - попадёт в мут на 5 секунд (вторая бомба)``\n**``??? - (третья бомба?!)``**".format(ctx.message.author.name), color = 0xff00ff)
        else:
            embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Смертельная королева``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~shibo - замутить на 3 секунды``\n``~bomb - поставить бомбу на человека, и тот, кто его упомянёт попадёт в мут на 10 минут (первая бомба)``\n``~bombcheck - проверить первую бомбу``\n``~sha - если этот человек что-то напишет - попадёт в мут на 5 секунд (вторая бомба)``\n**``~bite - (третья бомба?!)``**".format(ctx.message.author.name), color = 0xff0000)
            await bot.send_message(ctx.message.author, "**ТРЕТЬЯ БОМБА УБИЙСТВЕННОЙ КОРОЛЕВЫ: ПЫЛЬНЫЙ УКУС**\n``Активировав её, вас нельзя будет упоминать, читать книгой: тот, кто это сделает попадёт в мут, а чат откатится.``")
        embed.set_image(url="https://cdn.discordapp.com/attachments/472313657661980672/472316805763956756/unknown.png")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "The Hand" in (role.name for role in ctx.message.author.roles): #РУКА
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Рука``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~erase - стереть пространство``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/46/The_Hand_Anime.png/revision/latest/scale-to-width-down/350?cb=20160429212824")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Echoes Egg" in (role.name for role in ctx.message.author.roles): #ЭХО
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Эхо``\nВладелец стенда: ``{}``\nСпособности стенда:\n**``???``**".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/ce/Echoes_Egg_Form.png")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Echoes ACT1" in (role.name for role in ctx.message.author.roles): #ЭХО АКТ1
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Эхо``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~sound (юзер) (слово) - генерация звука``\n``~mutesound - перестать создавать звук``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/62/ACT1_AV.png/revision/latest/scale-to-width-down/270?cb=20160520170003")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Echoes ACT2" in (role.name for role in ctx.message.author.roles): #ЭХО АКТ2
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Эхо``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~soundtwo (юзер) (слово) - особенная генерация звука``\n``~mutesound - перестать создавать звук (от 1 и 2 акта)``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/19/EchoesACT2_AV.png/revision/latest/scale-to-width-down/270?cb=20160527173808")
        await bot.send_message(ctx.message.channel, embed=embed)
        await bot.send_message(ctx.message.author, "**ОСОБЫЕ ЗВУКИ** - если одно из этих слов содержится в *генерации звука*, будет особый эффект.\n``ОГЛУШЁН``\n``ГРОМКИЙ``\n``ГНЕВ``")
    elif "Echoes ACT3" in (role.name for role in ctx.message.author.roles): #ЭХО АКТ3
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Эхо``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~ffreeze - заморозить``\n``~mutesound - перестать создавать звук (от 1 и 2 акта)``\n``~unfreeze - разморозить``\n``~unevolve - вернуться к форме яйца``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/31/EchoesACT3_AV.png/revision/latest/scale-to-width-down/270?cb=20160909173528")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Heaven's Door" in (role.name for role in ctx.message.author.roles): #ХЕВЕН ДОР
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Райские врата``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~book - превратить в книгу``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/de/Heaven%27s_Door_AV.png/revision/latest/scale-to-width-down/270?cb=20160923180054")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Aqua Necklace" in (role.name for role in ctx.message.author.roles): #ВОДНОЕ ОЖЕРЕЛЬЕ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Водное ожерелье``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~aqua - заставить сообщения растекаться``\n``~unaqua - избавиться от течения``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/4f/Aqua_Necklace_AV.png/revision/latest/scale-to-width-down/350?cb=20160414095501")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Bad Company" in (role.name for role in ctx.message.author.roles): #ПК
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Плохая компания``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~soldier - атаковать солдатами (для остальных)``\n``~tank - атаковать танком (для остальных)``\n``~para - атаковать парашютистами (для остальных)``\n``~heli - атаковать вертолётами (для остальных)``\n``~targetbad - поставить цель``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/12/BadCo_AV.png/revision/latest/scale-to-width-down/350?cb=20160422191814")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Red Hot Chili Pepper" in (role.name for role in ctx.message.author.roles): #РХЧП
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Острый красный Чили Перец``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~charge - зарядить (вы должны быть в войсе)``\n``~el - замутить на {} секунд``".format(ctx.message.author.name, voicecharge), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/0e/RHCP_Anime.png/revision/latest/scale-to-width-down/350?cb=20160617173431")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "The Lock" in (role.name for role in ctx.message.author.roles): #ЗАМОК
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Замок``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~lock - закрепить на ком-то замок``\n``~mcheck - проверить кол-во монет``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Surface" in (role.name for role in ctx.message.author.roles): #Поверхность
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Поверхность``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~manq - сделать человека куклой``\n``~mimicry - превратить куклу в кого-то``\n``~unmanq - убрать превращение и куклу``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a0/SurfaceAnime.png/revision/latest/scale-to-width-down/227?cb=20160513182613")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Love Deluxe" in (role.name for role in ctx.message.author.roles): #ЛАВ ДЕЛЮКС
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Любовь Делюкс``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~lovedeluxe (буква или слова) - стирать данное слово (букву) каждый раз, когда хоть кто-то пишет сообщение``\n``~undel - убрать слово``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e9/Love_Deluxe_AV.png/revision/latest/scale-to-width-down/350?cb=20160527174230")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Pearl Jam" in (role.name for role in ctx.message.author.roles): #ПЁРЛ ДЖЕМ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Жемчужный Джем``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~feed - замутить человека на 5 минут, а затем дать ему возможность увернуться от следующего мута``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/3f/Pearl_Jam_Anime_Closeup.png/revision/latest/scale-to-width-down/270?cb=20160603192620")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Achtung Baby" in (role.name for role in ctx.message.author.roles): #МАЛЫШ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Опасный Малыш``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: пытаясь писать в муте, вы будете делать сообщения`` *``невидимыми``*".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/6f/Achtung_Baby_AV.png/revision/latest/scale-to-width-down/350?cb=20160924071026")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Ratt" in (role.name for role in ctx.message.author.roles): #КРЫСА
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Крыса``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~poishot - выстрелить ядом``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/59/Ratt_summoned.png/revision/latest/scale-to-width-down/640?cb=20160715205844")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Harvest" in (role.name for role in ctx.message.author.roles): #ЖАТВА
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Собиратель``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: каждый раз когда кто-то отправляет рофлан-ебало (не считая вас), вы получаете монетку``\n``~collects - проверить прайс-лист за рофлан-койны и кол-во монет``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b6/Harvestanime.png/revision/latest/scale-to-width-down/350?cb=20160729214906")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Cinderella" in (role.name for role in ctx.message.author.roles): #ЗОЛУШКА
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Золушка``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~form (юзер) - дать возможность кому-то сменить ник``\n``~newname (ник) - поставить новый ник (для тех, на кого использовали стенд)``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/0c/Cinderella_AV.png/revision/latest/scale-to-width-down/350?cb=20160812174646")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Atom Heart Father" in (role.name for role in ctx.message.author.roles): #ОТЕЦ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Отец с атомным сердцем``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~arrow - лук со стрелой``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/3c/AHF_AV.png/revision/latest/scale-to-width-down/350?cb=20160916171054")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Boy II Man" in (role.name for role in ctx.message.author.roles): #КНБ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Мужественный парень``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~rps - сыграть в камень-ножницы-бумага``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/5f/Boy_II_Man_KeyArt.png/revision/latest/scale-to-width-down/329?cb=20161228082527")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Earth Wind and Fire" in (role.name for role in ctx.message.author.roles): #EWF
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Земля, Огонь и Ветер``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: вас нельзя замутить``\n``~morph - сменить себе ник``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/9/9d/EW%26F_AV.png/revision/latest/scale-to-width-down/348?cb=20160930175920")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Highway Star" in (role.name for role in ctx.message.author.roles): #HS
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Звезда автострады``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~room (название) - создать новый приватный канал, который удалится через минуту``\n``~suck - высосать жизненную энергию (в следующий раз, когда вы будете в муте, вы будете размучены, а этот человек попадёт на 7 минут в мут)``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/ca/Highway_Star_AV.png/revision/latest/scale-to-width-down/350?cb=20161014210104")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Stray Cat" in (role.name for role in ctx.message.author.roles): #СК
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Бродячий Кот``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~airshoot - замутить на 6 секунд``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/aa/Stray_Cat_first_appearance.png/revision/latest/scale-to-width-down/640?cb=20161021205006")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Super Fly" in (role.name for role in ctx.message.author.roles): #СФ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Вздымающийся``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~reflect (юзер) - если вы будете пытаться писать в муте, замутят и данного человека``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/c1/Super_Fly_AV.png/revision/latest/scale-to-width-down/329?cb=20161028170755")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Enigma" in (role.name for role in ctx.message.author.roles): #ЭНИГМА
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Загадка``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: превращённый в бумагу больше не сможет использовать команды. Однако, если вас замутят, все бумажки пропадут.``\n``~paper - превратить в бумагу человека, написавшего вут-фейс``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/c1/Enigma_AV.png/revision/latest/scale-to-width-down/350?cb=20161111210722")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Cheap Trick" in (role.name for role in ctx.message.author.roles): #ЧИП ТРИК
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Дешёвый трюк``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~whisper (юзер) (слова) - шептать``".format(ctx.message.author.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/55/Cheap_Trick_AV.png/revision/latest/scale-to-width-down/346?cb=20161118192225")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        
        
        
        
    #5 ЧАСТЬ
    elif "Gold Experience" in (role.name for role in ctx.message.author.roles): #ЗО
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Золотой ветер Реквием``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: если вы напишите сообщение в муте - мут пропадёт``\n``~muda - замутить на 4 секунды``\n``~glife - создать жизнь``\n``~zero - убрать возможность пользоваться командами этого бота``".format(ctx.message.author.name), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a7/GER_Profile.png/revision/latest/scale-to-width-down/350?cb=20160414114347")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Золотой ветер``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: если вы напишите сообщение в муте - мут пропадёт``\n``~muda - замутить на 4 секунды``\n``~glife - создать жизнь``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/482250418206801932/cb8e42b3d77f1dbd.PNG")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Sticky Fingers" in (role.name for role in ctx.message.author.roles): #МОЛНИЯ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Липучие Пальцы``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: каждое сообщение от вас в застёжке - мут на 5 секунд``\n``~zip - сделать застёжку``\n``~zipper - ARIARIARI``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/dd/StickyFingers.png/revision/latest/scale-to-width-down/307?cb=20150428184345")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Moody Blues" in (role.name for role in ctx.message.author.roles): #2МАДИ БЛУС
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Угрюмый Джаз``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~record - начать записывать все сообщения человека в ЛС на 5 минут``\n``~stop - завершить запись``\n``~urya - замутить на 4 секунды``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/482253362620792852/aa17535292bee228.PNG")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Sex Pistols" in (role.name for role in ctx.message.author.roles): #Шесть пуль
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Шесть пуль``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~bully (юзер 1) (юзер 2) (юзер 3) (юзер 4)  - замутить`` **``4``** ``человека на 5 минут``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/484774724484726806/maxresdefault_3.jpg")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Aerosmith" in (role.name for role in ctx.message.author.roles): #АЭРОКУЗНИЦА
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Аэрокузница``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~aero (юзер 1) (юзер 2) - замутить 2-ух юзеров на 10 минут, но в это время нельзя использовать свои команды``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a5/Aerosmith.png/revision/latest/scale-to-width-down/350?cb=20170610062644")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Purple Haze" in (role.name for role in ctx.message.author.roles): #ФТ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Фиолетовый туман``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~virused - заразить вирусом, который через некоторое время исчезнет``\n``~ubasha - замутить на 3 секунды``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/1c/PurpleHaze.png/revision/latest/scale-to-width-down/335?cb=20150429070459")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Spice Girl" in (role.name for role in ctx.message.author.roles): #SG
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Спайс Гёрл``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~soft - замутить на 3 секунды и забрать возможность один раз воспользоваться стендом``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/df/Spice_Girl.png/revision/latest/scale-to-width-down/350?cb=20160413153303")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "King Crimson" in (role.name for role in ctx.message.author.roles): #KING CRIMSON
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Кроваво-красный Король``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~timeerase - стереть время``\n``~punch - замутить на 6 секунд (в стёртом времени 10)``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f9/KingCrimson.png/revision/latest/scale-to-width-down/350?cb=20170204065902")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Black Sabbath" in (role.name for role in ctx.message.author.roles): #BS
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Чёрная Суббота``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: если в вас выстрелят стрелой, вы заберёте её.``\n``~dshadow (юзер) - замутить на 10 секунд (до 16 часов)``\n``~vshadow (юзер 1) (юзер 2) - замутить на 5 секунд (после 16 часов)``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/3a/Black_Sabbath.png/revision/latest/scale-to-width-down/350?cb=20160320054224")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Soft Machine" in (role.name for role in ctx.message.author.roles): #SM
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Мягкая Машина``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~deflate - сделать`` *``лёгким``*\n``Пассивка: лёгкие вещи могут увернуться от следующего мута, но не смогут пользоваться командами``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f9/SoftMachine.png/revision/latest?cb=20150429071004")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Kraft Work" in (role.name for role in ctx.message.author.roles): #KW
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Крафт Ворк``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~llock - убрать пользователю писать возможность в канал, в котором вы использовали эту команду (на 5 минут)``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d0/KraftWork.png/revision/latest/scale-to-width-down/350?cb=20150429071412")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Little Feet" in (role.name for role in ctx.message.author.roles): #LF
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Крохотные Лапки``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~shrink - уменьшить``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/56/ManInTheMirror_first.png/revision/latest/scale-to-width-down/339?cb=20161231090359")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Man in the Mirror" in (role.name for role in ctx.message.author.roles): #LF
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Человек в зеркале``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~createmirror (юзер) - создать канал, в который открыт доступ вам и этому юзеру. Он будет уничтожен через 1 минуту.``\n``Пассивка: в этом канале вы сможете использовать стенд, а тот юзер, которого вы затащите - нет.``\n``~mirattack - атаковать зазеркаленного``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/56/ManInTheMirror_first.png/revision/latest/scale-to-width-down/339?cb=20161231090359")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Mr.President" in (role.name for role in ctx.message.author.roles): #ПРЕЗИДЕНТ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Президент``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~hide - спрятать на минуту от мута``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d9/Coco_Jumbo_Room_Color.png/revision/latest/scale-to-width-down/350?cb=20160517160222")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Beach Boy" in (role.name for role in ctx.message.author.roles): #BB
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Рыбак``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: пока мут есть, вы не можете использовать свои команды``\n``~hook - замутить человека в войсе на 10 минут``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/32/Beach_Boy.png/revision/latest/scale-to-width-down/336?cb=20160426155655")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "The Grateful Dead" in (role.name for role in ctx.message.author.roles): #BB
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Благодарный Мертвец``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~age - дать возможность написать сообщение в муте``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/70/The_Grateful_Dead.png/revision/latest/scale-to-width-down/339?cb=20150521171134")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Baby Face" in (role.name for role in ctx.message.author.roles): #BF
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Детское Лицо``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: чем больше используют команд бота, тем на большее время мут (заряды в это не входят)``\n``~homu - замутить на`` **``{}``** ``секунд``".format(ctx.message.author.name, muting), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d2/BabyFacePro.png/revision/latest/scale-to-width-down/350?cb=20170629221729")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "White Album" in (role.name for role in ctx.message.author.roles): #WA
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Белый Альбом``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка - ледяная броня: когда вас замутят, следующий, кто напишет сообщение не сможет использовать команды бота``\n``~temp - замутить на 4 секунды`` *``зафриженного юзера``*".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/da/WhiteAlbum.png/revision/latest/scale-to-width-down/338?cb=20150523161426")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Clash" in (role.name for role in ctx.message.author.roles): #КЛЭШ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Клэш``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~liq (юзер) - замутить на 3 секунды (если юзер в голосовом, на 5)``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/fb/Clash.png/revision/latest/scale-to-width-down/350?cb=20171024042957")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Talking Head" in (role.name for role in ctx.message.author.roles): #TH
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Разговорчивая Голова``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~lie (юзер) - переместить свой стенд в кого-то``\n``~lying (слово) (слова или слово) - заменять слова``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e5/Talking_Head.png/revision/latest/scale-to-width-down/350?cb=20160320054512")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Notorious B.I.G" in (role.name for role in ctx.message.author.roles): #NB
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Печально-известный B.I.G``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: командами этого стенда можно пользоваться в муте``\n``~enabsorb - атаковать (атаковав Солнце или РХЧП, вы заберёте у него всю энергию)``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/ef/NotoriousBIG.png/revision/latest?cb=20170620043550")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Metallica" in (role.name for role in ctx.message.author.roles): #МЕТАЛЛ
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Металлика``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~invisible - сделать невидимым``\n``~vis - сделать видимым``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/18/Metallica_AV.png/revision/latest/scale-to-width-down/350?cb=20160423084036")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Green Day" in (role.name for role in ctx.message.author.roles): #GD
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Зелёный Денёк``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: заплесневевший пользователь не сможет вас атаковать``\n``~mold (юзер) - заплесневеть``\n``~unmold (юзер) - убрать плесень``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f8/Green_Day.png/revision/latest?cb=20161231083726")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Oasis" in (role.name for role in ctx.message.author.roles): #ОАЗИС
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Оазис``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~ground (юзер 1) (юзер 2) - атаковать пользователей не в войсе``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/ae/Oasis_Stand.png/revision/latest/scale-to-width-down/350?cb=20170612181607")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Rolling Stones" in (role.name for role in ctx.message.author.roles): #РС
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Роллинг Стоунс``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~stone - дать вечный мут, муту на время (на одного человека, снимется сам, если вы переключите)``\n``~unstone - убрать вечный мут``".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/86/Rolling_Stones.png/revision/latest/scale-to-width-down/350?cb=20140822162552")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        
    #6 ЧАСТЬ (СТЕНДЫ)
    elif "Stone Free" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Каменная Свобода``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка:``\n``1) нитка может быть всего 1``\n``2) нить не может пользоваться стендом``\n``3) на нить не действует мут``\n``~stringed - превратить объект в нить``\n``~unstring - превратить обратно``\n``~ora - замутить на 4 секунды``".format(ctx.message.author.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/75/StonefreeP.png/revision/latest/scale-to-width-down/317?cb=20160417073326")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Kiss" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Поцелуй``\nВладелец стенда: ``{}``\n``~dub - дублировать стенд``".format(ctx.message.author.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/0f/KissP.png/revision/latest?cb=20170109190909")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Burning Down the House" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Поджог Дома``\nВладелец стенда: ``{}``\n``Пассивка: призраком может стать лишь один, они могут писать в муте, но не использовать команды. Нельзя использовать на себя.``\n``~ghost - превратить в призрака``\n``~unghost - снять превращение``".format(ctx.message.author.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/61/BDtHP.png/revision/latest/scale-to-width-down/350?cb=20150607141943")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Foo Fighters" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Фу Файтерс``\nВладелец стенда: ``{}``\n``~invasion - пересылать удалённые сообщения юзера вам в ЛС``\n``~plankton - замутить на`` **``(3-7)``** ``секунд``".format(ctx.message.author.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/4d/FooP.png/revision/latest/scale-to-width-down/328?cb=20170109053755")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Weather Report" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Прогноз Погоды``\nВладелец стенда: ``{}``\n``~wset - поставить погоду``\n``~wlist - список погодных условий``".format(ctx.message.author.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/42/WeatherRP.png/revision/latest/scale-to-width-down/350?cb=20150607144211")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Diver Down" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Водолаз``\nВладелец стенда: ``{}``\n``Пассивка: каждый раз когда вы пишите в муте - получаете заряд``\n``~diver - замутить на {} секунд``".format(ctx.message.author.name, dcharge), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/ee/DiveP.png/revision/latest/scale-to-width-down/350?cb=20170629083510")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Whitesnake" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Белая Змея``\nВладелец стенда: ``{}``\n``~extract - извлечь диск из кого-нибудь``\n``~insert - загрузить диск в кого-нибудь``".format(ctx.message.author.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/dc/Howaitosuneiku.png/revision/latest/scale-to-width-down/295?cb=20170101020857")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "C-Moon" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Луна``\nВладелец стенда: ``{}``\n``~gravity - сообщения вверх ногами у всех``".format(ctx.message.author.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e6/C-Moon.png/revision/latest?cb=20170101001516")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Made in Heaven" in (role.name for role in ctx.message.author.roles):
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Прямиком из Рая Реквием``\nВладелец стенда: ``{}``\n``Пассивка: если ускорять время слишком часто, может создаться новая`` *``вселенная``*\n``~aceltime - ускорить время``\n``~newstand - создать стенд``".format(ctx.message.author.name), color = 0x12ffff)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/27/MadeinHeaven.png/revision/latest/scale-to-width-down/312?cb=20140924111429")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Прямиком из Рая``\nВладелец стенда: ``{}``\n``Пассивка: если ускорять время слишком часто, может создаться новая`` *``вселенная``*\n``~aceltime - ускорить время``".format(ctx.message.author.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/27/MadeinHeaven.png/revision/latest/scale-to-width-down/312?cb=20140924111429")
        await bot.send_message(ctx.message.channel, embed=embed)
        
       
       
    #7 ЧАСТЬ (СТЕНДЫ)
    elif "Tusk ACT1" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Клык``\nВладелец стенда: ``{}``\n``~spin - набрать энергию вращения``\n``~nail - запустить вращающимися ногтями (изначально мут будет {} секунд) (с каждым его сообщением, мут будет на 5 секунд больше) (этот эффект будет длится столько времени, сколько энергии)``".format(ctx.message.author.name, spinning), color = 0xE69138)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/58/TuskAct1color.png/revision/latest/scale-to-width-down/350?cb=20140813205839")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Tusk ACT2" in (role.name for role in ctx.message.author.roles):
        spinnings = spinning * 2
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Клык``\nВладелец стенда: ``{}``\n``~spin - набрать энергию вращения``\n``~nail - запустить вращающимися ногтями (мут на {} секунд) (этот эффект будет длится столько времени, сколько энергии)``".format(ctx.message.author.name, spinnings), color = 0xE69138)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/7a/TuskAct2color.png/revision/latest/scale-to-width-down/350?cb=20160325172005")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Tusk ACT3" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Клык``\nВладелец стенда: ``{}``\n``~spin - набрать энергию вращения``\n``~whole - теперь сообщения этого пользователя будут вращаться``\n``P.S. это значит, что его сообщение будет под особым эффектом, он не сможет использовать бота, ему будут спамить в ЛС столько сообщений, сколько энергии (этот эффект будет длится столько времени, сколько энергии)``".format(ctx.message.author.name, spinning), color = 0xE69138)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/aa/TuskAct3color.png/revision/latest/scale-to-width-down/350?cb=20140813205954")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Tusk ACT4" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Клык``\nВладелец стенда: ``{}``\n``~spin - набрать энергию вращения``\n``~ginfspin - золотое бесконечное вращение (эффект третьего акта, но его время = энергия*2)``\n``~ora - замутить на 3 секунды``".format(ctx.message.author.name, spinning), color = 0xE69138)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/11/TuskAct4color.png/revision/latest/scale-to-width-down/350?cb=20140813210059")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Ball Breaker" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Шаразрушитель``\nВладелец стенда: ``{}``\n``~spin - набрать энергию вращения``\n``~bspin - заставить крутиться (каждое сообщение мут на 8 секунд) (этот эффект будет длится столько времени, сколько энергии)``".format(ctx.message.author.name), color = 0xE69138)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/52/BallBreakercolor.png/revision/latest/scale-to-width-down/255?cb=20140813205719")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Dirty Deeds Done Dirt Cheap" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Dirty Deeds Done Dirt Cheap``\nВладелец стенда: ``{}``\n``Пассивка: пока у вас активен`` **``Ticket to Ride``** ``вас нельзя замутить``\n``~ticket - активировать и деактивировать `` **``Ticket to Ride``**\n``~hop - вы можете дублировать ЛЮБОЙ стенд ДО 7-ой части на некоторое время, не потеряв свой (`` **``Ticket to Ride``** ``должен быть неактивен)``\n``~punch - замутить на 5 секунд (`` **``Ticket to Ride``** ``должен быть неактивен)``".format(ctx.message.author.name), color = 0xE69138)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/4d/D4c_sbr69.png/revision/latest/scale-to-width-down/350?cb=20160323142852")
        await bot.send_message(ctx.message.channel, embed=embed)
        
    #8 ЧАСТЬ (СТЕНДЫ)
    elif "Soft and Wet" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Мягкий и Влажный``\nВладелец стенда: ``{}``\n``~steal - вы можете украть всю энергию у некоторых стендов себе``\n``~mute - замутить на {} секунд (кол-во секунд зависит от украденной энергии, сперва, это 5 секунд)``".format(ctx.message.author.name, stealed), color = 0x81E8D2)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/9/9a/S%26WManga.png/revision/latest/scale-to-width-down/350?cb=20160108110654")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Paisley Park" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Цветочный парк``\nВладелец стенда: ``{}``\n``~getinfo (юзер) - если в последних 50 сообщениях есть сообщения этого пользователя, они перешлются вам в ЛС``".format(ctx.message.author.name), color = 0x81E8D2)
        embed.set_image(url="https://cdn.discordapp.com/attachments/483124973880213505/483147786951327744/unknown.png")
        await bot.send_message(ctx.message.channel, embed=embed)
        
    else:
        await bot.send_message(ctx.message.channel, "Вы не обладатель стенда, <@{}>. *Получить его можно только попросив у админа.*".format(ctx.message.author.id))

    if "{}".format(stand_name) in (role.name for role in ctx.message.author.roles):
        if stand_name == "":
            return
            
        if standability == "mute":
            stand_ab = "~standmute - замутить на 5 секунд"
        elif standability == "spam":
            stand_ab = "~standspam - заспамить уведомлениями в ЛС"
        elif standability == "gay":
            stand_ab = "~standgay - гей-порно в ЛС при каждом сообщении"
        elif standability == "un":
            stand_ab = "~standun - размутить человека (нельзя использовать на себя)"
        elif standability == "erase":
            stand_ab = "~standerase - стереть 10 сообщений (кулдавн этой команды 10 секунд)"
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``{}``\nВладелец стенда: ``{}``\n``{}``".format(stand_name, ctx.message.author.name, stand_ab), color = 0x81E8D2)
        embed.set_image(url=standpic)
        await bot.send_message(ctx.message.channel, embed=embed)
        
        
        
        
        
        
        

        
@bot.command(pass_context=True) #Инфа о стендах чужих
async def divine(ctx, member : discord.Member):
    global mutesec
    global charges
    global voicecharge
    global matured
    global muting
    global dcharge
    global spinning
    global stealed
    global degradations
    global degradations2
    global stand_name
    global standability
    global standpic
    global rippleenergy
    global rippleenergy2
    global karss
    
    #ХАМОН
    if "Jonathan Joestar" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о персонаже **{}**:".format(member.name), description = "Имя: ``Джонатан Джостар``\n``~overdrive (тип) (юзер)``\n``~ovlist - список доступных вам овердрайвов хамона``\n``Энергии хамона: {}``".format(rippleenergy), color = 0xFFFF00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/3f/JonathanP2.png/revision/latest/scale-to-width-down/342?cb=20170223113043")
        await bot.send_message(ctx.message.channel, embed=embed)
        
    elif "Joseph Joestar" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о персонаже **{}**:".format(member.name), description = 'Имя: ``Джозеф Джостар``\n``~overdrive (тип) (юзер)``\n``~ovlist - список доступных вам овердрайвов хамона``\n``Энергии хамона: {}``\n``~s (текст) - "И следующее, что ты скажешь: "``'.format(rippleenergy2), color = 0xFFFF00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/43/JosephJoestar123.png/revision/latest/scale-to-width-down/270?cb=20170521193900")
        await bot.send_message(ctx.message.channel, embed=embed)
        
    elif "Kars" in (role.name for role in member.roles):
        if "Ultimate" in (role.name for role in member.roles):
            embed = discord.Embed(title = "Информация о персонаже **{}**:".format(member.name), description = "Имя: ``Карс, ставший совершенным существом``\n``Пассивка: вас нельзя замутить, использовать на вас любую абилку``\n``~attack - замутить на {} секунд и получить энергию``".format(karss), color = 0xFFFF00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/43/KarsExposed.png/revision/latest?cb=20131127012039")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о персонаже **{}**:".format(member.name), description = "Имя: ``Карс``\n``~aja - надеть красный камень эйша в маску``\n``~attack - замутить на {} секунд``\n``~posseser (юзер) - поглотить пользователя хамона (Джонатан или Джозеф)``".format(karss), color = 0xFFFF00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/18/KarsA.png/revision/latest/scale-to-width-down/270?cb=20161029000057")
        await bot.send_message(ctx.message.channel, embed=embed)
        
    #ОСОБЫЙ СТЕНД
    elif "Roflan Crusader" in (role.name for role in member.roles): #2РОФЛАНОСЕЦ
        if "Requiem" in (role.name for role in member.roles):
            embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Рофланосец Реквием``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~rofl - случайное рофланебало в чат``\n``~degr - заставить человека деградировать 45 секунд``\n``~ultradegr - заставить деградировать всех 7 секунд``".format(member.name), color = 0x000000)
            embed.set_image(url="https://cdn.discordapp.com/attachments/472313657661980672/474521075846348800/unknown.png")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        if "Over Heaven" in (role.name for role in member.roles):
            degradations2 = round(degradations / 2.5)
            if degradations2 < 0:
                degradations2 = 2
            embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Рофланосец: Над небом``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~rofl - случайное рофланебало в чат``\n``~degr - заставить человека деградировать {} секунд``\n``~ultradegr - заставить деградировать всех {} секунд``\n``~charge - зарядить деградацию``".format(member.name, degradations, degradations2), color = 0x000000)
            embed.set_image(url="https://cdn.discordapp.com/attachments/472313657661980672/474521075846348800/unknown.png")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Рофланосец``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~rofl - случайное рофланебало в чат``\n``~degr - заставить человека деградировать 35 секунд``".format(member.name), color = 0x000000)
        embed.set_image(url="https://cdn.discordapp.com/attachments/472313657661980672/474521075846348800/unknown.png")
        await bot.send_message(ctx.message.channel, embed=embed)
        
    #3 ЧАСТЬ
    elif "The World" in (role.name for role in member.roles): #2МИР
        if "Over Heaven" in (role.name for role in member.roles):
            embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Мир: Над небом``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~world - «остановить время» на 12 секунд в чате``\n``~muda - замутить человека на 9 секунд`` **``МУДА МУДА МУДА``**".format(member.name), color = 0x9494e5)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b2/Twoh.png/revision/latest/scale-to-width-down/350?cb=20151229005251")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Мир``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~world - «остановить время» на 6 секунд в чате``\n``~muda - замутить человека на 7 секунд`` **``МУДА МУДА МУДА``**".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/41/TheWorld_AnimeAV.png/revision/latest/scale-to-width-down/270?cb=20160414095701")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Star Platinum" in (role.name for role in member.roles): #2СП
        if "Over Heaven" in (role.name for role in member.roles):
            embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Платиновая звезда: Мир над небом``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~ora - замутить человека на 8 секунд`` **``ORA ORA ORA``**\n``~world - «остановить время» на 9 секунды в чате``".format(member.name), color = 0x9494e5)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/ae/SPTW_AV.png/revision/latest/scale-to-width-down/270?cb=20160715195842")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Платиновая звезда``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~ora - замутить человека на 5 секунд`` **``ORA ORA ORA``**\n``~world - «остановить время» на 4 секунды в чате``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/ae/SPTW_AV.png/revision/latest/scale-to-width-down/270?cb=20160715195842")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Hermit Purple" in (role.name for role in member.roles): #2ХП
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Лиловый проповедник``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~divine - получить информацию о стенде кого-нибудь``\n``~ripple - защитить себя или кого-то от атак``\n``~unripple - снять защиту``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/1f/PurpleHermit_AnimeAV.png/revision/latest?cb=20160414095805")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Magician's Red" in (role.name for role in member.roles): #2МР
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Алый Маг``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~ignite - зажечь кого-нибудь``\n``~crossfire - зажечь всех на 5 секунд (ураган)``\n``~unignite - потушить``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/9/97/Magician%27s_Red_AnimeAV.png/revision/latest/scale-to-width-down/327?cb=20160414185722")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Hierophant Green" in (role.name for role in member.roles): #2ХГ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Зелёный проповедник``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~splash - замутить на 4 секунды``\n``~marionette - сделать человека марионеткой``\n``~mar (слова) - писать от его имени``\n``~unpuppet - снять марионетку``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d0/HierophantGreen_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414185638")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Silver Chariot" in (role.name for role in member.roles): #2СЧ
        if "Requiem" in (role.name for role in member.roles): #2СЧР
            embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Колесница Реквием``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: пытаясь писать в муте, вы размутите себя``\n``~self (юзер) - заставить стенд кого-то атаковать владельца (работает не на всех)``\n``~swordr (юзер 1) (юзер 2) (юзер 3) - замутить на 4 секунды``".format(member.name), color = 0x9494e5)
            embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/482449676495355904/unknown.png")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Серебряная колесница``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~speed - даёт возможность увернуться от мута (5 секунд)``\n``~sword - замутить на 4 секунды``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/88/SilverChariot_AnimeAV.png/revision/latest/scale-to-width-down/270?cb=20160414095744")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "The Fool" in (role.name for role in member.roles): #2ШУТ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Шут``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~shift - взять имя у кого-нибудь``\n``~nshift - взять ник``\n``~unshift - вернуть свой ник``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/07/Fool_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101341")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Tower of Gray" in (role.name for role in member.roles): #2ТАВЕР ОФ ГРЕЙ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Башня Сумерек``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: шанс 1/2 увернуться от атаки``\n``~jaw - отравить человека``\n``~unjaw - снять отраву``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414185549")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Dark Blue Moon" in (role.name for role in member.roles): #2ДБМ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Тёмно-синяя Луна``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~barn - прицепить моллюска``\n``~unbarn - убрать моллюска``\n``~barninfo - проверить моллюска``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e9/DarkBlueMoon_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414192329")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Strength" in (role.name for role in member.roles): #2СИЛА
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Сила``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: те, кто на корабле имеют защиту от остальных атак, но их можно атаковать этим стендом.``\n``~join - зайти на корабль (ВСЕМ)``\n``~shiptack - убрать возможность писать всем, кто на корабле``\n``~unshiptack - вернуть возможность писать всем, кто на корабле``\n``~take - выбросить с корабля``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/ec/Strength_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414095727")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Ebony Devil" in (role.name for role in member.roles): #2ДЬЯВОЛ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Дьявол``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: чем больше вас атакуют, тем на большее время вы можете мутить``\n``~dev - замутить на`` **``{}``** ``секунд``".format(member.name, mutesec), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/57/Ebony_Devil-AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414185656")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Yellow Temperance" in (role.name for role in member.roles): #2ЕТ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Жёлтая Умеренность``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~skill - написав это, вы не сможете использовать этот стенд, но подождав 5 минут, вы станете сильнее и снова сможете его использовать``\n``~slime - атаковать слизью``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/fb/YellowTemperance_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414185535")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Hanged Man" in (role.name for role in member.roles): #2ПОВЕШЕННЫЙ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Повешенный``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~hang - отзеркалить сообщения``\n``~unhang - убрать зеркало``~mirror - напасть на зазеркаленного``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d3/HangedMan_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101324")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Emperor" in (role.name for role in member.roles): #2ЭМПЕРОР
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Император``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: если тот, кого вы атаковали напишет хоть одно сообщение - вы сможете атаковать снова``\n``~emp - выстрелить (шанс 1/2)``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/9/9d/Emperor_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101400")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Empress" in (role.name for role in member.roles): #2ИМПРЕСС
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Императрица``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: начав паразитировать на ком-то, через некоторое время у вас спадёт стенд и вы попадёте в мут на 30 минут.``\n``~empress (слово) - если человек напишет это`` **``СЛОВО``**, ``вы начнёте паразитировать на нём``\n``~harm - замутить на 5 секунд человека, на котором паразитируете``\n``~unempress - снять слово``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/10/Empress_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101349")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Wheel of Fortune" in (role.name for role in member.roles): #2ВОФ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Колесо Фортуны``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~atrandom - замутить себя или кого на 10 минут (шанс 1/2).``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/28/WOF_AnimeAV.png/revision/latest/scale-to-width-down/340?cb=20160414095637")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Justice" in (role.name for role in member.roles): #2ДЖАСТИС
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Справедливость``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~manipulate (юзер) (слова) - манипулировать кем-то (заставить написать слова)``\n``~unman - перестать манипулировать``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/4d/Justice_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101110")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Lovers" in (role.name for role in member.roles): #2ЛАВЕРС
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Влюблённые``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: если вы попадёте в мут, то в мут попадёт и человек, в которого вы переместили свой стенд``\n``~love - переместить свой стенд в кого-то``\n``~lovemute - замутить себя на 5 минут``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/06/Lovers_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414185608")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Sun" in (role.name for role in member.roles): #2СОЛНЦЕ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Солнце``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~charge - зарядить энергией``\n``~hot - прислать {} уведомлений в ЛС``\n``~sun - опалить лучом на {} секунд``".format(member.name, charges, charges), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/ff/Sun_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414095719")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Death 13" in (role.name for role in member.roles): #2СМЕРТЬ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Смерть тринадцать``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~scythe - замутить на минуту себя или кого-то (шанс 1/2)``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/34/Death13_AnimeAV.png/revision/latest/scale-to-width-down/322?cb=20160414101418")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Judgement" in (role.name for role in member.roles): #2КАМЕО
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Суд``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~hail (юзер) - исполнить`` ~~**``?!желание?!``**~~".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/8e/Judgment_AnimeAV.png/revision/latest/scale-to-width-down/340?cb=20160414192321")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "High Priestess" in (role.name for role in member.roles): #2ЖРИЦА
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Жрица``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~posses - ненадолго завладеть кем-то``\n``~unposses - перестать владеть``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/11/Priestess_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414095813")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Geb" in (role.name for role in member.roles): #2ГЕБ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Геб``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~unignite - потушить всё пламя``\n``~water - атаковать водой человека в войсе``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/c7/Geb_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101332")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Khnum" in (role.name for role in member.roles): #2ХНУМ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Хнум``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~transfigure - преобразоваться в кого-то``\n``~unfigure - войти в нормальную форму``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/84/Khnum_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101100")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Tohth" in (role.name for role in member.roles): #2ТОТ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Тот``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~comics (человек со стендом`` **``Хнума``**``) - получить в ЛС комикс, контроллирующий пользователей``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/82/Tohth_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414095654")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Anubis" in (role.name for role in ctx.message.author.roles): #2АНУБИС
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Анубис``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: вы не можете пользоваться своим стендом, пока его не возьмёт другой человек``\n``~anubis - написав эту команду, активируется ваш стенд и можно будет использовать меч (для остальных)``\n``~swordbis - можно атаковать мечом, если стенд активен (для остальных)``\n``~destroy - замутить человека, взявшего меч, и деактивировать стенд (обладатель стенда)``".format(ctx.message.author.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f0/Anubis_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101457")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Bastet" in (role.name for role in member.roles): #2БАСТ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Баст``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~shock - после каждого сообщения, этому человеку будут спамить в ЛС``\n``~unshock - убрать шок``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/5b/Bastet_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101441")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Sethan" in (role.name for role in member.roles): #2СЕТ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Сет``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~babys - убрать у кого-нибудь возможность использовать свой стенд на 10 минут, отключив свой на это время``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/29/Sethan_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414185518")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Osiris" in (role.name for role in member.roles): #2ОСИРИС
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Осирис``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~play - сыграть в угадайку с кем-нибудь``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/7b/Osiris_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101007")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Horus" in (role.name for role in member.roles): #2ПЕТ ШОП
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Хор``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~freeze - заморозить одну команду``\n``~ice - атаковать льдом``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/64/Horus_AnimeAV.png/revision/latest/scale-to-width-down/348?cb=20160414101249")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Atum" in (role.name for role in member.roles): #2ДАРБИ СТАРШИЙ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Атум``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~vplay - сыграть в гонку с кем-нибудь``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/bd/Atum_AnimeAV.png/revision/latest/scale-to-width-down/333?cb=20160414101449")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Cream" in (role.name for role in member.roles): #2КРЕМ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Крем``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~void - затягивать в пустоту сообщения``\n``~unvoid - выпустить из пустоты``".format(member.name), color = 0x9494e5)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/57/Cream_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414101433")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        
    #4 ЧАСТЬ
        
      
      
      
    elif "Crazy Diamond" in (role.name for role in member.roles): #2ББ
        if "Requiem" in (role.name for role in member.roles):
            embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Безумный Алмаз Реквием``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~dorara - замутить на 5 секунд и размутить``\n``~untime - отменить все остановки времени``".format(member.name), color = 0xff00ff)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/c5/Crazy_Diamond_Anime.png/revision/latest/scale-to-width-down/350?cb=20160414081459")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Безумный Алмаз``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~heal - размутить и вылечить яд крысы``\n``~dorara - замутить на 5 секунд``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/c5/Crazy_Diamond_Anime.png/revision/latest/scale-to-width-down/350?cb=20160414081459")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Killer Queen" in (role.name for role in member.roles): #2КК
        if "Alternate" in (role.name for role in member.roles):
            embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Смертельная королева (Альтернативная)``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~bubble - замутить на 10 секунд (задержка 60 секунд)``\n``~bombcheck - проверить бомбы``\n``~sha - если этот человек что-то напишет - попадёт в мут на 5 секунд``\n``~sha2 - если этот человек что-то напишет - попадёт в мут на 5 секунд``\n``~sha3 - если этот человек что-то напишет - попадёт в мут на 5 секунд``\n``~sha4 - если этот человек что-то напишет - попадёт в мут на 5 секунд``".format(member.name), color = 0xff00ff)
            embed.set_image(url="https://cdn.discordapp.com/attachments/473403386599964672/483485245086105630/unknown.png")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        if "Matured" not in (role.name for role in member.roles):
            embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Смертельная королева``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~shibo - замутить на 3 секунды``\n``~bomb - поставить бомбу на человека, и тот, кто его упомянёт попадёт в мут на 10 минут (первая бомба)``\n``~bombcheck - проверить первую бомбу``\n``~sha - если этот человек что-то напишет - попадёт в мут на 5 секунд (вторая бомба)``\n**``??? - (третья бомба?!)``**".format(member.name), color = 0xff00ff)
        else:
            embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Смертельная королева``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~shibo - замутить на 3 секунды``\n``~bomb - поставить бомбу на человека, и тот, кто его упомянёт попадёт в мут на 10 минут (первая бомба)``\n``~bombcheck - проверить первую бомбу``\n``~sha - если этот человек что-то напишет - попадёт в мут на 5 секунд (вторая бомба)``\n**``~bite - (третья бомба?!)``**".format(member.name), color = 0xff0000)
        embed.set_image(url="https://cdn.discordapp.com/attachments/472313657661980672/472316805763956756/unknown.png")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "The Hand" in (role.name for role in member.roles): #2РУКА
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Рука``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~erase - стереть пространство``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/46/The_Hand_Anime.png/revision/latest/scale-to-width-down/350?cb=20160429212824")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Echoes Egg" in (role.name for role in member.roles): #2ЭХО
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Эхо``\nВладелец стенда: ``{}``\nСпособности стенда:\n**``???``**".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/ce/Echoes_Egg_Form.png")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Echoes ACT1" in (role.name for role in member.roles): #2ЭХО АКТ1
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Эхо``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~sound (юзер) (слово) - генерация звука``\n``~mutesound - перестать создавать звук``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/62/ACT1_AV.png/revision/latest/scale-to-width-down/270?cb=20160520170003")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Echoes ACT2" in (role.name for role in member.roles): #2ЭХО АКТ2
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Эхо``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~soundtwo (юзер) (слово) - особенная генерация звука``\n``~mutesound - перестать создавать звук (от 1 и 2 акта)``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/19/EchoesACT2_AV.png/revision/latest/scale-to-width-down/270?cb=20160527173808")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Echoes ACT3" in (role.name for role in member.roles): #2ЭХО АКТ3
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Эхо``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~ffreeze - заморозить``\n``~mutesound - перестать создавать звук (от 1 и 2 акта)``\n``~unfreeze - разморозить``\n``~unevolve - вернуться к форме яйца``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/31/EchoesACT3_AV.png/revision/latest/scale-to-width-down/270?cb=20160909173528")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Heaven's Door" in (role.name for role in member.roles): #2ХЕВЕН ДОР
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Райские врата``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~book - превратить в книгу``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/de/Heaven%27s_Door_AV.png/revision/latest/scale-to-width-down/270?cb=20160923180054")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Aqua Necklace" in (role.name for role in member.roles): #2ВОДНОЕ ОЖЕРЕЛЬЕ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Водное ожерелье``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~aqua - заставить сообщения растикаться``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/4f/Aqua_Necklace_AV.png/revision/latest/scale-to-width-down/350?cb=20160414095501")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Bad Company" in (role.name for role in member.roles): #2ПК
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Плохая компания``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~soldier - атаковать солдатами (для остальных)``\n``~tank - атаковать танком (для остальных)``\n``~para - атаковать парашютистами (для остальных)``\n``~heli - атаковать вертолётами (для остальных)``\n``~targetbad - поставить цель``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/12/BadCo_AV.png/revision/latest/scale-to-width-down/350?cb=20160422191814")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Red Hot Chili Pepper" in (role.name for role in member.roles): #2РХЧП
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Острый красный Чили Перец``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: каждые несколько секунд в войсе вы будете заряжаться (максимум 30)``\n``~el - замутить на {} секунд``".format(member.name, voicecharge), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/0e/RHCP_Anime.png/revision/latest/scale-to-width-down/350?cb=20160617173431")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "The Lock" in (role.name for role in member.roles): #2ЗАМОК
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Замок``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~lock - закрепить на ком-то замок``\n``~mcheck - проверить кол-во монет``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Surface" in (role.name for role in member.roles): #2Поверхность
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Поверхность``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~manq - сделать человека куклой``\n``~mimicry - превратить куклу в кого-то``\n``~unmanq - убрать превращение и куклу``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a0/SurfaceAnime.png/revision/latest/scale-to-width-down/227?cb=20160513182613")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Love Deluxe" in (role.name for role in member.roles): #2ЛАВ ДЕЛЮКС
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Любовь Делюкс``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~lovedeluxe (буква или слова) - стирать данное слово (букву) каждый раз, когда хоть кто-то пишет сообщение``\n``~undel - убрать слово``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e9/Love_Deluxe_AV.png/revision/latest/scale-to-width-down/350?cb=20160527174230")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Pearl Jam" in (role.name for role in member.roles): #2ПЁРЛ ДЖЕМ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Жемчужный Джем``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~feed - замутить человека на 5 минут, а затем дать ему возможность увернуться от следующего мута``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/3f/Pearl_Jam_Anime_Closeup.png/revision/latest/scale-to-width-down/270?cb=20160603192620")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Achtung Baby" in (role.name for role in member.roles): #2МАЛЫШ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Опасный Малыш``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: пытаясь писать в муте, вы будете делать сообщения`` *``невидимыми``*".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/6f/Achtung_Baby_AV.png/revision/latest/scale-to-width-down/350?cb=20160924071026")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Ratt" in (role.name for role in member.roles): #2КРЫСА
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Крыса``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~poishot - выстрелить ядом``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/59/Ratt_summoned.png/revision/latest/scale-to-width-down/640?cb=20160715205844")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Harvest" in (role.name for role in member.roles): #2ЖАТВА
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Собиратель``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: каждый раз когда кто-то отправляет рофлан-ебало (не считая вас), вы получаете монетку``\n``~collects - проверить прайс-лист за рофлан-койны и кол-во монет``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b6/Harvestanime.png/revision/latest/scale-to-width-down/350?cb=20160729214906")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Cinderella" in (role.name for role in member.roles): #2ЗОЛУШКА
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Золушка``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~form (юзер) - дать возможность кому-то сменить ник``\n``~newname (ник) - поставить новый ник (для тех, на кого использовали стенд)``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/0c/Cinderella_AV.png/revision/latest/scale-to-width-down/350?cb=20160812174646")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Atom Heart Father" in (role.name for role in member.roles): #2ОТЕЦ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Отец с атомным сердцем``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~arrow - лук со стрелой``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/3c/AHF_AV.png/revision/latest/scale-to-width-down/350?cb=20160916171054")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Boy II Man" in (role.name for role in member.roles): #2КНБ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Мужественный парень``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~rps - сыграть в камень-ножницы-бумага``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/5f/Boy_II_Man_KeyArt.png/revision/latest/scale-to-width-down/329?cb=20161228082527")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Earth Wind and Fire" in (role.name for role in member.roles): #2EWF
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Земля, огонь и ветер``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: вас нельзя замутить``\n``~morph - сменить себе ник``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/9/9d/EW%26F_AV.png/revision/latest/scale-to-width-down/348?cb=20160930175920")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Highway Star" in (role.name for role in member.roles): #HS
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Звезда автострады``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~room (название) - создать новый приватный канал, который удалится через минуту``\n``~suck - высосать жизненную энергию (в следующий раз, когда вы будете в муте, вы будете размучены, а этот человек попадёт на 7 минут в мут)``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/ca/Highway_Star_AV.png/revision/latest/scale-to-width-down/350?cb=20161014210104")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Stray Cat" in (role.name for role in member.roles): #2СК
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Бродячий Кот``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~airshoot - замутить на 6 секунд``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/aa/Stray_Cat_first_appearance.png/revision/latest/scale-to-width-down/640?cb=20161021205006")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Super Fly" in (role.name for role in member.roles): #2СФ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Вздымающийся``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~reflect (юзер) - если вы будете пытаться писать в муте, замутят и данного человека``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/c1/Super_Fly_AV.png/revision/latest/scale-to-width-down/329?cb=20161028170755")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Enigma" in (role.name for role in member.roles): #2ЭНИГМА
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Загадка``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: превращённый в бумагу больше не сможет использовать команды. Однако, если вас замутят, все бумажки пропадут.``\n``~paper - превратить в бумагу человека, написавшего вут-фейс``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/c1/Enigma_AV.png/revision/latest/scale-to-width-down/350?cb=20161111210722")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Cheap Trick" in (role.name for role in member.roles): #2ЧИП ТРИК
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Дешёвый трюк``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~whisper (юзер) (слова) - шептать``".format(member.name), color = 0xff00ff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/55/Cheap_Trick_AV.png/revision/latest/scale-to-width-down/346?cb=20161118192225")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        
        
        
        
    #5 ЧАСТЬ
    elif "Gold Experience" in (role.name for role in member.roles): #ЗО
        if "Requiem" in (role.name for role in member.roles):
            embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Золотой ветер Реквием``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: если вы напишите сообщение в муте - мут пропадёт``\n``~muda - замутить на 4 секунды``\n``~glife - создать жизнь``\n``~zero - убрать возможность пользоваться командами этого бота``".format(member.name), color = 0xffff00)
            embed.set_image(url="https://cdn.discordapp.com/attachments/473403386599964672/476410589523083284/5cd2cbe5528d28cc.PNG")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Золотой ветер``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: если вы напишите сообщение в муте - мут пропадёт``\n``~muda - замутить на 4 секунды``\n``~glife - создать жизнь``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/482250418206801932/cb8e42b3d77f1dbd.PNG")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Sticky Fingers" in (role.name for role in member.roles): #2МОЛНИЯ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Липучие Пальцы``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: каждое сообщение от вас в застёжке - мут на 5 секунд``\n``~zip - сделать застёжку``\n``~zipper - ARIARIARI``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/dd/StickyFingers.png/revision/latest/scale-to-width-down/307?cb=20150428184345")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Moody Blues" in (role.name for role in member.roles): #2МАДИ БЛУС
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Угрюмый Джаз``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~record - начать записывать все сообщения человека в ЛС на 5 минут``\n``~stop - завершить запись``\n``~urya - замутить на 4 секунды``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/482253362620792852/aa17535292bee228.PNG")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Sex Pistols" in (role.name for role in member.roles): #2Шесть пуль
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Шесть пуль``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~bully (юзер 1) (юзер 2) (юзер 3) (юзер 4)  - замутить`` **``4``** ``человека на 5 минут``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/bb/SexPistols.png/revision/latest/scale-to-width-down/350?cb=20160425115528")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Aerosmith" in (role.name for role in member.roles): #2АЭРОКУЗНИЦА
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Аэрокузница``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~aero (юзер 1) (юзер 2) - замутить 2-ух юзеров на 20 минут, но в это время нельзя использовать свои команды``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a5/Aerosmith.png/revision/latest/scale-to-width-down/350?cb=20170610062644")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Purple Haze" in (role.name for role in member.roles): #2ФТ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Фиолетовый туман``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~virused - заразить вирусом, который через некоторое время исчезнет``\n``~ubasha - замутить на 3 секунды``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/1c/PurpleHaze.png/revision/latest/scale-to-width-down/335?cb=20150429070459")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Spice Girl" in (role.name for role in member.roles): #2SG
        embed = discord.Embed(title = "Информация о вашем стенде:", description = "Имя стенда: ``Спайс Гёрл``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~soft - замутить на 3 секунды и забрать возможность один раз воспользоваться стендом``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/df/Spice_Girl.png/revision/latest/scale-to-width-down/350?cb=20160413153303")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "King Crimson" in (role.name for role in member.roles): #2KING CRIMSON
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Кроваво-красный Король``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~timeerase - стереть время``\n``~punch - замутить на 6 секунд (в стёртом времени 10)``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f9/KingCrimson.png/revision/latest/scale-to-width-down/350?cb=20170204065902")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Black Sabbath" in (role.name for role in member.roles): #2BS
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Чёрная Суббота``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: если в вас выстрелят стрелой, вы заберёте её.``\n``~dshadow (юзер) - замутить на 10 секунд (до 16 часов)``\n``~vshadow (юзер 1) (юзер 2) - замутить на 5 секунд (после 16 часов)``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/3a/Black_Sabbath.png/revision/latest/scale-to-width-down/350?cb=20160320054224")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Soft Machine" in (role.name for role in member.roles): #2SM
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Мягкая Машина``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~deflate - сделать`` *``лёгким``*\n``Пассивка: лёгкие вещи могут увернуться от следующего мута, но не смогут пользоваться командами``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f9/SoftMachine.png/revision/latest?cb=20150429071004")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Kraft Work" in (role.name for role in member.roles): #2KW
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Крафт Ворк``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~llock - убрать пользователю писать возможность в канал, в котором вы использовали эту команду (на 5 минут)``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d0/KraftWork.png/revision/latest/scale-to-width-down/350?cb=20150429071412")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Little Feet" in (role.name for role in member.roles): #2LF
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Крохотные Лапки``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~shrink - уменьшить``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/56/ManInTheMirror_first.png/revision/latest/scale-to-width-down/339?cb=20161231090359")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Man in the Mirror" in (role.name for role in member.roles): #2MIM
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Человек в зеркале``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~createmirror (юзер) - создать канал, в который открыт доступ вам и этому юзеру. Он будет уничтожен через 1 минуту.``\n``Пассивка: в этом канале вы сможете использовать стенд, а тот юзер, которого вы затащите - нет.``\n``~mirattack - атаковать зазеркаленного``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/56/ManInTheMirror_first.png/revision/latest/scale-to-width-down/339?cb=20161231090359")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Mr.President" in (role.name for role in member.roles): #2ПРЕЗИДЕНТ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Президент``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~hide - спрятать на минуту от мута``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d9/Coco_Jumbo_Room_Color.png/revision/latest/scale-to-width-down/350?cb=20160517160222")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Beach Boy" in (role.name for role in member.roles): #2BB
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Рыбак``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: пока мут есть, вы не можете использовать свои команды``\n``~hook - замутить человека в войсе на 10 минут``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/32/Beach_Boy.png/revision/latest/scale-to-width-down/336?cb=20160426155655")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "The Grateful Dead" in (role.name for role in member.roles): #2BB
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Благодарный Мертвец``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~age - дать возможность написать сообщение в муте``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/70/The_Grateful_Dead.png/revision/latest/scale-to-width-down/339?cb=20150521171134")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Baby Face" in (role.name for role in member.roles): #2BF
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Детское Лицо``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: чем больше используют команд бота, тем на большее время мут``\n``~homu - замутить на`` **``{}``** ``секунд``".format(member.name, muting), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d2/BabyFacePro.png/revision/latest/scale-to-width-down/350?cb=20170629221729")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "White Album" in (role.name for role in member.roles): #2WA
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Белый Альбом``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка - ледяная броня: когда вас замутят, следующий, кто напишет сообщение не сможет использовать команды бота``\n``~temp - замутить на 4 секунды`` *``зафриженного юзера``*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/da/WhiteAlbum.png/revision/latest/scale-to-width-down/338?cb=20150523161426")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Clash" in (role.name for role in member.roles): #2КЛЭШ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Клэш``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~liq (юзер) - замутить на 3 секунды (если юзер в голосовом, на 5)``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/fb/Clash.png/revision/latest/scale-to-width-down/350?cb=20171024042957")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Talking Head" in (role.name for role in member.roles): #2TH
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Разговорчивая Голова``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~lie (юзер) - переместить свой стенд в кого-то``\n``~lying (слово) (слова или слово) - заменять слова``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e5/Talking_Head.png/revision/latest/scale-to-width-down/350?cb=20160320054512")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Notorious B.I.G" in (role.name for role in member.roles): #2NB
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Печально-известный B.I.G``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: командами этого стенда можно пользоваться в муте``\n``~enabsorb - атаковать (атаковав Солнце или РХЧП, вы заберёте у него всю энергию)``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/ef/NotoriousBIG.png/revision/latest?cb=20170620043550")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Metallica" in (role.name for role in member.roles): #2МЕТАЛЛ
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Металлика``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~invisible - сделать невидимым``\n``~vis - сделать видимым``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/18/Metallica_AV.png/revision/latest/scale-to-width-down/350?cb=20160423084036")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Green Day" in (role.name for role in member.roles): #2GD
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Зелёный Денёк``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка: заплесневевший пользователь не сможет вас атаковать``\n``~mold (юзер) - заплесневеть``\n``~unmold (юзер) - убрать плесень``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f8/Green_Day.png/revision/latest?cb=20161231083726")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Oasis" in (role.name for role in member.roles): #2ОАЗИС
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Оазис``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~ground (юзер 1) (юзер 2) - атаковать пользователей не в войсе``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/ae/Oasis_Stand.png/revision/latest/scale-to-width-down/350?cb=20170612181607")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Rolling Stones" in (role.name for role in member.roles): #2РС
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Роллинг Стоунс``\nВладелец стенда: ``{}``\nСпособности стенда:\n``~stone - дать вечный мут, муту на время (на одного человека, снимется сам, если вы переключите)``\n``~unstone - убрать вечный мут``".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/86/Rolling_Stones.png/revision/latest/scale-to-width-down/350?cb=20140822162552")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        
    #6 ЧАСТЬ (СТЕНДЫ)
    elif "Stone Free" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Каменная Свобода``\nВладелец стенда: ``{}``\nСпособности стенда:\n``Пассивка:``\n``1) нитка может быть всего 1``\n``2) нить не может пользоваться стендом``\n``3) на нить не действует мут``\n``~stringed - превратить объект в нить``\n``~unstring - превратить обратно``\n``~ora - замутить на 4 секунды``".format(member.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/75/StonefreeP.png/revision/latest/scale-to-width-down/317?cb=20160417073326")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Kiss" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Поцелуй``\nВладелец стенда: ``{}``\n``~dub - дублировать стенд``".format(member.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/0f/KissP.png/revision/latest?cb=20170109190909")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Burning Down the House" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Поджог Дома``\nВладелец стенда: ``{}``\n``Пассивка: призраком может стать лишь один, они могут писать в муте, но не использовать команды. Нельзя использовать на себя.``\n``~ghost - превратить в призрака``\n``~unghost - снять превращение``".format(member.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/61/BDtHP.png/revision/latest/scale-to-width-down/350?cb=20150607141943")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Foo Fighters" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Фу Файтерс``\nВладелец стенда: ``{}``\n``~invasion - пересылать удалённые сообщения юзера вам в ЛС``\n``~plankton - замутить на`` **``(3-7)``** ``секунд``".format(member.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/4d/FooP.png/revision/latest/scale-to-width-down/328?cb=20170109053755")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Weather Report" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Прогноз Погоды``\nВладелец стенда: ``{}``\n``~wset - поставить погоду``\n``~wlist - список погодных условий``".format(member.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/42/WeatherRP.png/revision/latest/scale-to-width-down/350?cb=20150607144211")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Diver Down" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Водолаз``\nВладелец стенда: ``{}``\n``Пассивка: каждый раз когда вы пишите в муте - получаете заряд``\n``~diver - замутить на {} секунд``".format(member.name, dcharge), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/ee/DiveP.png/revision/latest/scale-to-width-down/350?cb=20170629083510")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Whitesnake" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Белая Змея``\nВладелец стенда: ``{}``\n``~extract - извлечь диск из кого-нибудь``\n``~insert - загрузить диск в кого-нибудь``".format(member.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/dc/Howaitosuneiku.png/revision/latest/scale-to-width-down/295?cb=20170101020857")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "C-Moon" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Луна``\nВладелец стенда: ``{}``\n``~gravity - сообщения вверх ногами у всех``".format(member.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e6/C-Moon.png/revision/latest?cb=20170101001516")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Made in Heaven" in (role.name for role in member.roles):
        if "Requiem" in (role.name for role in member.roles):
            embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Прямиком из Рая Реквием``\nВладелец стенда: ``{}``\n``Пассивка: если ускорять время слишком часто, может создаться новая`` *``вселенная``*\n``~aceltime - ускорить время``\n``~newstand - создать стенд``".format(member.name), color = 0x12ffff)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/27/MadeinHeaven.png/revision/latest/scale-to-width-down/312?cb=20140924111429")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Прямиком из Рая``\nВладелец стенда: ``{}``\n``Пассивка: если ускорять время слишком часто, может создаться новая`` *``вселенная``*\n``~aceltime - ускорить время``".format(member.name), color = 0x12ffff)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/27/MadeinHeaven.png/revision/latest/scale-to-width-down/312?cb=20140924111429")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        
    #7 ЧАСТЬ (СТЕНДЫ)
    elif "Tusk ACT1" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Клык``\nВладелец стенда: ``{}``\n``~spin - набрать энергию вращения``\n``~nail - запустить вращающимися ногтями (изначально мут будет {} секунд) (с каждым его сообщением, мут будет на 5 секунд больше) (этот эффект будет длится столько времени, сколько энергии)``".format(member.name, spinning), color = 0xE69138)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/58/TuskAct1color.png/revision/latest/scale-to-width-down/350?cb=20140813205839")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Tusk ACT2" in (role.name for role in member.roles):
        spinnings = spinning * 2
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Клык``\nВладелец стенда: ``{}``\n``~spin - набрать энергию вращения``\n``~nail - запустить вращающимися ногтями (мут на {} секунд) (этот эффект будет длится столько времени, сколько энергии)``".format(member.name, spinnings), color = 0xE69138)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/7a/TuskAct2color.png/revision/latest/scale-to-width-down/350?cb=20160325172005")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Tusk ACT3" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Клык``\nВладелец стенда: ``{}``\n``~spin - набрать энергию вращения``\n``~whole - теперь сообщения этого пользователя будут вращаться``\n``P.S. это значит, что его сообщение будет под особым эффектом, он не сможет использовать бота, ему будут спамить в ЛС столько сообщений, сколько энергии (этот эффект будет длится столько времени, сколько энергии)``".format(member.name, spinning), color = 0xE69138)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/aa/TuskAct3color.png/revision/latest/scale-to-width-down/350?cb=20140813205954")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Tusk ACT4" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Клык``\nВладелец стенда: ``{}``\n``~spin - набрать энергию вращения``\n``~ginfspin - золотое бесконечное вращение (эффект третьего акта, но его время = энергия*2)``\n``~ora - замутить на 3 секунды``".format(member.name, spinning), color = 0xE69138)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/11/TuskAct4color.png/revision/latest/scale-to-width-down/350?cb=20140813210059")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Ball Breaker" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Шаразрушитель``\nВладелец стенда: ``{}``\n``~spin - набрать энергию вращения``\n``~bspin - заставить крутиться (каждое сообщение мут на 8 секунд) (этот эффект будет длится столько времени, сколько энергии)``".format(member.name, spinning), color = 0xE69138)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/52/BallBreakercolor.png/revision/latest/scale-to-width-down/255?cb=20140813205719")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Dirty Deeds Done Dirt Cheap" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Dirty Deeds Done Dirt Cheap``\nВладелец стенда: ``{}``\n``Пассивка: пока у вас активен`` **``Ticket to Ride``** ``вас нельзя замутить``\n``~ticket - активировать и деактивировать `` **``Ticket to Ride``**\n``~hop - вы можете дублировать ЛЮБОЙ стенд ДО 7-ой части на некоторое время, не потеряв свой (`` **``Ticket to Ride``** ``должен быть неактивен)``\n``~punch - замутить на 5 секунд (`` **``Ticket to Ride``** ``должен быть неактивен)``".format(member.name), color = 0xE69138)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/4d/D4c_sbr69.png/revision/latest/scale-to-width-down/350?cb=20160323142852")
        await bot.send_message(ctx.message.channel, embed=embed)
        
    #8 ЧАСТЬ (СТЕНДЫ)
    elif "Soft and Wet" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Мягкий и Влажный``\nВладелец стенда: ``{}``\n``~steal - вы можете украть всю энергию у некоторых стендов себе``\n``~mute - замутить на {} секунд (кол-во секунд зависит от украденной энергии, сперва, это 5 секунд)``".format(member.name, stealed), color = 0x81E8D2)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/9/9a/S%26WManga.png/revision/latest/scale-to-width-down/350?cb=20160108110654")
        await bot.send_message(ctx.message.channel, embed=embed)
    elif "Paisley Park" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``Цветочный парк``\nВладелец стенда: ``{}``\n``~getinfo (юзер) - если в последних 50 сообщениях есть сообщения этого пользователя, они перешлются вам в ЛС``".format(member.name), color = 0x81E8D2)
        embed.set_image(url="https://cdn.discordapp.com/attachments/483124973880213505/483147786951327744/unknown.png")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        
        
    else:
        await bot.send_message(ctx.message.channel, "<@{}> не обладает стендом.".format(member.id))  
        
        
    if "{}".format(stand_name) in (role.name for role in member.roles):
        if stand_name == "":
            return
            
        if standability == "mute":
            stand_ab = "~standmute - замутить на 5 секунд"
        elif standability == "spam":
            stand_ab = "~standspam - заспамить уведомлениями в ЛС"
        elif standability == "gay":
            stand_ab = "~standgay - гей-порно в ЛС при каждом сообщении"
        elif standability == "un":
            stand_ab = "~standun - размутить человека (нельзя использовать на себя)"
        elif standability == "erase":
            stand_ab = "~standerase - стереть 10 сообщений (кулдавн этой команды 10 секунд)"
        embed = discord.Embed(title = "Информация о стенде:", description = "Имя стенда: ``{}``\nВладелец стенда: ``{}``\n``{}``".format(stand_name, member.name, stand_ab), color = 0x81E8D2)
        embed.set_image(url=standpic)
        await bot.send_message(ctx.message.channel, embed=embed)
        
        
        

        
        
        
        
        
        
        
        
        
        
        
@bot.command(pass_context=True) #ЗА ВАРУДО
async def bomb(ctx, member : discord.Member):
    global user_bomb
    if "Killer Queen" in (role.name for role in ctx.message.author.roles):
        if "Alternate" in (role.name for role in ctx.message.author.roles):
            return
    
    if ctx.message.author.id == member.id:
        embed = discord.Embed(title = "Нельзя использовать превращение в бомбу на себе, {}.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d7/Killer_Queen_glares.png/revision/latest/scale-to-width-down/640?cb=20160826191328")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        return

    if "Killer Queen" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "{} превратил кого-то в бомбу, используя свой стенд.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d7/Killer_Queen_glares.png/revision/latest/scale-to-width-down/640?cb=20160826191328")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        user_bomb = member.id
        
@bot.command(pass_context=True) #ЗА ВАРУДО
async def sha(ctx, member : discord.Member):
    global sha_bomb
    global sha_bombe
    if "Killer Queen" in (role.name for role in ctx.message.author.roles):
        if "Alternate" in (role.name for role in ctx.message.author.roles):
            embed = discord.Embed(title = "**{}** использовал *первый* сердечный приступ на **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/35/SHA_Part8.jpg/revision/latest?cb=20180728030216")
            await bot.send_message(ctx.message.channel, embed=embed)
        
            sha_bombe = member.id
            return
            
    if "Killer Queen" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "{} использовал на {} вторую бомбу.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/53/SHA_initial_appearance.png/revision/latest/scale-to-width-down/640?cb=20160826191428")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        sha_bomb = member.id
        
@bot.command(pass_context=True) #ЗА ВАРУДО
async def sha2(ctx, member : discord.Member):
    global sha_bombe2
    if "Killer Queen" in (role.name for role in ctx.message.author.roles):
        if "Alternate" in (role.name for role in ctx.message.author.roles):
            embed = discord.Embed(title = "**{}** использовал *второй* сердечный приступ на **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/35/SHA_Part8.jpg/revision/latest?cb=20180728030216")
            await bot.send_message(ctx.message.channel, embed=embed)
        
            sha_bombe2 = member.id
            
@bot.command(pass_context=True) #ЗА ВАРУДО
async def sha3(ctx, member : discord.Member):
    global sha_bombe3
    if "Killer Queen" in (role.name for role in ctx.message.author.roles):
        if "Alternate" in (role.name for role in ctx.message.author.roles):
            embed = discord.Embed(title = "**{}** использовал *третий* сердечный приступ на **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/35/SHA_Part8.jpg/revision/latest?cb=20180728030216")
            await bot.send_message(ctx.message.channel, embed=embed)
        
            sha_bombe3 = member.id
            
@bot.command(pass_context=True) #ЗА ВАРУДО
async def sha4(ctx, member : discord.Member):
    global sha_bombe4
    if "Killer Queen" in (role.name for role in ctx.message.author.roles):
        if "Alternate" in (role.name for role in ctx.message.author.roles):
            embed = discord.Embed(title = "**{}** использовал *четвёртый* сердечный приступ на **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/35/SHA_Part8.jpg/revision/latest?cb=20180728030216")
            await bot.send_message(ctx.message.channel, embed=embed)
        
            sha_bombe4 = member.id
        
@bot.command(pass_context=True) #ЗА ВАРУДО
async def bombcheck(ctx):
    global user_bomb
    global sha_bombe
    global sha_bombe2
    global sha_bombe3
    global sha_bombe4
    if "Killer Queen" in (role.name for role in ctx.message.author.roles):
        if "Alternate" in (role.name for role in ctx.message.author.roles):
            await bot.send_message(ctx.message.author, "**Первый приступ на <@{}>**\n**Второй приступ на <@{}>**\n**Третий приступ на <@{}>**\n**Четвёртый приступ на <@{}>**".format(sha_bombe, sha_bombe2, sha_bombe3, sha_bombe4))
            return
    
    if "Killer Queen" in (role.name for role in ctx.message.author.roles):
        
        await bot.send_message(ctx.message.author, "**<@{}> сейчас превращён в бомбу.**".format(user_bomb))

        
@bot.command(pass_context=True) #ЗА ВАРУДО
@commands.cooldown(1, 60, commands.BucketType.user)
async def world(ctx):
    global star_stop
    global muted_all_users
    global stopped_mgs
    
    if muted_all_users == 1:
        return
    if "The World" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "ZA WARUDO! TOKI WO TOMARE.", description = "*«МИР! ВРЕМЯ ОСТАНОВИСЬ»*", color = 0xffff00)
        embed.set_image(url="https://thumbs.gfycat.com/SelfishIllinformedIceblueredtopzebra-size_restricted.gif")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        star_stop = 1
        muted_all_users = 1
        stopped_mgs = []
        
        if "Over Heaven" in (role.name for role in ctx.message.author.roles):
            await asyncio.sleep(12)
        else:
            await asyncio.sleep(6)

        embed = discord.Embed(title = "Soshite, toki wa ugoki dasu.", description = "*«Время снова возообновило свой ход»*", color = 0xffff00)
        await bot.send_message(ctx.message.channel, embed=embed)
        
        muted_all_users = 0
        for i in stopped_mgs:
            await bot.send_message(ctx.message.channel, "{} : {}".format(i.author.name, i.content))
        
    if "Star Platinum" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "STAR PLATINUM! ZA WARUDO!", description = "*«ПЛАТИНОВАЯ ЗВЕЗДА! МИР!»*", color = 0xffff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/472313657661980672/472332302932770826/1515086809_tumblr_ouvojg7ZQg1qlmo0vo1_500.gif")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        star_stop = 2
        muted_all_users = 1
        stopped_mgs = []

        if "Over Heaven" in (role.name for role in ctx.message.author.roles):
            await asyncio.sleep(9)
        else:
            await asyncio.sleep(4)
        
        embed = discord.Embed(title = "Toki wa ugoki dasu.", description = "*«Время возообновило свой ход»*", color = 0xffff00)
        await bot.send_message(ctx.message.channel, embed=embed)
        
        muted_all_users = 0
        for i in stopped_mgs:
            await bot.send_message(ctx.message.channel, "{} : {}".format(i.author.name, i.content))
        
@bot.command(pass_context=True) #МУДА МУДА МУДА
async def muda(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "The World" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "MUDA MUDA MUDA, {}!".format(member.name), description = "*«БЕСПОЛЕЗНО БЕСПОЛЕЗНО БЕСПОЛЕЗНО, {}!»*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://media1.tenor.com/images/f793f8e06058e79b2efe7e30ad239640/tenor.gif?itemid=5455737")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        if "Over Heaven" in (role.name for role in ctx.message.author.roles):
            await asyncio.sleep(9)
        else:
            await asyncio.sleep(7)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
    if "Gold Experience" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "MUDA MUDA MUDA, {}!".format(member.name), description = "*«БЕСПОЛЕЗНО БЕСПОЛЕЗНО БЕСПОЛЕЗНО, {}!»*".format(member.name), color = 0xffff00)
        
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/482428965621989406/unknown.png")
        else:
            embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/482420173182074892/unknown.png")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(4)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True) #МУДА МУДА МУДА
async def ora(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Star Platinum" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "ORA ORA ORA, {}!".format(member.name), description = "*«ОРА ОРА ОРА, {}!»*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://i.kym-cdn.com/photos/images/original/001/196/436/c92.gif")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        if "Over Heaven" in (role.name for role in ctx.message.author.roles):
            await asyncio.sleep(8)
        else:
            await asyncio.sleep(5)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
    if "Stone Free" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "ORA ORA ORA, {}!".format(member.name), description = "*«ОРА ОРА ОРА, {}!»*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://i.ytimg.com/vi/TSN1q3FBGgo/maxresdefault.jpg")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(4)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
        
        
    if "Tusk ACT4" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "ORA ORA ORA, {}!".format(member.name), description = "*«ОРА ОРА ОРА, {}!»*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/482422276994891776/unknown.png")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(3)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True) #ХАЙЕРОФАНТ ГРИН
@commands.cooldown(1, 8, commands.BucketType.user)
async def splash(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Hierophant Green" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "ИЗУМРУДНЫЙ ВСПЛЕСК!", description = "*{} атаковали.*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/powerlisting/images/8/81/Hierophant_Green%27s_Emerald_Splash%21%21%21%21_JoJo.gif/revision/latest?cb=20180412154853")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(4)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True) #ДЬЯВОЛ МУТ
@commands.cooldown(1, 8, commands.BucketType.user)
async def dev(ctx, member : discord.Member):
    global mutesec
    if "В муте" in (role.name for role in member.roles):
        return
    if "Ebony Devil" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "Дьявол **{}** атаковал **{}**.".format(ctx.message.author.name, member.name), description = "*{} атаковали.*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/76/EbonyDevilAttacking.jpg/revision/latest/scale-to-width-down/640?cb=20140523223228")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(mutesec)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True) #СЛИЗНЕВЫЙ МУТ
@commands.cooldown(1, 8, commands.BucketType.user)
async def slime(ctx, member : discord.Member):
    global mutesec
    global mutesec2
    global skilling
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if skilling == 1:
        return
    if "Yellow Temperance" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "{} атаковал слизью {}.".format(ctx.message.author.name, member.name), description = "*{} атаковали. Он попал в мут на {} секунд.*".format(member.name, mutesec2), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/77/Rubber_Soul_Anime.png/revision/latest?cb=20140530194339")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(mutesec2)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True) #РАНДОМ МУТ
@commands.cooldown(1, 8, commands.BucketType.user)
async def atrandom(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Wheel of Fortune" in (role.name for role in ctx.message.author.roles):
        if random.randint(0, 1) == 1:
            embed = discord.Embed(title = "{} атаковал {}.".format(ctx.message.author.name, member.name), description = "*Ему не повезло. Попал в мут на 10 минут.*", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/39/Wofgasoline.png/revision/latest/scale-to-width-down/640?cb=20140627172032")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, mute_role)
        
            await asyncio.sleep(600)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, mute_role)
            
        else:
            embed = discord.Embed(title = "{} атаковал {}.".format(ctx.message.author.name, member.name), description = "*Ему удалось замутить на 10 минут.*", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/39/Wofgasoline.png/revision/latest/scale-to-width-down/640?cb=20140627172032")
            await bot.send_message(ctx.message.channel, embed=embed)
            if "Tower of Gray" in (role.name for role in member.roles):
                if random.randint(0, 1) == 1:
                    embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                    await bot.send_message(ctx.message.channel, embed=embed)
                    return
                
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
        
            await asyncio.sleep(600)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
            
@bot.command(pass_context=True) #СОЛНЕЧНЫЙ ЛУЧ
@commands.cooldown(1, 8, commands.BucketType.user)
async def sun(ctx, member : discord.Member):
    global charges
    global mutesec
    charged = charges
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
        
    if "Sun" in (role.name for role in ctx.message.author.roles):
        if charges <= 0:
            embed = discord.Embed(title = "У вас нет зарядов, **{}**.".format(ctx.message.author.name), description = "*Зарядитесь энергией, написав* **``~charge``**".format(ctx.message.author.name), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/Sun_Desert.png/revision/latest/scale-to-width-down/640?cb=20140803075459")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "**{}** опалил лучом **{}**.".format(ctx.message.author.name, member.name), description = "``{}`` *атаковали. Он попал в мут на* ``{}`` *секунд.*".format(member.name, charged), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/20/Sun_laser.png/revision/latest/scale-to-width-down/640?cb=20140803080630")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        charges = 0
        
        await asyncio.sleep(charged)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True) #КОСА
@commands.cooldown(1, 8, commands.BucketType.user)
async def scythe(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Death 13" in (role.name for role in ctx.message.author.roles):
        if random.randint(0, 1) == 1:
            embed = discord.Embed(title = "**{}** атаковал косой **{}**.".format(ctx.message.author.name, member.name), description = "*Ему не повезло. Попал в мут на минуту.*", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/4e/Mannishboy.png/revision/latest?cb=20140809015258")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, mute_role)
        
            await asyncio.sleep(60)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, mute_role)
            
        else:
            embed = discord.Embed(title = "**{}** атаковал косой **{}**.".format(ctx.message.author.name, member.name), description = "*Ему удалось замутить на минуту.*", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/74/Death13.png/revision/latest/scale-to-width-down/640?cb=20140809020632")
            await bot.send_message(ctx.message.channel, embed=embed)
            if "Tower of Gray" in (role.name for role in member.roles):
                if random.randint(0, 1) == 1:
                    embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                    await bot.send_message(ctx.message.channel, embed=embed)
                    return
                
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
        
            await asyncio.sleep(60)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True) #АТАКА МЕЧОМ
async def speed(ctx):
    global top_speed
    if "Silver Chariot" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "{} попытался увернуться.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/3a/Afterimage_Creation_by_Jean_Pierre_Polnareff.gif/revision/latest?cb=20180227032250")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        top_speed = 1
        
        await asyncio.sleep(5)
        
        top_speed = 0
        
@bot.command(pass_context=True) #АТАКА МЕЧОМ
async def sword(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Silver Chariot" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "HORA HORA HORA, {}!".format(member.name), description = "*ХОРА ХОРА ХОРА, {}!*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/472313657661980672/472398319994535936/community_image_1430255865.gif")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(4)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True) #АТАКА ЗЕРКАЛА
async def mirror(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Hanged Man" in (role.name for role in ctx.message.author.roles):
        if member.id != hanged:
            embed = discord.Embed(title = "Атаковать можно только *отзеркаленных.*".format(member.name), description = "``Вне досягаемости стенда.``".format(member.name), color = 0xffff00)
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "**{}** атаковал **{}** в зеркале.".format(ctx.message.author.name, member.name), description = "*Отзеркаленный был атакован.*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/03/Hangedmanstabbing.png/revision/latest/scale-to-width-down/640?cb=20140606215232")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(4)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True) #ВЫСТРЕЛ ЭМП
async def emp(ctx, member : discord.Member):
    global mutesec
    global shooting
    global canshoot
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Emperor" in (role.name for role in ctx.message.author.roles):
        if canshoot == 1:
            embed = discord.Embed(title = "Вам *нечем* стрелять, **{}**.".format(message.author.name), description = "``У вас нет патрона. Чтобы его получить, ваша прошлая цель`` **``({})``** ``должна написать сообщение.``".format(shooting), color = 0xffff00)
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        if random.randint(0, 1) == 1:
            embed = discord.Embed(title = "**{}** не попал в **{}**.".format(ctx.message.author.name, member.name), description = "*Промахнулся и потерял пулю.*", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/6c/Jojos_bizarre_adventure_stardust_crusaders-11-hol_horse-emperor-stand-gun-cowboy-assassin.jpg/revision/latest/scale-to-width-down/640?cb=20140802183332")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            shooting = member.id
            canshoot = 1
            return
        embed = discord.Embed(title = "**{}** выстрелил в **{}**.".format(ctx.message.author.name, member.name), description = "*Теперь он в муте на 10 минут.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/6c/Jojos_bizarre_adventure_stardust_crusaders-11-hol_horse-emperor-stand-gun-cowboy-assassin.jpg/revision/latest/scale-to-width-down/640?cb=20140802183332")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        shooting = member.id
        canshoot = 1
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(600)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True) #ВОДА
@commands.cooldown(1, 8, commands.BucketType.user)
async def water(ctx, member : discord.Member):
    global mutesec
    
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Geb" in (role.name for role in ctx.message.author.roles):
        if member.voice_channel != None:
            embed = discord.Embed(title = "**{}** атаковал волной воды **{}**!".format(ctx.message.author.name, member.name), description = "*Теперь он в муте на 5 минут.*", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/2c/GebColliders_anime.png/revision/latest/scale-to-width-down/640?cb=20150119114500")
            await bot.send_message(ctx.message.channel, embed=embed)
        
            if "Tower of Gray" in (role.name for role in member.roles):
                if random.randint(0, 1) == 1:
                    embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                    await bot.send_message(ctx.message.channel, embed=embed)
                    return
                
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
        
            await asyncio.sleep(300)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
        else:
            embed = discord.Embed(title = "Можно атаковать пользователей только в войс-канале, **{}**.".format(ctx.message.author.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/2c/GebColliders_anime.png/revision/latest/scale-to-width-down/640?cb=20150119114500")
            await bot.send_message(ctx.message.channel, embed=embed)
            
@bot.command(pass_context=True) #АТАКА ЛЬДОМ
@commands.cooldown(1, 8, commands.BucketType.user)
async def ice(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Horus" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** атаковал **{}** глыбой льда.".format(ctx.message.author.name, member.name), description = "*{} атаковали. Он в муте на 3 секунды.*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/5a/Horus_kills_a_man.png/revision/latest/scale-to-width-down/640?cb=20150411065137")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(3)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True) #РИПЛ
async def ripple(ctx, member : discord.Member):
    global ripple_id
    if "Hermit Purple" in (role.name for role in ctx.message.author.roles):
        
        if member.id != ctx.message.author.id:
            embed = discord.Embed(title = "{} теперь защищён от атак.".format(member.name), description = "*{} защитил {} своим стендом.*".format(ctx.message.author.name, member.name), color = 0xffff00)
        else:
            embed = discord.Embed(title = "{} теперь защищён от атак.".format(member.name), description = "*{} защитился своим стендом.*".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/01/Hermit_Purple_Part_4.png/revision/latest/scale-to-width-down/640?cb=20160624190957")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        ripple_id = member.id
        
@bot.command(pass_context=True) #АНРИПЛ
async def unripple(ctx):
    global ripple_id
    if "Hermit Purple" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "{} снял защиту.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/01/Hermit_Purple_Part_4.png/revision/latest/scale-to-width-down/640?cb=20160624190957")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        ripple_id = ""
        
@bot.command(pass_context=True) #ИГНАЙТ
async def ignite(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    global ignite_id
    if "Magician's Red" in (role.name for role in ctx.message.author.roles):
        
        if ctx.message.author.id != ripple_id:
            if member.id != ctx.message.author.id:
                embed = discord.Embed(title = "{} зажёг {}.".format(ctx.message.author.name, member.name), description = "Теперь его сообщения *отжигают*.".format(ctx.message.author.name, member.name), color = 0xffff00)
            else:
                embed = discord.Embed(title = "{} поджёг себя.".format(ctx.message.author.name), description = "Теперь его сообщения *отжигают*.".format(ctx.message.author.name, member.name), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/4d/Magredanime.png/revision/latest/scale-to-width-down/640?cb=20140626022253")
            await bot.send_message(ctx.message.channel, embed=embed)
        
            ignite_id = member.id
        else:
            await bot.send_message(ctx.message.channel, "Неудалось зажечь <@{}>, так как он защищён.".format(member.id))
            
@bot.command(pass_context=True) #АНИГНАЙТ
async def unignite(ctx):
    global ignite_id
    global ignited_all_users
    if "Magician's Red" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "{} потушил пламя.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/4d/Magredanime.png/revision/latest/scale-to-width-down/640?cb=20140626022253")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        ignite_id = ""
        
    if "Geb" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** потушил пламя.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/ac/GebdefeatedAvdol.png/revision/latest/scale-to-width-down/640?cb=20150119114533")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        ignite_id = ""
        ignited_all_users = 0
            
@bot.command(pass_context=True) #КРОССФАЙР
@commands.cooldown(1, 8, commands.BucketType.user)
async def crossfire(ctx):
    global ignited_all_users
    
    if "Magician's Red" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "MAJISHANZU REDDO!", description = "*«АЛЫЙ МАГ!»*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/4d/Magredanime.png/revision/latest/scale-to-width-down/640?cb=20140626022253")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        ignited_all_users = 1
        await asyncio.sleep(5)
        ignited_all_users = 0
        
        embed = discord.Embed(title = "Все пользователи потухли.", description = "", color = 0xffff00)
        await bot.send_message(ctx.message.channel, embed=embed)
        
@bot.command(pass_context=True) #МАРИОНЕТКА
async def marionette(ctx, member : discord.Member):
    global puppet
    
    if "Hierophant Green" in (role.name for role in ctx.message.author.roles):
        if member.id != ctx.message.author.id:
            embed = discord.Embed(title = "{} стал марионеткой.".format(member.name), description = "*Теперь им может управлять {}.*".format(ctx.message.author.name), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/ff/Kakyoin%27s_puppet.png/revision/latest/scale-to-width-down/427?cb=20140413101435")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            puppet = member.id
        else:
            await bot.send_message(ctx.message.channel, "<@{}> **нельзя превратить в марионетку.**".format(ctx.message.author.id))
            
@bot.command(pass_context=True) #МАРИОНЕТКА
async def unpuppet(ctx):
    global puppet
    
    if "Hierophant Green" in (role.name for role in ctx.message.author.roles):
        await bot.send_message(ctx.message.channel, "*Марионетка уничтожена. Пользователь освобождён.*")
        
        puppet = ""
        
@bot.command(pass_context=True) #МАРИОНЕТКА
async def mar(ctx, *args):
    global puppet
    
    if "Hierophant Green" in (role.name for role in ctx.message.author.roles):
        marrionete_word = ' '.join(args)
        
        await bot.delete_message(ctx.message)
        await bot.send_message(ctx.message.channel, "<@{}> : {}".format(puppet, marrionete_word))
        
@bot.command(pass_context=True) #ПРЕВРАЩЕНИЕ
async def shift(ctx, member : discord.Member):
    
    if "The Fool" in (role.name for role in ctx.message.author.roles):
    
        embed = discord.Embed(title = "{} своровал ник у {}.".format(ctx.message.author.name, member.name), description = "*Песочное превращение.*".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/89/Thefoolnew.PNG/revision/latest/scale-to-width-down/640?cb=20150111042538")
        await bot.send_message(ctx.message.channel, embed=embed)

        await bot.change_nickname(ctx.message.author, member.name)
        
@bot.command(pass_context=True) #ПРЕВРАЩЕНИЕ2
async def nshift(ctx, member : discord.Member):
    
    if "The Fool" in (role.name for role in ctx.message.author.roles):
    
        embed = discord.Embed(title = "{} своровал ник у {}.".format(ctx.message.author.name, member.name), description = "*Песочное превращение.*".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/89/Thefoolnew.PNG/revision/latest/scale-to-width-down/640?cb=20150111042538")
        await bot.send_message(ctx.message.channel, embed=embed)

        await bot.change_nickname(ctx.message.author, member.nick)
        
@bot.command(pass_context=True) #РАЗЖАТИЕ
async def unshift(ctx):
    
    if "The Fool" in (role.name for role in ctx.message.author.roles):
    
        embed = discord.Embed(title = "{} вернул свой ник.".format(ctx.message.author.name), description = "*Песочное превращение.*".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/89/Thefoolnew.PNG/revision/latest/scale-to-width-down/640?cb=20150111042538")
        await bot.send_message(ctx.message.channel, embed=embed)

        await bot.change_nickname(ctx.message.author, ctx.message.author.name)
        
@bot.command(pass_context=True) #ОТРАВА
async def jaw(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    global jawed
    if "Tower of Gray" in (role.name for role in ctx.message.author.roles):
    
        embed = discord.Embed(title = "{} отравлен {}.".format(member.name, ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414185549")
        await bot.send_message(ctx.message.channel, embed=embed)
        jawed = member.id
        
@bot.command(pass_context=True) #АНОТРАВА
async def unjaw(ctx):
    global jawed
    if "Tower of Gray" in (role.name for role in ctx.message.author.roles):
    
        await bot.send_message(ctx.message.channel, "{} снял отраву.".format(ctx.message.author.name))
        jawed = ""
        
@bot.command(pass_context=True) #МОЛЛЮСК
async def barn(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    global barn
    global barned
    if "Dark Blue Moon" in (role.name for role in ctx.message.author.roles):
    
        embed = discord.Embed(title = "На {} теперь паразитируется моллюск.".format(member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e9/DarkBlueMoon_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414192329")
        await bot.send_message(ctx.message.channel, embed=embed)
        barn = member.id
        barned = 0
        
        await asyncio.sleep(300)
        if barn == member.id:
            barned = 1
        else:
            return
            
        await asyncio.sleep(300)
        if barn == member.id:
            barned = 2
        else:
            return
            
        await asyncio.sleep(300)
        if barn == member.id:
            barned = 3
        else:
            return
            
        await asyncio.sleep(300)
        if barn == member.id:
            embed = discord.Embed(title = "*Моллюск спал.*", description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e9/DarkBlueMoon_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414192329")
            await bot.send_message(ctx.message.channel, embed=embed)
            barned = 0
            barn = ""
        else:
            return
        
@bot.command(pass_context=True) #МОЛЛЮСК2
async def unbarn(ctx):
    global barn
    global barned
    if "Dark Blue Moon" in (role.name for role in ctx.message.author.roles):
    
        embed = discord.Embed(title = "*Моллюск снят.*", description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e9/DarkBlueMoon_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414192329")
        await bot.send_message(ctx.message.channel, embed=embed)
        barn = ""
        barned = 0
        
@bot.command(pass_context=True) #МОЛЛЮСК3
async def barninfo(ctx):
    global barned
    
    if barned == 0:
        embed = discord.Embed(title = "Информация о моллюске:", description = "Первая стадия: ``Активна``\n*Уведомление в ЛС.*\nВторая стадия: ``Неактивна``\n*Уведомление в ЛС и мут на 2 секунды после каждого сообщения.*\nТретья стадия: ``Неактивна``\n*Два уведомления в ЛС и мут на 4 секунды.*\nЧетвёртая стадия: ``Неактивна``\n*Мут на 10 секунд.*\nПятая стадия: ``Неактивна``\n*Спадение моллюска.*", color = 0xffff00)
    elif barned == 1:
        embed = discord.Embed(title = "Информация о моллюске:", description = "Первая стадия: ``Неактивна``\n*Уведомление в ЛС.*\nВторая стадия: ``Активна``\n*Уведомление в ЛС и мут на 2 секунды после каждого сообщения.*\nТретья стадия: ``Неактивна``\n*Два уведомления в ЛС и мут на 4 секунды.*\nЧетвёртая стадия: ``Неактивна``\n*Мут на 10 секунд.*\nПятая стадия: ``Неактивна``\n*Спадение моллюска.*", color = 0xffff00)
    elif barned == 2:
        embed = discord.Embed(title = "Информация о моллюске:", description = "Первая стадия: ``Неактивна``\n*Уведомление в ЛС.*\nВторая стадия: ``Неактивна``\n*Уведомление в ЛС и мут на 2 секунды после каждого сообщения.*\nТретья стадия: ``Активна``\n*Два уведомления в ЛС и мут на 4 секунды.*\nЧетвёртая стадия: ``Неактивна``\n*Мут на 10 секунд.*\nПятая стадия: ``Неактивна``\n*Спадение моллюска.*", color = 0xffff00)
    elif barned == 3:
        embed = discord.Embed(title = "Информация о моллюске:", description = "Первая стадия: ``Неактивна``\n*Уведомление в ЛС.*\nВторая стадия: ``Неактивна``\n*Уведомление в ЛС и мут на 2 секунды после каждого сообщения.*\nТретья стадия: ``Неактивна``\n*Два уведомления в ЛС и мут на 4 секунды.*\nЧетвёртая стадия: ``Активна``\n*Мут на 10 секунд.*\nПятая стадия: ``Неактивна``\n*Спадение моллюска.*", color = 0xffff00)
    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e9/DarkBlueMoon_AnimeAV.png/revision/latest/scale-to-width-down/350?cb=20160414192329")
    await bot.send_message(ctx.message.channel, embed=embed)
    
@bot.command(pass_context=True)
async def shiptack(ctx):
    global attackship
    if "Strength" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "{} убрал возможность писать на корабле.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b5/StrengthAv.png/revision/latest/scale-to-width-down/480?cb=20160501181810")
        await bot.send_message(ctx.message.channel, embed=embed)
        attackship = 1
        
@bot.command(pass_context=True)
async def unshiptack(ctx):
    global attackship
    if "Strength" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "{} вернул возможность писать на корабле.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b5/StrengthAv.png/revision/latest/scale-to-width-down/480?cb=20160501181810")
        await bot.send_message(ctx.message.channel, embed=embed)
        attackship = 0

@bot.command(pass_context=True) #ЗАЙТИ НА КОРАБЛЬ
async def join(ctx):
    if "Strength" not in (role.name for role in ctx.message.author.roles):
        if "На корабле" in (role.name for role in ctx.message.author.roles):
            embed = discord.Embed(title = "{} уже *на корабле*.".format(ctx.message.author.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b5/StrengthAv.png/revision/latest/scale-to-width-down/480?cb=20160501181810")
            await bot.send_message(ctx.message.channel, embed=embed)
        else:
            embed = discord.Embed(title = "{} зашёл *на корабль*.".format(ctx.message.author.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b5/StrengthAv.png/revision/latest/scale-to-width-down/480?cb=20160501181810")
            await bot.send_message(ctx.message.channel, embed=embed)
        
            korabl_role = discord.utils.find(lambda r: r.name == 'На корабле', ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, korabl_role)
    else:
        embed = discord.Embed(title = "Нельзя зайти на корабль.", description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b5/StrengthAv.png/revision/latest/scale-to-width-down/480?cb=20160501181810")
        await bot.send_message(ctx.message.channel, embed=embed)
        
@bot.command(pass_context=True) #ВЫБРОСИТЬ С КОРАБЛЯ
async def take(ctx, member : discord.Member):
    if "Strength" in (role.name for role in ctx.message.author.roles):
        if "На корабле" in (role.name for role in member.roles):
            embed = discord.Embed(title = "{} выбросил {} *с корабля*.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b5/StrengthAv.png/revision/latest/scale-to-width-down/480?cb=20160501181810")
            await bot.send_message(ctx.message.channel, embed=embed)
        
            korabl_role = discord.utils.find(lambda r: r.name == 'На корабле', ctx.message.server.roles)
            await bot.remove_roles(member, korabl_role)
        else:
            embed = discord.Embed(title = "{} не было *на корабле*.".format(member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b5/StrengthAv.png/revision/latest/scale-to-width-down/480?cb=20160501181810")
            await bot.send_message(ctx.message.channel, embed=embed)
            
@bot.command(pass_context=True) #АТАКА СЛИЗНЯ
async def skill(ctx):
    global mutesec2
    global skilling
    
    if skilling == 1:
        return
    if mutesec2 >= 30:
        return
    if "Yellow Temperance" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** эволюционирует.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/7e/YellowTemparance_defence.jpg/revision/latest/scale-to-width-down/640?cb=20140817055059")
        await bot.send_message(ctx.message.channel, embed=embed)
        skilling = 1
        
        await asyncio.sleep(300)
        
        mutesec2 += 3
        skilling = 0
        
        embed = discord.Embed(title = "**{}** эволюционировал.".format(ctx.message.author.name), description = "Теперь он мутит на **``{}``** секунды.".format(mutesec2), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/7e/YellowTemparance_defence.jpg/revision/latest/scale-to-width-down/640?cb=20140817055059")
        await bot.send_message(ctx.message.channel, embed=embed)
        
@bot.command(pass_context=True) #ЗЕРКАЛО
@commands.cooldown(1, 8, commands.BucketType.user)
async def hang(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    global hanged
    if "Hanged Man" in (role.name for role in ctx.message.author.roles):
    
        embed = discord.Embed(title = "{} отзеркалил {}.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/22/Hangedmanmirror.png/revision/latest/scale-to-width-down/640?cb=20140606215038")
        await bot.send_message(ctx.message.channel, embed=embed)
        hanged = member.id
        
@bot.command(pass_context=True) #ЗЕРКАЛО2
async def unhang(ctx):
    global hanged
    if "Hanged Man" in (role.name for role in ctx.message.author.roles):
    
        embed = discord.Embed(title = "**{}** убрал зеркало.".format(ctx.message.author.name), description = "*Теперь ничто не отзеркалено.*", color = 0xffff00)
        await bot.send_message(ctx.message.channel, embed=embed)
        hanged = ""
        
@bot.command(pass_context=True) #СЛОВО
@commands.cooldown(1, 8, commands.BucketType.user)
async def empress(ctx, word_new : str):
    global emp_w
    global paraziting
    if "Empress" in (role.name for role in ctx.message.author.roles):
        if parazit == "":
            embed = discord.Embed(title = "**{}** поставил новое слово.".format(ctx.message.author.name), description = "*{} стало новым словом.*".format(word_new), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/03/Empress_Anime01.png/revision/latest/scale-to-width-down/563?cb=20140807091208")
            await bot.send_message(ctx.message.channel, embed=embed)
            emp_w = word_new
            paraziting = ctx.message.author.id
        else:
            await bot.send_message(ctx.message.channel, "*<@{}>* ``уже паразитирует на`` *<@{}>*.".format(ctx.message.author.id, parazit))
            
@bot.command(pass_context=True) #СЛОВО
@commands.cooldown(1, 8, commands.BucketType.user)
async def unempress(ctx, word_new : str):
    global emp_w
    global paraziting
    if "Empress" in (role.name for role in ctx.message.author.roles):
        if parazit == "":
            embed = discord.Embed(title = "**{}** снял слово.".format(ctx.message.author.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/03/Empress_Anime01.png/revision/latest/scale-to-width-down/563?cb=20140807091208")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            emp_w = ""
            paraziting = ""
        else:
            await bot.send_message(ctx.message.channel, "*<@{}>* ``уже паразитирует на`` *<@{}>*.".format(ctx.message.author.id, parazit))
            
@bot.command(pass_context=True) #СЛОВО
@commands.cooldown(1, 8, commands.BucketType.user)
async def harm(ctx):
    global parazit
    global mutesec
    
    user = discord.Server.get_member(ctx.message.server, user_id=parazit)
    
    if "В муте" in (role.name for role in user.roles):
        return
        
    if "Ebony Devil" in (role.name for role in user.roles):
        mutesec += 1
                
    if "Empress" in (role.name for role in ctx.message.author.roles):
        if parazit != "":
            embed = discord.Embed(title = "Паразит **{}** ранил **{}**.".format(ctx.message.author.name, user.name), description = "*Теперь он в муте на 5 секунд.*", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/83/Empresspunch.png/revision/latest/scale-to-width-down/640?cb=20140620174650")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(user, mute_role)
        
            await asyncio.sleep(5)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(user, mute_role)
            
@bot.command(pass_context=True) #МАНИПУЛЯЦИЯ
@commands.cooldown(1, 8, commands.BucketType.user)
async def manipulate(ctx, member : discord.Member, *args):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    global word_need
    global justly
    
    if "Justice" in (role.name for role in ctx.message.author.roles):
    
    
        word_need = ' '.join(args)
        embed = discord.Embed(title = "**{}** поставил новое слово: **{}**.".format(ctx.message.author.name, word_need), description = "*Теперь {} нужно написать его, иначе он попадёт в мут на 3 минуты.*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/86/Justice_polnareff.png/revision/latest?cb=20140716123141")
        await bot.send_message(ctx.message.channel, embed=embed)

        
@bot.command(pass_context=True) #МАНИПУЛЯЦИЯ
@commands.cooldown(1, 8, commands.BucketType.user)
async def unman(ctx):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    global word_need
    global justly
    
    if "Justice" in (role.name for role in ctx.message.author.roles):
    
        embed = discord.Embed(title = "**{}** убрал слово.".format(ctx.message.author.name), description = "*Теперь не манипулирует пользователей.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/37/Justice_with_Enya.png/revision/latest/scale-to-width-down/640?cb=20140716122650")
        await bot.send_message(ctx.message.channel, embed=embed)

        justly = ""
        word_need = ""
        
@bot.command(pass_context=True) #ЛАВЕРС
@commands.cooldown(1, 8, commands.BucketType.user)
async def love(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    global loved
    global loving
    
    if "Lovers" in (role.name for role in ctx.message.author.roles):
    
        embed = discord.Embed(title = "**{}** переместил свой стенд в **{}**.".format(ctx.message.author.name, member.name), description = "*Если {} попадёт в мут, то в него попадёт и {}.*".format(ctx.message.author.name, member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/6e/Loversnerves.png/revision/latest/scale-to-width-down/590?cb=20140718230920")
        await bot.send_message(ctx.message.channel, embed=embed)

        loved = member.id
        loving = ctx.message.author.id
        
@bot.command(pass_context=True) #ЛАВЕРС
@commands.cooldown(1, 8, commands.BucketType.user)
async def lovemute(ctx):
    global mutesec
    global loved
    global loving
    
    lovermem = discord.Server.get_member(ctx.message.server, user_id=loved)
    if "Ebony Devil" in (role.name for role in lovermem.roles):
        mutesec += 1
    
    if "Lovers" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** ранил себя.".format(ctx.message.author.name), description = "*{} попал в мут на 5 минут.*".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/6e/Loversnerves.png/revision/latest/scale-to-width-down/590?cb=20140718230920")
        await bot.send_message(ctx.message.channel, embed=embed)

        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(ctx.message.author, mute_role)
        
        if loved != "":
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(lovermem, mute_role)
        
        await asyncio.sleep(300)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(ctx.message.author, mute_role)
        
        if loved != "":
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(lovermem, mute_role)
            
@bot.command(pass_context=True) #ЗАРЯДЫ
async def charge(ctx):
    global charges
    global voicecharge
    global degradations
    global muting
    
    muting -= 1
    
    if muting < 0:
        muting = 0
    if "Sun" in (role.name for role in ctx.message.author.roles):
        charges += 1
        
        await bot.send_message(ctx.message.channel, "Солнце *заряжается.* ``{}`` **зарядов**.".format(charges))
        
    if "Red Hot Chili Pepper" in (role.name for role in ctx.message.author.roles):
        if ctx.message.author.voice_channel == None:
            await bot.send_message(ctx.message.channel, "Для начала надо зайти в войс-канал.")
            return
        voicecharge += 1
        
        await bot.send_message(ctx.message.channel, "Перец *заряжается.* ``{}`` **зарядов**.".format(voicecharge))
        
    if "Roflan Crusader" in (role.name for role in ctx.message.author.roles):
        degradations += 1
        
        await bot.send_message(ctx.message.channel, "Деградация *заряжается.* ``{}`` **зарядов**.".format(degradations))
            
@bot.command(pass_context=True) #ЗАРЯДЫ
@commands.cooldown(1, 8, commands.BucketType.user)
async def hot(ctx, member : discord.Member):
    global charges
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
        
    if "Sun" in (role.name for role in ctx.message.author.roles):
        if charges == 0:
            embed = discord.Embed(title = "У вас нет зарядов, **{}**.".format(ctx.message.author.name), description = "*Зарядитесь энергией, написав* **``~charge``**".format(ctx.message.author.name), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/Sun_Desert.png/revision/latest/scale-to-width-down/640?cb=20140803075459")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        for i in range(charges):
            if charges > 0:
                embed = discord.Embed(title = "**{}**".format(member.name), description = "*Вас сжигает лучами солнца* **{}**.".format(ctx.message.author.name), color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/Sun_Desert.png/revision/latest/scale-to-width-down/640?cb=20140803075459")
                await bot.send_message(member, embed=embed)
                await bot.send_message(member, "<@{}>".format(member.id))
                charges -= 1
                
@bot.command(pass_context=True) #HAIL 2 U
async def hail(ctx, member : discord.Member):
  
    if "Judgement" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**``H A I L   2 U``**.", description = "***``С Ч А С Т Ь Я  Т 3 Б 3``***", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f2/Judgment_hail2u.gif")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        await asyncio.sleep(5)
        
        hail2u = random.randint(0, 4)
        if hail2u == 0:
            embed = discord.Embed(title = "Ваше ***?!желание?!*** исполнено, {}.".format(ctx.message.author.name), description = "***``ВЫ ПОПАЛИ В МУТ НА 30 МИНУТ.``***", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/57/JudgmentandPolnareff.png/revision/latest/scale-to-width-down/443?cb=20140825083230")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, mute_role)
        
            await asyncio.sleep(1800)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, mute_role)
        
        if hail2u == 1:
            hail2nick = ["Пидор", "Питуч галимый", "сосу бесплатно", "ОПА, ТВОЯ МАТЬ ОПА", "Раб Фуфа", "Радужный поник", "Единорог", "Артём Киселёв", "Весёлая Члениха", "Трапский чечник", "хочу умереть", "долбаёб", "Эйс пидор", "убейте меня", "пососный отсос", "ПУТЕН ЛОХ", "http://natribu.org", "ПИЗДАБОЛЛ"]
            randomnick = random.choice(hail2nick)
            embed = discord.Embed(title = "Ваше ***?!желание?!*** исполнено, {}.".format(ctx.message.author.name), description = "***``ВАШ НИК БЫЛ ИЗМЕНЁН НА {}.``***".format(randomnick), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/57/JudgmentandPolnareff.png/revision/latest/scale-to-width-down/443?cb=20140825083230")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            await bot.change_nickname(ctx.message.author, randomnick)
            
        if hail2u == 2:
            embed = discord.Embed(title = "Ваше ***?!желание?!*** исполнено, {}.".format(ctx.message.author.name), description = "***``ВЫ ЗАМУТИЛИ {} НА ЧАС.``***".format(member.name), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/57/JudgmentandPolnareff.png/revision/latest/scale-to-width-down/443?cb=20140825083230")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
        
            await asyncio.sleep(3600)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
            
        if hail2u == 3:
            hail2nick = ["Пидор", "Питуч галимый", "сосу бесплатно", "ОПА, ТВОЯ МАТЬ ОПА", "Раб Фуфа", "Радужный поник", "Единорог", "Артём Киселёв", "Весёлая Члениха", "Трапский чечник", "хочу умереть", "долбаёб", "Эйс пидор", "убейте меня", "пососный отсос", "ПУТЕН ЛОХ", "http://natribu.org", "ПИЗДАБОЛЛ"]
            randomnick = random.choice(hail2nick)
            embed = discord.Embed(title = "Ваше ***?!желание?!*** исполнено, {}.".format(ctx.message.author.name), description = "***``ВЫ ИЗМЕНИЛИ НИК {} НА {}.``***".format(member.name, randomnick), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/57/JudgmentandPolnareff.png/revision/latest/scale-to-width-down/443?cb=20140825083230")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            await bot.change_nickname(member, randomnick)
            
        if hail2u == 4:
            embed = discord.Embed(title = "Ваше ***?!желание?!*** исполнено, {}.".format(ctx.message.author.name), description = "***``ВЫ РАЗМУТИЛИ {} И ПОПАЛИ В МУТ НА ЧАС.``***".format(member.name), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/57/JudgmentandPolnareff.png/revision/latest/scale-to-width-down/443?cb=20140825083230")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            mutes_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mutes_role)
            
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, mute_role)
        
            await asyncio.sleep(3600)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, mute_role)
            
@bot.command(pass_context=True) #ПРИСТЛЕСС
async def posses(ctx, member : discord.Member):
    global posses
    if "В муте" in (role.name for role in member.roles):
        return
        
    if "High Priestess" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** ненадолго завладел **{}**.".format(ctx.message.author.name, member.name), description = "***``Вы завладели {} и теперь у него нет возможности писать сообщения.``***".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/ee/HighPriestess_AvdulDisguise.png/revision/latest/scale-to-width-down/575?cb=20140906091710")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        await bot.change_nickname(ctx.message.author, member.name)
        
        muted_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, muted_role)
        
        await bot.change_nickname(member, "_")
        
        posses = member.id
        
        await asyncio.sleep(600)
        
        await bot.change_nickname(ctx.message.author, ctx.message.author.name)
        await bot.change_nickname(member, member.name)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True) #ПРИСТЛЕСС
async def unposses(ctx):
    global posses
    if "High Priestess" in (role.name for role in ctx.message.author.roles):
        if posses == "":
            return
            
        userPosses = discord.Server.get_member(ctx.message.server, user_id=posses)
        embed = discord.Embed(title = "**{}** перестал владеть **{}**.".format(ctx.message.author.name, userPosses.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/fc/HP_giant_Angry.png/revision/latest/scale-to-width-down/640?cb=20150420145827")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        await bot.change_nickname(ctx.message.author, ctx.message.author.name)
        await bot.change_nickname(userPosses, userPosses.name)
        
@bot.command(pass_context=True) #ХНУМ ПРЕВРАЩЕНИЕ
async def transfigure(ctx, member : discord.Member):
    global oblik
    if "Khnum" in (role.name for role in ctx.message.author.roles):

        embed = discord.Embed(title = "Вы превратились в **{}**.".format(member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/74/Khnum_changeface.gif")
        await bot.send_message(ctx.message.author, embed=embed)
        
        oblik = member.id
        await bot.change_nickname(ctx.message.author, member.name)
        
@bot.command(pass_context=True) #ХНУМ ПРЕВРАЩЕНИЕ2
async def unfigure(ctx):
    global oblik
    if "Khnum" in (role.name for role in ctx.message.author.roles):

        embed = discord.Embed(title = "Вы вернули **свой облик**.", description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/74/Khnum_changeface.gif")
        await bot.send_message(ctx.message.author, embed=embed)
        
        oblik = ""
        await bot.change_nickname(ctx.message.author, ctx.message.author.name)
        
@bot.command(pass_context=True) #ХНУМ ПРЕВРАЩЕНИЕ
async def comics(ctx, member : discord.Member):
    global brat
    if "Tohth" in (role.name for role in ctx.message.author.roles):
        brat = member.id
        embed = discord.Embed(title = "**ПРИКЛЮЧЕНИЯ БРАТЦЕВ {} И {}**".format(ctx.message.author.name, member.name), description = "*``Licensed by``* ***``Чара``*** *``in 2018``*", color = 0xffff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/464724695506223105/473078999648829450/boin.png")
        await bot.send_message(ctx.message.author, embed=embed)
        await bot.send_message(member, embed=embed)
        
        await bot.send_message(ctx.message.author, "*Действия над книгой:*\n``~target (юзер) - выбрать цель приключений``\n``~read - читать дальше...``")
        
@bot.command(pass_context=True) #ХНУМ ПРЕВРАЩЕНИЕ
async def target(ctx, member : discord.Member):
    global target
    global brat
    
    if brat == "":
        return
    bratMem = discord.Server.get_member(ctx.message.server, user_id=brat)
    if "Tohth" in (role.name for role in ctx.message.author.roles):
        await bot.send_message(ctx.message.author, "``Вы выбрали в качестве цели:`` <@{}>".format(member.id))
        await bot.send_message(bratMem, "``Вы выбрали в качестве цели:`` <@{}>".format(member.id))
        
        target = member.id
        
@bot.command(pass_context=True) #ХНУМ ПРЕВРАЩЕНИЕ
async def read(ctx):
    global brat
    global oblik
    
    if brat == "":
        return
    bratMem = discord.Server.get_member(ctx.message.server, user_id=brat)
    if "Tohth" in (role.name for role in ctx.message.author.roles):
        if oblik == target:
            await bot.send_message(ctx.message.author, "``Дальше ему потребовалось написать: `` *``Я ПИДОРАС ГАЛИМЫЙ.``* и ваша цель попадёт в мут на 10 минут.".format(target, brat))
            await bot.send_message(ctx.message.author, "https://vignette.wikia.nocookie.net/jjba/images/3/31/Tohth_jotarodeath01.png/revision/latest/scale-to-width-down/640?cb=20150207174400")
            await bot.send_message(bratMem, "``Дальше ему потребовалось написать: `` *``Я ПИДОРАС ГАЛИМЫЙ.``* и ваша цель попадёт в мут на 10 минут.".format(target, brat))
            await bot.send_message(bratMem, "https://vignette.wikia.nocookie.net/jjba/images/3/31/Tohth_jotarodeath01.png/revision/latest/scale-to-width-down/640?cb=20150207174400")
            return
        await bot.send_message(ctx.message.author, "``Чтобы замутить свою цель`` (<@{}>) ``братцу`` <@{}> ``пришлось превратиться в него, используя свой стенд.``".format(target, brat))
        await bot.send_message(ctx.message.author, "https://cdn.discordapp.com/attachments/464724695506223105/473081672099692544/unknown.png")
        await bot.send_message(bratMem, "``Чтобы замутить свою цель`` (<@{}>) ``братцу`` <@{}> ``пришлось превратиться в него, используя свой стенд. Читать дальше: ~read``".format(target, brat))
        await bot.send_message(bratMem, "https://cdn.discordapp.com/attachments/464724695506223105/473081672099692544/unknown.png")
        
@bot.command(pass_context=True) #АКТИВ АНУБИСА
async def anubis(ctx):
    global tooksword
    
    if "Anubis" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Вы не можете взять себя, **{}**.".format(ctx.message.author.name), description = "*Активировать меч могут только другие люди.*", color = 0xffff00)
        if tooksword == "":
            embed.set_image(url="https://cdn.discordapp.com/attachments/472313657661980672/473103864954880000/unknown.png")
        else:
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/27/Anubisvision_Anime.png/revision/latest/scale-to-width-down/640?cb=20150207075806")
        await bot.send_message(ctx.message.channel, embed=embed)
        return

    if tooksword != "":
        embed = discord.Embed(title = "Меч уже активирован **{}**, {}.".format(tooksword, ctx.message.author.name), description = "*Вам следует подождать, когда меч станет деактивированым.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/27/Anubisvision_Anime.png/revision/latest/scale-to-width-down/640?cb=20150207075806")
        await bot.send_message(ctx.message.channel, embed=embed)
        return
        
    embed = discord.Embed(title = "{} взял меч и активировал его.".format(ctx.message.author.name), description = "*Теперь вами может управлять* ***``Анубис.``***", color = 0xffff00)
    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/bc/Anubis_Pol.PNG/revision/latest/scale-to-width-down/640?cb=20150202091335")
    await bot.send_message(ctx.message.channel, embed=embed)
    
    tooksword = ctx.message.author.id
    
@bot.command(pass_context=True) #АКТИВ АНУБИСА
async def swordbis(ctx, member : discord.Member):
    global tooksword

    if "Anubis" in (role.name for role in member.roles):
        embed = discord.Embed(title = "Нельзя атаковать своё же орудие, **{}**.".format(ctx.message.author.name), description = "*Попробуйте в качестве цели другого человека.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d5/Anubis_Silver_Charriot.PNG/revision/latest/scale-to-width-down/640?cb=20150209084825")
        await bot.send_message(ctx.message.channel, embed=embed)
        return

    if member.id == tooksword:
        embed = discord.Embed(title = "Вы пытаетесь атаковать себя, **{}**.".format(ctx.message.author.name), description = "*Но это безуспешно.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d5/Anubis_Silver_Charriot.PNG/revision/latest/scale-to-width-down/640?cb=20150209084825")
        await bot.send_message(ctx.message.channel, embed=embed)
        return
        
    if ctx.message.author.id == tooksword:
        embed = discord.Embed(title = "**{}** атаковал мечом **{}**.".format(ctx.message.author.name, member.name), description = "*{} попал в мут на 5 минут*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d5/Anubis_Silver_Charriot.PNG/revision/latest/scale-to-width-down/640?cb=20150209084825")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(300)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
    if random.randint(0, 5) == 5:
        embed = discord.Embed(title = "Вы случайно выронили меч, **{}**".format(ctx.message.author.name), description = "*Теперь он неактивен.*", color = 0xffff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/472313657661980672/473103864954880000/unknown.png")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        tooksword = ""
        
@bot.command(pass_context=True) #САМОУНИЧТОЖЕНИЕ С ЮЗЕРОМ
async def destroy(ctx):
    global tooksword

    tookmember = discord.Server.get_member(ctx.message.server, user_id=tooksword)
    if "Anubis" in (role.name for role in ctx.message.author.roles):
        if tooksword == "":
            embed = discord.Embed(title = "Меч никем не используется, **{}**.".format(ctx.message.author.name), description = "*Меч уже неактивен и нельзя использовать эту абилку.*", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/27/Anubisvision_Anime.png/revision/latest/scale-to-width-down/640?cb=20150207075806")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
            
        embed = discord.Embed(title = "Меч снова деактивирован, а его пользователь **({})** ранен, **{}**.".format(tookmember.name, ctx.message.author.name), description = "*Теперь его снова нужно подобрать. Пользователь попал в мут на 25 минут.*", color = 0xffff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/472313657661980672/473103864954880000/unknown.png")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        tooksword = ""

        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(tookmember, mute_role)
        
        await asyncio.sleep(1500)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(tookmember, mute_role)
        
        return
        
@bot.command(pass_context=True) #ШОКИРОВАТЬ
async def shock(ctx, member : discord.Member):
    global shocked

    if "Bastet" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** получил удар током.".format(member.name), description = "*Теперь его ЛС* **под напряжением** *и к нему* **липнут сообщения.**", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/c8/Bastet_stronger.png/revision/latest/scale-to-width-down/400?cb=20150223053044")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        shocked = member.id
        
@bot.command(pass_context=True) #РАЗШОКИРОВАТЬ
async def unshock(ctx):
    global shocked

    if "Bastet" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Напряжение снято.", description = "*Теперь разрядов больше нет.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/6f/Bast2.jpg/revision/latest/scale-to-width-down/640?cb=20150216072338")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        shocked = ""
        
@bot.command(pass_context=True) #ПРЕВРАТИТЬ В ПИЗДЮКА
async def babys(ctx, member : discord.Member):
    global baby
    
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1

    if "Sethan" in (role.name for role in ctx.message.author.roles):
        if baby != "":
            return
            
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        if top_speed == 1:
            embed = discord.Embed(title = "{} удалось увернуться от атаки.".format(message.author.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f3/Silver_Chariot_no_armor.png/revision/latest/scale-to-width-down/640?cb=20160410022457")
            await bot.send_message(message.channel, embed=embed)
            
            return
        embed = discord.Embed(title = "**{}** превратил **{}** в малыша на 10 минут.".format(ctx.message.author.name, member.name), description = "*Теперь ему нельзя использовать свой стенд.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/72/Screenshot_%28294%29.png/revision/latest/scale-to-width-down/640?cb=20150301231723")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        baby = member.id
        
        await bot.change_nickname(member, "Малыш {}".format(member.name))
        
        await asyncio.sleep(600)
        
        baby = ""
        
        await bot.change_nickname(member, member.name)
        
        embed = discord.Embed(title = "Превращение **{}** снято, {}.".format(member.name, ctx.message.author.name), description = "*Теперь он снова может использовать свой стенд.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/81/Sethansummon.png/revision/latest/scale-to-width-down/527?cb=20150302033313")
        await bot.send_message(ctx.message.channel, embed=embed)
        
@bot.command(pass_context=True) #ДАРБИ
async def play(ctx, member : discord.Member):
    global playing_with
    global randomnum
    global randomnum2
    global ready
    global ready2
    global darbi

    if playing_with != "":
        return
    if "Osiris" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** начал игру с **{}**.".format(ctx.message.author, member.name), description = "*Инструкция прислана в ЛС.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/5c/Osiris_shuffling_chips.png/revision/latest/scale-to-width-down/640?cb=20150320234957")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        playing_with = member.id
        darbi = ctx.message.author.id
        randomnum = random.randint(1, 9)
        randomnum2 = random.randint(1, 9)
        ready = 0
        ready2 = 0
            
        await bot.send_message(ctx.message.author, "Число вашего противника: **``{}``**. Если у вас выпало число **больше** чем у противника - **вы** выиграли, а он попадает в ``мут на 5 минут``. Вы можете **перебросить своё число**, если хотите, а **противник может у вас**. Если **вы** проиграли - попадаете в ``мут на 5 минут``.\nСписок команд во время игры:\n``~roll - перебросить своё число``\n``~readroll - готов (если вы оба готовы начнётся проверка - и выберется победитель)``".format(randomnum2))
        await bot.send_message(member, "Число вашего противника: **``{}``**. Если у вас выпало число **больше** чем у противника - **вы** выиграли, а он попадает в ``мут на 5 минут``. Вы можете **перебросить своё число**, если хотите, а **противник может у вас**. Если **вы** проиграли - попадаете в ``мут на 5 минут``.\nСписок команд во время игры:\n``~roll - перебросить своё число``\n``~readroll - готов (если вы оба готовы начнётся проверка - и выберется победитель)``".format(randomnum))
        
@bot.command(pass_context=True) #ДАРБИ
async def roll(ctx):
    global playing_with
    global randomnum
    global randomnum2
    global ready
    global ready2
    global darbi
    
    if playing_with == "":
        return
    if "Osiris" in (role.name for role in ctx.message.author.roles):
        if ready == 1:
            return
        randomnum = random.randint(1, 9)
        await bot.send_message(ctx.message.channel, "**{}** перебросил своё число. Теперь у вашего противника (<@{}>) показно ваше новое число.".format(ctx.message.author.name, playing_with))
        
        protivnik = discord.Server.get_member(ctx.message.server, user_id=playing_with)
        await bot.send_message(protivnik, "Новое число вашего противника: **``{}``**.".format(randomnum))
    elif ctx.message.author.id == playing_with:
        if ready2 == 1:
            return
        randomnum2 = random.randint(1, 9)
        await bot.send_message(ctx.message.channel, "**{}** перебросил своё число. Теперь у вашего противника (<@{}>) показно ваше новое число.".format(ctx.message.author.name, darbi))
        
        protivnik = discord.Server.get_member(ctx.message.server, user_id=darbi)
        await bot.send_message(protivnik, "Новое число вашего противника: **``{}``**.".format(randomnum2))
        
@bot.command(pass_context=True) #ДАРБИ
async def readroll(ctx):
    global playing_with
    global randomnum
    global randomnum2
    global ready
    global ready2
    global darbi
    
    if playing_with == "":
        return
    if "Osiris" in (role.name for role in ctx.message.author.roles):
        if ready == 1:
            return
        await bot.send_message(ctx.message.channel, "**{}** готов. Он больше **не сможет** перебросить своё число, <@{}>.".format(ctx.message.author.name, playing_with))
        ready = 1
        
        if ready2 == 1:
            await bot.send_message(ctx.message.channel, "Все готовы. **Вскрываемся**...")
            await asyncio.sleep(5)
            
            if randomnum > randomnum2:
                await bot.send_message(ctx.message.channel, "Вы победили, <@{}>. Ваше число - **{}**, число противника - **{}**...".format(ctx.message.author.id, randomnum, randomnum2))
                playing_with = ""
                ready = 0
                ready2 = 0
                
                protivnik = discord.Server.get_member(ctx.message.server, user_id=playing_with)
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(protivnik, mute_role)
        
                await asyncio.sleep(300)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(protivnik, mute_role)
            elif randomnum < randomnum2:
                await bot.send_message(ctx.message.channel, "Вы проиграли, <@{}>. Ваше число - **{}**, число противника - **{}**...".format(ctx.message.author.id, randomnum, randomnum2))
                playing_with = ""
                ready = 0
                ready2 = 0
                
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, mute_role)
        
                await asyncio.sleep(300)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, mute_role)
            else:
                await bot.send_message(ctx.message.channel, "Ничья. Ваши числа - {}, {}.".format(randomnum, randomnum2))
                playing_with = ""
                ready = 0
                ready2 = 0
                
    if ctx.message.author.id == playing_with:
        if ready2 == 1:
            return
        await bot.send_message(ctx.message.channel, "**{}** готов. Он больше **не сможет** перебросить своё число.".format(ctx.message.author.name))
        ready = 1
        
        if ready == 1:
            await bot.send_message(ctx.message.channel, "Все готовы. **Вскрываемся**...")
            await asyncio.sleep(5)
            
            if randomnum2 > randomnum:
                await bot.send_message(ctx.message.channel, "Вы победили, <@{}>. Ваше число - **{}**, число противника - **{}**...".format(ctx.message.author.id, randomnum2, randomnum))
                playing_with = ""
                ready = 0
                ready2 = 0
                
                protivnik = discord.Server.get_member(ctx.message.server, user_id=darbi)
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(protivnik, mute_role)
        
                await asyncio.sleep(300)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(protivnik, mute_role)
            elif randomnum2 < randomnum:
                await bot.send_message(ctx.message.channel, "Вы проиграли, <@{}>. Ваше число - **{}**, число противника - **{}**...".format(ctx.message.author.id, randomnum2, randomnum))
                playing_with = ""
                ready = 0
                ready2 = 0
                
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, mute_role)
        
                await asyncio.sleep(300)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, mute_role)
            else:
                await bot.send_message(ctx.message.channel, "Ничья. Ваши числа - {}, {}.".format(randomnum, randomnum2))
                playing_with = ""
                ready = 0
                ready2 = 0
                
@bot.command(pass_context=True) #ЗАМОРОЗКА
@commands.cooldown(1, 8, commands.BucketType.user)
async def freeze(ctx, member : discord.Member):
    global froze

    if "Horus" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** заморозил **{}**.".format(ctx.message.author.name, member.name), description = "*Его следующая команда бота заморожена.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d5/Horus_revealed.png/revision/latest/scale-to-width-down/640?cb=20150411065105")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        froze = member.id
        
@bot.command(pass_context=True) #ДАРБИ СТАРШИЙ
async def vplay(ctx, member : discord.Member):
    global playcar
    global car1pos
    global car2pos
    global darbis
    global carready
    global carready2
    global game_started

    if playcar != "":
        return
    if "Atum" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** начал гонку с **{}**.".format(ctx.message.author, member.name), description = "*Инструкция прислана в ЛС.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/29/Telence_with_Kakyoin.png/revision/latest/scale-to-width-down/640?cb=20150425011348")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        playcar = member.id
        darbis = ctx.message.author.id
        car1pos = 0
        car2pos = 0
        carready = 0
        carready2 = 0
        game_started = 0
            
        await bot.send_message(ctx.message.author, "Если оба игрока будут готовы - начнётся гонка. Во время неё нужно как можно быстрее писать ``~carmove``. Чья машина приедет первой, тот и выиграл.\nСпиоск команд этой игры:\n``~readyrace - готовность``\n``~carmove - подвинуть машину``")
        await bot.send_message(member, "Если оба игрока будут готовы - начнётся гонка. Во время неё нужно как можно быстрее писать ``~carmove``. Чья машина приедет первой, тот и выиграл.\nСпиоск команд этой игры:\n``~readyrace - готовность``\n``~carmove - подвинуть машину``")
        
@bot.command(pass_context=True) #ДАРБИ СТАРШИЙ
async def readyrace(ctx):
    global playcar
    global car1pos
    global car2pos
    global darbis
    global carready
    global carready2
    global game_started
    global race
    global race2

    if playcar == "":
        return
    if "Atum" in (role.name for role in ctx.message.author.roles):
        if carready == 1:
            return
        await bot.send_message(ctx.message.channel, "<@{}> *готов играть. Ожидаем противника...*".format(ctx.message.author.id))
        carready = 1
        
        if carready2 == 1:
            await bot.send_message(ctx.message.channel, "Оба игрока готовы, заезд начнётся через ``5 секунд``.")
            
            car1pos = 0
            car2pos = 0
            game_started = 0
            
            await asyncio.sleep(5)
            
            race = await bot.send_message(ctx.message.channel, "1----------------------------F")
            race2 = await bot.send_message(ctx.message.channel, "2----------------------------F")
            game_started = 1

    elif ctx.message.author.id == playcar:
        if carready2 == 1:
            return
        await bot.send_message(ctx.message.channel, "<@{}> *готов играть. Ожидаем противника...*".format(ctx.message.author.id))
        carready2 = 1
        
        if carready == 1:
            await bot.send_message(ctx.message.channel, "Оба игрока готовы, заезд начнётся через ``5 секунд``.")
            
            car1pos = 0
            car2pos = 0
            game_started = 0
            
            await asyncio.sleep(5)
            
            race = await bot.send_message(ctx.message.channel, "1----------------------------F")
            race2 = await bot.send_message(ctx.message.channel, "2----------------------------F")
            game_started = 1
            
@bot.command(pass_context=True) #ДАРБИ СТАРШИЙ
async def carmove(ctx):
    global playcar
    global car1pos
    global car2pos
    global darbis
    global carready
    global carready2
    global game_started
    global race
    global race2

    if game_started == 0:
        return
    if "Atum" in (role.name for role in ctx.message.author.roles):
        car1pos += 1
        
        await bot.delete_message(ctx.message)
        if car1pos == 1:
            await bot.edit_message(race, "-1---------------------------F")
        if car1pos == 2:
            await bot.edit_message(race, "--1--------------------------F")
        if car1pos == 3:
            await bot.edit_message(race, "---1-------------------------F")
        if car1pos == 4:
            await bot.edit_message(race, "----1------------------------F")
        if car1pos == 5:
            await bot.edit_message(race, "-----1-----------------------F")
        if car1pos == 6:
            await bot.edit_message(race, "------1----------------------F")
        if car1pos == 7:
            await bot.edit_message(race, "-------1---------------------F")
        if car1pos == 8:
            await bot.edit_message(race, "--------1--------------------F")
        if car1pos == 9:
            await bot.edit_message(race, "---------1-------------------F")
        if car1pos == 10:
            await bot.edit_message(race, "----------1------------------F")
        if car1pos == 11:
            await bot.edit_message(race, "-----------1-----------------F")
        if car1pos == 12:
            await bot.edit_message(race, "------------1----------------F")
        if car1pos == 13:
            await bot.edit_message(race, "-------------1---------------F")
        if car1pos == 14:
            await bot.edit_message(race, "--------------1--------------F")
        if car1pos == 15:
            await bot.edit_message(race, "---------------1-------------F")
        if car1pos == 16:
            await bot.edit_message(race, "----------------1------------F")
        if car1pos == 17:
            await bot.edit_message(race, "-----------------1-----------F")
        if car1pos == 18:
            await bot.edit_message(race, "------------------1----------F")
        if car1pos == 19:
            await bot.edit_message(race, "-------------------1---------F")
        if car1pos == 20:
            await bot.edit_message(race, "--------------------1--------F")
        if car1pos == 21:
            await bot.edit_message(race, "---------------------1-------F")
        if car1pos == 22:
            await bot.edit_message(race, "----------------------1------F")
        if car1pos == 23:
            await bot.edit_message(race, "-----------------------1-----F")
        if car1pos == 24:
            await bot.edit_message(race, "------------------------1----F")
        if car1pos == 25:
            await bot.edit_message(race, "-------------------------1---F")
        if car1pos == 26:
            await bot.edit_message(race, "--------------------------1--F")
        if car1pos == 27:
            await bot.edit_message(race, "---------------------------1-F")
        if car1pos == 28:
            await bot.edit_message(race, "----------------------------1F")
        if car1pos >= 29:
            if car2pos < 29:
                await bot.send_message(ctx.message.channel, "Заезд окончен. Выиграла первая машинка **(<@{}>)**.".format(ctx.message.author.id))
                car1pos = 0
                car2pos = 0
                carready = 0
                carready2 = 0
                game_started = 0
                
                protivnik = discord.Server.get_member(ctx.message.server, user_id=playcar)
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(protivnik, mute_role)
                
                playcar = ""
                darbis = ""
        
                await asyncio.sleep(300)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(protivnik, mute_role)
            elif car2pos == 29:
                await bot.send_message(ctx.message.channel, "Заезд окончен. Ничья.".format(ctx.message.author.id))
                playcar = ""
                darbis = ""
                car1pos = 0
                car2pos = 0
                carready = 0
                carready2 = 0
                game_started = 0
            

    elif ctx.message.author.id == playcar:
        car2pos += 1
        
        await bot.delete_message(ctx.message)
        if car2pos == 2:
            await bot.edit_message(race2, "-2---------------------------F")
        if car2pos == 2:
            await bot.edit_message(race2, "--2--------------------------F")
        if car2pos == 3:
            await bot.edit_message(race2, "---2-------------------------F")
        if car2pos == 4:
            await bot.edit_message(race2, "----2------------------------F")
        if car2pos == 5:
            await bot.edit_message(race2, "-----2-----------------------F")
        if car2pos == 6:
            await bot.edit_message(race2, "------2----------------------F")
        if car2pos == 7:
            await bot.edit_message(race2, "-------2---------------------F")
        if car2pos == 8:
            await bot.edit_message(race2, "--------2--------------------F")
        if car2pos == 9:
            await bot.edit_message(race2, "---------2-------------------F")
        if car2pos == 20:
            await bot.edit_message(race2, "----------2------------------F")
        if car2pos == 22:
            await bot.edit_message(race2, "-----------2-----------------F")
        if car2pos == 22:
            await bot.edit_message(race2, "------------2----------------F")
        if car2pos == 23:
            await bot.edit_message(race2, "-------------2---------------F")
        if car2pos == 24:
            await bot.edit_message(race2, "--------------2--------------F")
        if car2pos == 25:
            await bot.edit_message(race2, "---------------2-------------F")
        if car2pos == 26:
            await bot.edit_message(race2, "----------------2------------F")
        if car2pos == 27:
            await bot.edit_message(race2, "-----------------2-----------F")
        if car2pos == 28:
            await bot.edit_message(race2, "------------------2----------F")
        if car2pos == 29:
            await bot.edit_message(race2, "-------------------2---------F")
        if car2pos == 20:
            await bot.edit_message(race2, "--------------------2--------F")
        if car2pos == 22:
            await bot.edit_message(race2, "---------------------2-------F")
        if car2pos == 22:
            await bot.edit_message(race2, "----------------------2------F")
        if car2pos == 23:
            await bot.edit_message(race2, "-----------------------2-----F")
        if car2pos == 24:
            await bot.edit_message(race2, "------------------------2----F")
        if car2pos == 25:
            await bot.edit_message(race2, "-------------------------2---F")
        if car2pos == 26:
            await bot.edit_message(race2, "--------------------------2--F")
        if car2pos == 27:
            await bot.edit_message(race2, "---------------------------2-F")
        if car2pos == 28:
            await bot.edit_message(race2, "----------------------------2F")
        if car2pos >= 29:
            if car1pos < 29:
                await bot.send_message(ctx.message.channel, "Заезд окончен. Выиграла вторая машинка **(<@{}>)**.".format(ctx.message.author.id))
                car2pos = 0
                car2pos = 0
                carready = 0
                carready2 = 0
                game_started = 0
                
                protivnik = discord.Server.get_member(ctx.message.server, user_id=darbis)
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(protivnik, mute_role)
                
                playcar = ""
                darbis = ""
        
                await asyncio.sleep(300)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(protivnik, mute_role)
            elif car1pos == 29:
                await bot.send_message(ctx.message.channel, "Заезд окончен. Ничья.".format(ctx.message.author.id))
                playcar = ""
                darbis = ""
                car2pos = 0
                car2pos = 0
                carready = 0
                carready2 = 0
                game_started = 0
                
@bot.command(pass_context=True) #ПУСТОТА
async def void(ctx, member : discord.Member):
    global voided

    if "Cream" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "Теперь сообщения **{}** затянуты в пустоту.".format(member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/70/Cream_kills_Avdol.png/revision/latest/scale-to-width-down/640?cb=20160331003202")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        voided = member.id
        
@bot.command(pass_context=True) #АНПУСТОТА
async def unvoid(ctx):
    global voided

    if "Cream" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**Пустота открыта.**", description = "*Все выпущены из неё.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/9/9e/Cream_standing.png/revision/latest/scale-to-width-down/421?cb=20150512132612")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        voided = ""
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#4 ЧАСТЬ (не считая KQ)










@bot.command(pass_context=True) #ДОРА РА
@commands.cooldown(1, 8, commands.BucketType.user)
async def dorara(ctx, member : discord.Member):
    global mutesec
    if "Crazy Diamond" in (role.name for role in ctx.message.author.roles):
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            embed = discord.Embed(title = "DORARARA, {}!".format(member.name), description = "*«ДОРАРАРА, {}!»*".format(member.name), color = 0xffff00)
            embed.set_image(url="https://i.imgur.com/6xdbtkW.gif?noredirect")
            await bot.send_message(ctx.message.channel, embed=embed)
        
            if "Tower of Gray" in (role.name for role in member.roles):
                if random.randint(0, 1) == 1:
                    embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                    await bot.send_message(ctx.message.channel, embed=embed)
                    return
                
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
        
            await asyncio.sleep(5)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
            return
        
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Crazy Diamond" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "DORARARA, {}!".format(member.name), description = "*«ДОРАРАРА, {}!»*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://i.imgur.com/6xdbtkW.gif?noredirect")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(5)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True) #РАЗМУТИТЬ
@commands.cooldown(1, 8, commands.BucketType.user)
async def heal(ctx, member : discord.Member):
    global poishot
    if "В муте" not in (role.name for role in member.roles) and member.id != poishot:
        return
    if member.id == ctx.message.author.id:
        embed = discord.Embed(title = "Нельзя вылечить себя, **{}**.".format(ctx.message.author.name), description = "", color = 0xffff00)
        await bot.send_message(ctx.message.channel, embed=embed)
        return
    if "Crazy Diamond" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** вылечил **{}**.".format(ctx.message.author.name, member.name), description = "*{} теперь размучен.*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/22/Crazy_D_heals_Yuya.png/revision/latest/scale-to-width-down/640?cb=20161015203138")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
        if member.id == poishot:
            poishot = ""
        
@bot.command(pass_context=True) #РУКА
async def erase(ctx):
    if "The Hand" in (role.name for role in ctx.message.author.roles):
                
        mgs = []
        async for x in bot.logs_from(ctx.message.channel, limit = 15):
            mgs.append(x)
        await bot.delete_messages(mgs)
        
        embed = discord.Embed(title = "**{}** стёр пространство.".format(ctx.message.author.name), description = "*Сообщения, находившиеся в нём, теперь стёрты.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/2e/The_Hand_swipe.gif")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        
@bot.command(pass_context=True) #ЗВУК
@commands.cooldown(1, 8, commands.BucketType.user)
async def sound(ctx, member : discord.Member, *args):
    global sound
    global soundword
    if "Echoes ACT1" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** написал слово на **{}**.".format(ctx.message.author.name, member.name), description = "*Теперь из него выходит звук.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f5/Echoes_BELIEVE.png/revision/latest/scale-to-width-down/640?cb=20160506192139")
        await bot.send_message(ctx.message.channel, embed=embed)

        act2 = 0
        sound = member.id
        soundword = " ".join(args)
        
@bot.command(pass_context=True) #ЗВУК
@commands.cooldown(1, 8, commands.BucketType.user)
async def soundtwo(ctx, member : discord.Member, *args):
    global sound
    global soundword
    global act2
    if "Echoes ACT2" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** написал действующее слово на **{}**.".format(ctx.message.author.name, member.name), description = "*Теперь звук делает особый эффект.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e8/EchoesACT2_forming_word.png/revision/latest/scale-to-width-down/640?cb=20160527174051")
        await bot.send_message(ctx.message.channel, embed=embed)

        act2 = 1
        sound = member.id
        soundword = " ".join(args)
        
        echoed = discord.Server.get_member(ctx.message.server, user_id=sound)
        await bot.change_nickname(echoed, "{}{}".format(echoed.name, soundword))
        
@bot.command(pass_context=True) #МУТ ЗВУКА
@commands.cooldown(1, 8, commands.BucketType.user)
async def mutesound(ctx):
    global sound
    global soundword
    if "Echoes ACT1" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** стёр слова.".format(ctx.message.author.name), description = "*Перестал создавать звук.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/9/93/Koichi_with_Echoes1.png/revision/latest/scale-to-width-down/640?cb=20160506191915")
        await bot.send_message(ctx.message.channel, embed=embed)

        sound = ""
        soundword = ""
        
    if "Echoes ACT2" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** стёр слова.".format(ctx.message.author.name), description = "*Перестал создавать звук.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/49/EchoesACT2_is_born.png/revision/latest/scale-to-width-down/640?cb=20160527174007")
        await bot.send_message(ctx.message.channel, embed=embed)

        if sound != "":
            echoed = discord.Server.get_member(ctx.message.server, user_id=sound)
            await bot.change_nickname(echoed, echoed.name)
        
        sound = ""
        soundword = ""
    
    if "Echoes ACT3" in (role.name for role in ctx.message.author.roles):
    
        embed = discord.Embed(title = "**{}** стёр слова.".format(ctx.message.author.name), description = "*Перестал создавать звук.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f2/ACT3_explains_its_power.png/revision/latest/scale-to-width-down/640?cb=20160904163230")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if sound != "":
            echoed = discord.Server.get_member(ctx.message.server, user_id=sound)
            await bot.change_nickname(echoed, echoed.name)

        sound = ""
        soundword = ""
        
@bot.command(pass_context=True) #ЗАМОРОЗКА АКТО СРИ
@commands.cooldown(1, 8, commands.BucketType.user)
async def ffreeze(ctx, member : discord.Member):
    global act3freeze
    if "Echoes ACT3" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**S-H-I-T**.", description = "*``«Г-О-В-Н-О»``* **{} был заморожен.**".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/67/ACT3_3_freeze.png/revision/latest/scale-to-width-down/640?cb=20160904163229")
        await bot.send_message(ctx.message.channel, embed=embed)

        act2 = 0
        act3freeze = member.id
        
@bot.command(pass_context=True) #ЗАМОРОЗКА АКТО СРИ
@commands.cooldown(1, 8, commands.BucketType.user)
async def unfreeze(ctx):
    global act3freeze
    if "Echoes ACT3" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**Всё разморожено.**", description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f9/ACT3_posing.png/revision/latest/scale-to-width-down/640?cb=20160904163229")
        await bot.send_message(ctx.message.channel, embed=embed)

        act2 = 0
        act3freeze = ""
        
@bot.command(pass_context=True) #ЗАМОРОЗКА АКТО СРИ
@commands.cooldown(1, 8, commands.BucketType.user)
async def unevolve(ctx):
    global act3freeze
    global act2
    global sound
    global soundword
    global evolving
    
    if "Echoes ACT3" in (role.name for role in ctx.message.author.roles):

        act2 = 0
        act3freeze = ""
        sound = ""
        soundword = ""
        evolving = 0
        
        if sound != "":
            echoed = discord.Server.get_member(ctx.message.server, user_id=sound)
            await bot.change_nickname(echoed, echoed.name)
            
        echoes_act3 = discord.utils.find(lambda r: r.name == 'Echoes ACT3', message.server.roles)
        await bot.remove_roles(ctx.message.author, echoes_act3)
        echoes_egg = discord.utils.find(lambda r: r.name == 'Echoes Egg', message.server.roles)
        await bot.add_roles(ctx.message.author, echoes_egg)
        echoes_act3 = discord.utils.find(lambda r: r.name == 'Echoes ACT3', message.server.roles)
        await bot.remove_roles(ctx.message.author, echoes_act3)
        
        
        
        
@bot.command(pass_context=True) #КНИЖКА
@commands.cooldown(1, 8, commands.BucketType.user)
async def book(ctx, member : discord.Member):
    global booked
    global bites_dust
    if "Heaven's Door" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** превратился в книжку.".format(member.name), description = "*Теперь его можно прочитать.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f1/Heaven%27s_Door_on_Koichi.png/revision/latest/scale-to-width-down/640?cb=20160701183547")
        await bot.send_message(ctx.message.channel, embed=embed)

        booked = member.id
        
        if member.id == bites_dust:
            await bot.send_message(ctx.message.author, embed=embed)
            await bot.send_message(ctx.message.author, "**ЗДЕСЬ НАПИСАНО:**\n**```{}\nТОЖЕ\nБЫЛ\nУБИТ...```**".format(ctx.message.author.name.upper()))
                
            await asyncio.sleep(3)
                
            kiraq = discord.Server.get_member(ctx.message.server, user_id=bites_dust)
            await bot.send_message(ctx.message.author, "**```ОН БЫЛ УБИТ ПРОЗВРЕВШИМ {}```**".format(kiraq.name.upper()))
                
            await asyncio.sleep(3)
                
            embed = discord.Embed(title = "ТРЕТЬЯ БОМБА СМЕРТЕЛЬНОЙ КОРОЛЕВЫ: **ПЫЛЬНЫЙ УКУС**.", description = "「KILLER QUEEN」 DAISAN NO BAKUDAN 「BITES ZA DUSTO」", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/8b/Bites_the_Dust_first.png/revision/latest/scale-to-width-down/640?cb=20161128003634")
            await bot.send_message(ctx.message.author, embed=embed)
            
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, mute_role)

            booked = ""
            return
                
        await bot.send_message(ctx.message.author, embed=embed)
        await bot.send_message(ctx.message.author, "``Список действий над ним:``\n``~setab - поставить абилку на сообщение``\n``~ablist - список абилок``\n``Пассивка: абилка используется, когда`` <@{}> ``напишет`` **``любое``** ``сообщение.``".format(booked))
        
@bot.command(pass_context=True) #КНИЖКА
async def unbook(ctx):
    global booked
    if "Heaven's Door" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**Все** книжки закрыты.", description = "*Теперь никто не читается.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/5d/Rohan_drawing_HD.png/revision/latest/scale-to-width-down/640?cb=20160722203236")
        await bot.send_message(ctx.message.channel, embed=embed)

        booked = ""
        
@bot.command(pass_context=True) #КНИЖКА
async def ablist(ctx):
    global booked
    
    if booked == "":
        return
    if "Heaven's Door" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "Вот список ваших **абилок.**", description = "*Поставить одну из них можно написав ~setab.*", color = 0xffff00)
        embed.add_field(name="~setab 1", value="Гей-порно в ЛС.", inline=True)
        embed.add_field(name="~setab 2", value="Мут на 3 секунды после каждого сообщения.", inline=True)
        embed.add_field(name="~setab 3", value="Уведомление в ЛС после каждого сообщения.", inline=True)
        embed.add_field(name="~setab 4", value="Повторение сообщения на сервере.", inline=True)
    
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/5d/Rohan_drawing_HD.png/revision/latest/scale-to-width-down/640?cb=20160722203236")
        await bot.send_message(ctx.message.author, embed=embed)
        
@bot.command(pass_context=True) #КНИЖКА
async def setab(ctx, abilka : str):
    global booked
    global bookab
    
    if booked == "":
        return
    if "Heaven's Door" in (role.name for role in ctx.message.author.roles):
        
        if abilka == "1":
            embed = discord.Embed(title = "Новая абилка - **{}**".format(abilka), description = "*Гей-порно в ЛС.*", color = 0xffff00)
        elif abilka == "2":
            embed = discord.Embed(title = "Новая абилка - **{}**".format(abilka), description = "*Мут на 3 секунды после каждого сообщения.*", color = 0xffff00)
        elif abilka == "3":
            embed = discord.Embed(title = "Новая абилка - **{}**".format(abilka), description = "*Уведомление в ЛС после каждого сообщения.*", color = 0xffff00)
        elif abilka == "4":
            embed = discord.Embed(title = "Новая абилка - **{}**".format(abilka), description = "*Повторение сообщения на сервере.*", color = 0xffff00)
        else:
            embed = discord.Embed(title = "Абилки с таким номером нет.".format(abilka), description = "Введите номер от 1 до 4.", color = 0xffff00)
    
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/5d/Rohan_drawing_HD.png/revision/latest/scale-to-width-down/640?cb=20160722203236")
        await bot.send_message(ctx.message.author, embed=embed)
        
        bookab = abilka
        
@bot.command(pass_context=True) #ВОДА
@commands.cooldown(1, 8, commands.BucketType.user)
async def aqua(ctx, member : discord.Member):
    global watered
    if "Aqua Necklace" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "Теперь сообщения **{}** *растекаются*.".format(member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a2/Aqua_taunts.png/revision/latest/scale-to-width-down/640?cb=20160401191404")
        await bot.send_message(ctx.message.channel, embed=embed)

        watered = member.id
        
@bot.command(pass_context=True) #ВОДА2
async def unaqua(ctx):
    global watered
    if "Aqua Necklace" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "*Вода перестала течь.*", description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a2/Aqua_taunts.png/revision/latest/scale-to-width-down/640?cb=20160401191404")
        await bot.send_message(ctx.message.channel, embed=embed)

        watered = ""
        
@bot.command(pass_context=True) #ВОДА
@commands.cooldown(1, 8, commands.BucketType.user)
async def targetbad(ctx, member : discord.Member):
    global badtarget
    if "Bad Company" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** поставил новую цель.".format(ctx.message.author.name), description = "*Новая цель - {}.*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/75/BC_prepares_ambush.png/revision/latest/scale-to-width-down/640?cb=20160422201158")
        await bot.send_message(ctx.message.channel, embed=embed)

        badtarget = member.id
        
        
@bot.command(pass_context=True) #СОЛДАТ
async def soldier(ctx, member : discord.Member):
    global mutesec
    global badtarget
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Bad Company" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** нельзя использовать свой стенд.".format(ctx.message.author.name), description = "*Это могут делать только другие люди.*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a8/Bad_Comapny_Anime.png/revision/latest/scale-to-width-down/640?cb=20160422201849")
        await bot.send_message(ctx.message.channel, embed=embed)
        return
    if member.id != badtarget:
        celnii = discord.Server.get_member(ctx.message.server, user_id=badtarget)
        embed = discord.Embed(title = "У вас **другая** цель.", description = "*Стрелять можно только в {}.*".format(celnii.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a8/Bad_Comapny_Anime.png/revision/latest/scale-to-width-down/640?cb=20160422201849")
        await bot.send_message(ctx.message.channel, embed=embed)
        return
        
    embed = discord.Embed(title = "**{}** расстрелял **{}**".format(ctx.message.author.name, member.name), description = "*{} был атакован* **солдатом** *и попал в мут на 2 секунды.*".format(member.name), color = 0xffff00)
    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/17/BC_troops_firing.png/revision/latest/scale-to-width-down/640?cb=20160422201901")
    await bot.send_message(ctx.message.channel, embed=embed)
        
    if "Tower of Gray" in (role.name for role in member.roles):
        if random.randint(0, 1) == 1:
            embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
                
    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
    await bot.add_roles(member, mute_role)
        
    await asyncio.sleep(2)
        
    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
    await bot.remove_roles(member, mute_role)
    
@bot.command(pass_context=True) #ТАНК
@commands.cooldown(1, 8, commands.BucketType.user)
async def tank(ctx, member : discord.Member):
    global mutesec
    global badtarget
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Bad Company" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** нельзя использовать свой стенд.".format(ctx.message.author.name), description = "*Это могут делать только другие люди.*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a8/Bad_Comapny_Anime.png/revision/latest/scale-to-width-down/640?cb=20160422201849")
        await bot.send_message(ctx.message.channel, embed=embed)
        return
    if member.id != badtarget:
        celnii = discord.Server.get_member(ctx.message.server, user_id=badtarget)
        embed = discord.Embed(title = "У вас **другая** цель.", description = "*Стрелять можно только в {}.*".format(celnii.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a8/Bad_Comapny_Anime.png/revision/latest/scale-to-width-down/640?cb=20160422201849")
        await bot.send_message(ctx.message.channel, embed=embed)
        return
        
    embed = discord.Embed(title = "**{}** выстрелил из танка в **{}**".format(ctx.message.author.name, member.name), description = "*{} был атакован* **танком** *и попал в мут на 5 секунд.*".format(member.name), color = 0xffff00)
    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/3e/BC_tank.png/revision/latest/scale-to-width-down/640?cb=20160422201919")
    await bot.send_message(ctx.message.channel, embed=embed)
        
    if "Tower of Gray" in (role.name for role in member.roles):
        if random.randint(0, 1) == 1:
            embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
                
    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
    await bot.add_roles(member, mute_role)
        
    await asyncio.sleep(5)
        
    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
    await bot.remove_roles(member, mute_role)
    
@bot.command(pass_context=True) #ПАРА
@commands.cooldown(1, 8, commands.BucketType.user)
async def para(ctx, member : discord.Member):
    global mutesec
    global badtarget
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Bad Company" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** нельзя использовать свой стенд.".format(ctx.message.author.name), description = "*Это могут делать только другие люди.*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a8/Bad_Comapny_Anime.png/revision/latest/scale-to-width-down/640?cb=20160422201849")
        await bot.send_message(ctx.message.channel, embed=embed)
        return
    if member.id != badtarget:
        celnii = discord.Server.get_member(ctx.message.server, user_id=badtarget)
        embed = discord.Embed(title = "У вас **другая** цель.", description = "*Стрелять можно только в {}.*".format(celnii.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a8/Bad_Comapny_Anime.png/revision/latest/scale-to-width-down/640?cb=20160422201849")
        await bot.send_message(ctx.message.channel, embed=embed)
        return
        
    embed = discord.Embed(title = "**{}** атаковал **{}**".format(ctx.message.author.name, member.name), description = "*{} был атакован* **парашютистом** *и попал в мут на 4 секунды.*".format(member.name), color = 0xffff00)
    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/eb/BC_paratroopers.png/revision/latest/scale-to-width-down/640?cb=20160422201214")
    await bot.send_message(ctx.message.channel, embed=embed)
        
    if "Tower of Gray" in (role.name for role in member.roles):
        if random.randint(0, 1) == 1:
            embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
                
    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
    await bot.add_roles(member, mute_role)
        
    await asyncio.sleep(4)
        
    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
    await bot.remove_roles(member, mute_role)
    
@bot.command(pass_context=True) #ПАРА
@commands.cooldown(1, 20, commands.BucketType.user)
async def heli(ctx, member : discord.Member):
    global mutesec
    global badtarget
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Bad Company" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** нельзя использовать свой стенд.".format(ctx.message.author.name), description = "*Это могут делать только другие люди.*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a8/Bad_Comapny_Anime.png/revision/latest/scale-to-width-down/640?cb=20160422201849")
        await bot.send_message(ctx.message.channel, embed=embed)
        return
    if member.id != badtarget:
        celnii = discord.Server.get_member(ctx.message.server, user_id=badtarget)
        embed = discord.Embed(title = "У вас **другая** цель.", description = "*Стрелять можно только в {}.*".format(celnii.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a8/Bad_Comapny_Anime.png/revision/latest/scale-to-width-down/640?cb=20160422201849")
        await bot.send_message(ctx.message.channel, embed=embed)
        return
        
    embed = discord.Embed(title = "**{}** атаковал из вертолёта **{}**".format(ctx.message.author.name, member.name), description = "*{} был атакован* **вертолётом** *и попал в мут на 10 секунд.*".format(member.name), color = 0xffff00)
    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/68/BC_helicopters.png/revision/latest/scale-to-width-down/640?cb=20160422201910")
    await bot.send_message(ctx.message.channel, embed=embed)
        
    if "Tower of Gray" in (role.name for role in member.roles):
        if random.randint(0, 1) == 1:
            embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
                
    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
    await bot.add_roles(member, mute_role)
        
    await asyncio.sleep(10)
        
    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
    await bot.remove_roles(member, mute_role)
    
@bot.command(pass_context=True) #СОЛНЕЧНЫЙ ЛУЧ
@commands.cooldown(1, 8, commands.BucketType.user)
async def el(ctx, member : discord.Member):
    global voicecharge
    global mutesec
    voicecharges = voicecharge
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
        
    if "Red Hot Chili Pepper" in (role.name for role in ctx.message.author.roles):
        if voicecharge <= 0:
            embed = discord.Embed(title = "У вас нет зарядов, **{}**.".format(ctx.message.author.name), description = "*Зарядитесь электричеством, написав* **``~charge``**".format(ctx.message.author.name), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/31/RHCP_rusting.png/revision/latest/scale-to-width-down/640?cb=20160610191202")
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title = "**{}** шибанул током **{}**.".format(ctx.message.author.name, member.name), description = "``{}`` *атаковали. Он попал в мут на* ``{}`` *секунд.*".format(member.name, voicecharges), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/af/RHCP_annoyed.png/revision/latest/scale-to-width-down/640?cb=20160429214006")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        voicecharge = 0
        
        await asyncio.sleep(voicecharges)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
        
@bot.command(pass_context=True) #ЗАМОК
async def lock(ctx, member : discord.Member):
    global locked
    global mon
    if "The Lock" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** закрепил замок на **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/2e/The_Lock_on_Koichi.png/revision/latest/scale-to-width-down/640?cb=20160506192703")
        await bot.send_message(ctx.message.channel, embed=embed)

        locked = member.id
        
@bot.command(pass_context=True) #МОНЕТ
async def mcheck(ctx):
    global locked
    global mon
    if "The Lock" in (role.name for role in ctx.message.author.roles):
        if locked != "":
            await bot.send_message(ctx.message.author, "``Замок закреплён на`` <@{}>.".format(locked))
        else:
            await bot.send_message(ctx.message.author, "```Замок не закреплён.```".format(locked))
        await bot.send_message(ctx.message.author, "У вас ``{}`` монет.\n```~mute - замутить на 5 минут (15 монет)```\n```~mnick (юзер) (ник) - поменять ник кому-нибудь (30 монет)```\n```~mbomb - убрать все бомбы, книжку и звуки (60 монет)```".format(mon))
        

@bot.command(pass_context=True) #МУТ
async def mute(ctx, member : discord.Member):
    global locked
    global mon
    global stealed
    if "The Lock" in (role.name for role in ctx.message.author.roles):
        if mon >= 15:
            
            mon -= 15
            embed = discord.Embed(title = "**{}** замутил за деньги **{}** на 5 минут.".format(ctx.message.author.name, member.name), description = "У него осталось **{}** монет.".format(mon), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
            
            await asyncio.sleep(300)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
        
        
        else:
            
            embed = discord.Embed(title = "У **{}** недостаточно монет.".format(ctx.message.author.name), description = "**{}** монет.".format(mon), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(ctx.message.channel, embed=embed)
            
    if "Soft and Wet" in (role.name for role in ctx.message.author.roles):
        if stealed == 0:
            await bot.send_message(ctx.message.channel, "У вас нет зарядов.")
            return
        if "Ebony Devil" in (role.name for role in member.roles):
            mutesec += 1
        if "В муте" in (role.name for role in member.roles):
            return
        embed = discord.Embed(title = "**{}** атаковал **{}**".format(ctx.message.author.name, member.name), description = "*Мут на {} секунд.*".format(stealed), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/9/9a/S%26WManga.png/revision/latest/scale-to-width-down/350?cb=20160108110654")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        stealing = stealed
        stealed = 0
        
        await asyncio.sleep(stealing)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
            
@bot.command(pass_context=True) #НИК
async def mnick(ctx, member : discord.Member, *args):
    global locked
    global mon
    if "The Lock" in (role.name for role in ctx.message.author.roles):
        if mon >= 30:
            
            nickk = ' '.join(args)

            mon -= 30
            embed = discord.Embed(title = "**{}** поменял ник **{}** на **{}**.".format(ctx.message.author.name, member.name, nickk), description = "У него осталось **{}** монет.".format(mon), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            await bot.change_nickname(member, nickk)
        
        
        else:
            
            embed = discord.Embed(title = "У **{}** недостаточно монет.".format(ctx.message.author.name), description = "**{}** монет.".format(mon), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(ctx.message.channel, embed=embed)
            
@bot.command(pass_context=True) #НИК
async def mbomb(ctx):
    global locked
    global mon
    global booked
    global sound
    global soundword
    global sha_bomb
    global user_bomb
    global sha_bombe
    global sha_bombe2
    global sha_bombe3
    global sha_bombe4
    if "The Lock" in (role.name for role in ctx.message.author.roles):
        if mon >= 60:
            
            mon -= 60
            embed = discord.Embed(title = "**{}** снял некоторые эффекты стендов.".format(ctx.message.author.name), description = "У него осталось **{}** монет.".format(mon), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            sound = ""
            soundword = ""
            sha_bomb = ""
            sha_bombe = ""
            sha_bombe2 = ""
            sha_bombe3 = ""
            sha_bombe4 = ""
            user_bomb = ""
            booked = ""
        
        
        else:
            
            embed = discord.Embed(title = "У **{}** недостаточно монет.".format(ctx.message.author.name), description = "**{}** монет.".format(mon), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d8/The_Lock_AV.png/revision/latest/scale-to-width-down/350?cb=20160526194516")
            await bot.send_message(ctx.message.channel, embed=embed)
            
@bot.command(pass_context=True) #КУКЛА
async def manq(ctx, member : discord.Member):
    global maniq
    if "Surface" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** сделал **{}** куклой.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/42/Surface_returned_to_wood.png/revision/latest/scale-to-width-down/640?cb=20160513195608")
        await bot.send_message(ctx.message.channel, embed=embed)

        maniq = member.id
        
@bot.command(pass_context=True) #КУКЛА
async def unmanq(ctx):
    global maniq
    global mimi
    if "Surface" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** уничтожил куклу.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/83/Surface_destroyed.png/revision/latest/scale-to-width-down/640?cb=20160513195620")
        await bot.send_message(ctx.message.channel, embed=embed)

        maniq = ""
        mimi = ""
        
@bot.command(pass_context=True) #КУКЛА
async def mimicry(ctx, member : discord.Member):
    global mimi
    global maniq
    if maniq == "":
        return
    if member.id == maniq:
        embed = discord.Embed(title = "**Кукла** и **этот человек** должны быть разные люди.", description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/42/Surface_returned_to_wood.png/revision/latest/scale-to-width-down/640?cb=20160513195608")
        await bot.send_message(ctx.message.channel, embed=embed)
        return
    if "Surface" in (role.name for role in ctx.message.author.roles):
        kuklaebatb = discord.Server.get_member(ctx.message.server, user_id=maniq)
        embed = discord.Embed(title = "**{}** превратил куклу **({})** в **{}**.".format(ctx.message.author.name, kuklaebatb.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/88/Surface_as_Josuke.png/revision/latest/scale-to-width-down/640?cb=20160513195210")
        await bot.send_message(ctx.message.channel, embed=embed)

        mimi = member.id
        
@bot.command(pass_context=True) #КУКЛА
async def lovedeluxe(ctx, *wordss):
    global lovedel
    if "Love Deluxe" in (role.name for role in ctx.message.author.roles):
        lovedel = ' '.join(wordss)
        embed = discord.Embed(title = "**{}** - теперь новое слово, **{}**.".format(lovedel, ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/db/Yukako_attacks_Koichi.png/revision/latest/scale-to-width-down/640?cb=20160527183415")
        await bot.send_message(ctx.message.channel, embed=embed)
        
@bot.command(pass_context=True) #КУКЛА
async def undel(ctx):
    global lovedel
    if "Love Deluxe" in (role.name for role in ctx.message.author.roles):
        lovedel = ""
        embed = discord.Embed(title = "Слово убрано, **{}**.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/78/Yukako%27s_white_hair.png/revision/latest/scale-to-width-down/640?cb=20160527174034")
        await bot.send_message(ctx.message.channel, embed=embed)
        
@bot.command(pass_context=True) #КУКЛА
async def feed(ctx, member : discord.Member):
    if "Здоровый" in (role.name for role in member.roles):
        await bot.send_message(ctx.message.channel, "<@{}> уже здоров.".format(member.id))
        return
    if "Pearl Jam" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** накормил **{}** *итким блюдом*.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/39/PearlJamOkuyasuGuts.jpg/revision/latest/scale-to-width-down/640?cb=20170204192747")
        await bot.send_message(ctx.message.channel, embed=embed)

        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        await asyncio.sleep(300)
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
        zdorovii = discord.utils.find(lambda r: r.name == 'Здоровый', ctx.message.server.roles)
        await bot.add_roles(member, zdorovii)
        
        embed = discord.Embed(title = "**{}** полностью здоров.".format(member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/74/Okuyasu_feeling_refreshed.png/revision/latest/scale-to-width-down/640?cb=20160603202410")
        await bot.send_message(ctx.message.channel, embed=embed)
        
@bot.command(pass_context=True) #КУКЛА
async def poishot(ctx, member : discord.Member):
    global poisoned
    global messagoison
    global BOT_ID
    if member.id == BOT_ID:
        return
    if "Ratt" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** выстрелил ядом в **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b7/Ratt%27s_scope.png/revision/latest/scale-to-width-down/640?cb=20160715205610")
        await bot.send_message(ctx.message.channel, embed=embed)

        poisoned = member.id
        messagoison = ""
        
@bot.command(pass_context=True) #СОБИРАТЕЛЬ
async def collects(ctx):
    global harvatiya
    if "Harvest" in (role.name for role in ctx.message.author.roles):
        
        await bot.send_message(ctx.message.author, "У вас **{}** ``рофлан-коинов``".format(harvatiya))
        await bot.send_message(ctx.message.author, "***Рофлан-прайс-лист:***\n```~harvmute - замутить кого-нибудь на 5 минут (50 рофлан-коинов)\n~harvmmute - замутить на 10 минут (100 рофлан-коинов)```")
        
@bot.command(pass_context=True) #МУТ
async def harvmute(ctx, member : discord.Member):
    global harvatiya
    if "Harvest" in (role.name for role in ctx.message.author.roles):
        if harvatiya >= 50:
            
            harvatiya -= 50
            embed = discord.Embed(title = "**{}** атаковал собирателями **{}** за 50 рофлан-коинов.".format(ctx.message.author.name, member.name), description = "У **{}** осталось **{}** коинов. **{}** попал в мут на 5 минут.".format(ctx.message.author.name, harvatiya, member.name), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/72/Harvest_attacking_Okuyasu.png/revision/latest/scale-to-width-down/640?cb=20160806072414")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
            
            await asyncio.sleep(300)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
        
        
        else:
            
            embed = discord.Embed(title = "У **{}** недостаточно рофлан-коинов.".format(ctx.message.author.name), description = "**{}** рофлан-коинов.".format(harvatiya), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e5/Harvest_finds_a_coin.png/revision/latest/scale-to-width-down/640?cb=20160729224801")
            await bot.send_message(ctx.message.channel, embed=embed)
            
@bot.command(pass_context=True) #МУТ
async def harvmmute(ctx, member : discord.Member):
    global harvatiya
    if "Harvest" in (role.name for role in ctx.message.author.roles):
        if harvatiya >= 100:
            
            harvatiya -= 100
            embed = discord.Embed(title = "**{}** атаковал собирателями **{}** за 100 рофлан-коинов.".format(ctx.message.author.name, member.name), description = "У **{}** осталось **{}** коинов. **{}** попал в мут на 10 минут.".format(ctx.message.author.name, harvatiya, member.name), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/72/Harvest_attacking_Okuyasu.png/revision/latest/scale-to-width-down/640?cb=20160806072414")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
            
            await asyncio.sleep(600)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
        
        
        else:
            
            embed = discord.Embed(title = "У **{}** недостаточно рофлан-коинов.".format(ctx.message.author.name), description = "**{}** рофлан-коинов.".format(harvatiya), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e5/Harvest_finds_a_coin.png/revision/latest/scale-to-width-down/640?cb=20160729224801")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            
@bot.command(pass_context=True) #ЗОЛУШКА
async def form(ctx, member : discord.Member):
    global changenickcan
    
    if ctx.message.author.id == member.id:
        await bot.send_message(ctx.message.channel, "**Нельзя использовать этот стенд на себе.**")
        return
    if "Cinderella" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** дал возможность поменять ник **{}**.".format(ctx.message.author.name, member.name), description = "*Это можно сделать, написав:* ``~newname (ник)``", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/dc/Cinderella_summons_faces.png/revision/latest/scale-to-width-down/640?cb=20160812181025")
        await bot.send_message(ctx.message.channel, embed=embed)
        changenickcan = member.id
        
        
@bot.command(pass_context=True) #ЗОЛУШКА
async def newname(ctx, *args):
    global changenickcan
    if ctx.message.author.id == changenickcan:
        
        if random.randint(0, 2) == 1:
            newnick = ' '.join(args)
        else:
            lolnicks = ["Пидор", "Питуч галимый", "сосу бесплатно", "ОПА, ТВОЯ МАТЬ ОПА", "Раб Фуфа", "Радужный поник", "Единорог", "Артём Киселёв", "Весёлая Члениха", "Трапский чечник", "хочу умереть", "долбаёб", "Эйс пидор", "убейте меня", "пососный отсос", "ПУТЕН ЛОХ", "http://natribu.org", "ПИЗДАБОЛЛ"]
            newnick = random.choice(lolnicks)
        embed = discord.Embed(title = "**{}** поменял ник на **{}**.".format(ctx.message.author.name, newnick), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/dc/Cinderella_summons_faces.png/revision/latest/scale-to-width-down/640?cb=20160812181025")
        await bot.send_message(ctx.message.channel, embed=embed)
        await bot.change_nickname(ctx.message.author, newnick)

        changenickcan = ""
        
@bot.command(pass_context=True) #СТРЕЛА
async def arrow(ctx, member : discord.Member):
    if "Matured" in (role.name for role in member.roles):
        return
    if "Atom Heart Father" in (role.name for role in ctx.message.author.roles):
        if "Killer Queen" in (role.name for role in member.roles):
            if "Alternate" in (role.name for role in member.roles):
                return
            embed = discord.Embed(title = "**{}** проткнул стрелой **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://cdn.discordapp.com/attachments/472313657661980672/474280017875042332/8661d78d8d75e176.PNG")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            if "Matured" not in (role.name for role in member.roles):
                mute_role = discord.utils.find(lambda r: r.name == 'Matured', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
            
                await bot.send_message(member, "ВАШ СТЕНД **(СМЕРТЕЛЬНАЯ КОРОЛЕВА)** ОБРЁЛ ТРЕТЬЮ СПОСОБНОСТЬ.")
            else:
                await bot.send_message(ctx.message.channel, "Никакого эффекта.")
            return
            
        if "Gold Experience" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** проткнул стрелой **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f0/RequiemAwake.png/revision/latest/scale-to-width-down/549?cb=20161201030833")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            if "Requiem" not in (role.name for role in member.roles):
                req = discord.utils.find(lambda r: r.name == 'Requiem', ctx.message.server.roles)
                await bot.add_roles(member, req)
            
                await bot.send_message(member, "ПРОБУДИЛСЯ **РЕКВИЕМ ВАШЕГО СТЕНДА.**")
            else:
                await bot.send_message(ctx.message.channel, "Никакого эффекта.")
            return
            
        if "Silver Chariot" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** проткнул стрелой **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/5b/SilverChariotPierced.png/revision/latest/scale-to-width-down/358?cb=20180609131657")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            if "Requiem" not in (role.name for role in member.roles):
                req = discord.utils.find(lambda r: r.name == 'Requiem', ctx.message.server.roles)
                await bot.add_roles(member, req)
            
                await bot.send_message(member, "ПРОБУДИЛСЯ **РЕКВИЕМ ВАШЕГО СТЕНДА.**")
            else:
                await bot.send_message(ctx.message.channel, "Никакого эффекта.")
            return
            
        if "Made in Heaven" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** проткнул стрелой **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/27/MadeinHeaven.png/revision/latest/scale-to-width-down/312?cb=20140924111429")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            if "Requiem" not in (role.name for role in member.roles):
                req = discord.utils.find(lambda r: r.name == 'Requiem', ctx.message.server.roles)
                await bot.add_roles(member, req)
            
                await bot.send_message(member, "ПРОБУДИЛСЯ **РЕКВИЕМ ВАШЕГО СТЕНДА.**")
            else:
                await bot.send_message(ctx.message.channel, "Никакого эффекта.")
            return
            
        if "Crazy Diamond" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** проткнул стрелой **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/c5/Crazy_Diamond_Anime.png/revision/latest/scale-to-width-down/350?cb=20160414081459")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            if "Requiem" not in (role.name for role in member.roles):
                req = discord.utils.find(lambda r: r.name == 'Requiem', ctx.message.server.roles)
                await bot.add_roles(member, req)
            
                await bot.send_message(member, "ПРОБУДИЛСЯ **РЕКВИЕМ ВАШЕГО СТЕНДА.**")
            else:
                await bot.send_message(ctx.message.channel, "Никакого эффекта.")
            return
            
        if "The World" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** проткнул стрелой **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b2/Twoh.png/revision/latest/scale-to-width-down/350?cb=20151229005251")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            if "Over Heaven" not in (role.name for role in member.roles):
                req = discord.utils.find(lambda r: r.name == 'Over Heaven', ctx.message.server.roles)
                await bot.add_roles(member, req)
            
                await bot.send_message(member, "ПРОБУДИЛСЯ **ЗЕ ВОРЛД ОВЕР ХЭВЭН.**")
            else:
                await bot.send_message(ctx.message.channel, "Никакого эффекта.")
            return
            
        if "Star Platinum" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** проткнул стрелой **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d7/Star_p_1.PNG/revision/latest/scale-to-width-down/417?cb=20170217073356")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            if "Over Heaven" not in (role.name for role in member.roles):
                req = discord.utils.find(lambda r: r.name == 'Over Heaven', ctx.message.server.roles)
                await bot.add_roles(member, req)
            
                await bot.send_message(member, "ПРОБУДИЛСЯ **СТАР ПЛАТИНУМ ОВЕР ХЭВЭН.**")
            else:
                await bot.send_message(ctx.message.channel, "Никакого эффекта.")
            return
            
        if "Roflan Crusader" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** проткнул стрелой **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://cdn.discordapp.com/emojis/478437941967060993.gif?v=1")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            if "Over Heaven" in (role.name for role in member.roles):
                await bot.send_message(ctx.message.channel, "Никакого эффекта.")
                return
            if "Requiem" not in (role.name for role in member.roles):
                req = discord.utils.find(lambda r: r.name == 'Requiem', ctx.message.server.roles)
                await bot.add_roles(member, req)
            
                await bot.send_message(member, "ПРОБУДИЛСЯ **РЕКВИЕМ ВАШЕГО СТЕНДА.**")
            else:
                if "Over Heaven" not in (role.name for role in member.roles):
                    req = discord.utils.find(lambda r: r.name == 'Requiem', ctx.message.server.roles)
                    await bot.remove_roles(member, req)
                    
                    req2 = discord.utils.find(lambda r: r.name == 'Over Heaven', ctx.message.server.roles)
                    await bot.add_roles(member, req2)
                else:
                    await bot.send_message(ctx.message.channel, "Никакого эффекта.")
                    
        if "Black Sabbath" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** поглотил стрелу.".format(member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/9/9b/BS_Killing_a_oldman.png/revision/latest/scale-to-width-down/625?cb=20150626050150")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            req2 = discord.utils.find(lambda r: r.name == 'Atom Heart Father', ctx.message.server.roles)
            await bot.add_roles(member, req2)
            return
            
        embed = discord.Embed(title = "**{}** запустил стрелу в **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/2c/Yoshihiro_with_the_Arrow.png/revision/latest/scale-to-width-down/640?cb=20170409194539")
        await bot.send_message(ctx.message.channel, embed=embed)
            
        if random.randint(0, 4) == 4:
            await bot.send_message(ctx.message.channel, "**{}** попал в мут на ``5 минут.``".format(member.name))
                
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
            
            await asyncio.sleep(300)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
        else:
            await bot.send_message(ctx.message.channel, "Никакого эффекта.")
                
                
@bot.command(pass_context=True) #СТРЕЛА
async def bite(ctx):
    global bites_dust
    if bites_dust != ctx.message.author.id:
        if "Killer Queen" in (role.name for role in ctx.message.author.roles):
            if "Matured" in (role.name for role in ctx.message.author.roles):
            
                embed = discord.Embed(title = "Вы активировали **``ПЫЛЬНЫЙ УКУС``**.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/8b/Bites_the_Dust_first.png/revision/latest/scale-to-width-down/640?cb=20161128003634")
                await bot.send_message(ctx.message.author, embed=embed)
            
                bites_dust = ctx.message.author.id
            
@bot.command(pass_context=True)
async def rps(ctx, member : discord.Member):
    global rps
    global player1choose
    global player2choose
    global choosed
    global readyplay
    global readyplayer1
    global readyplayer2
    
    if readyplay != "":
        return
        
    if "Boy II Man" in (role.name for role in ctx.message.author.roles):
            
        embed = discord.Embed(title = "Вы предложили **{}** сыграть в КНБ.".format(member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/c0/Ken_summons_B2M.png/revision/latest/scale-to-width-down/640?cb=20170409191444")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        rps = ctx.message.author.id
        player1choose = ""
        player1choose = ""
        readyplay = ""
        choosed = member.id
        readyplayer1 = 0
        readyplayer2 = 0
        
        await bot.send_message(member, "**Если вы готовы сыграть в КНБ, напишите:** ``~readytoplay``")
        
@bot.command(pass_context=True)
async def readytoplay(ctx):
    global rps
    global player1choose
    global player2choose
    global choosed
    global readyplay
    global readyplayer1
    global readyplayer2
    global randomrock
    global randompaper
    global randomscissors
    global randomrock2
    global randompaper2
    global randomscissors2
    
    if readyplay != "":
        return
        
    if ctx.message.author.id == choosed:
        await bot.send_message(ctx.message.channel, "<@{}> готов сыграть в **КНБ**, <@{}>.".format(ctx.message.author.id, rps))
        
        readyplay = ctx.message.author.id
        choosed = ""
        
        knbPlayer = discord.Server.get_member(ctx.message.server, user_id=rps)
        await bot.send_message(knbPlayer, "**Если вы победите в КНБ, то <@{}> попадёт в мут.**".format(ctx.message.author.id))
        await bot.send_message(ctx.message.author, "**Если вы победите в КНБ, то <@{}> попадёт в мут.**".format(rps))
        
        randomrock = "{}".format(random.randint(0, 150))
        randompaper = "{}".format(random.randint(0, 150))
        randomscissors = "{}".format(random.randint(0, 150))
        randomrock2 = "{}".format(random.randint(0, 150))
        randompaper2 = "{}".format(random.randint(0, 150))
        randomscissors2 = "{}".format(random.randint(0, 150))
        await bot.send_message(knbPlayer, "**Поставить камень -** ``~rpsset {}``\n**Поставить ножницы -** ``~rpsset {}``\n**Поставить бумагу -** ``~rpsset {}``\n``~rpsready - готов``".format(randomrock, randomscissors, randompaper))
        await bot.send_message(ctx.message.author, "**Поставить камень -** ``~rpsset {}``\n**Поставить ножницы -** ``~rpsset {}``\n**Поставить бумагу -** ``~rpsset {}``\n``~rpsready - готов``".format(randomrock2, randomscissors2, randompaper2))
        
@bot.command(pass_context=True)
async def rpsset(ctx, vibral : str):
    global rps
    global player1choose
    global player2choose
    global choosed
    global readyplay
    global readyplayer1
    global readyplayer2
    global randomrock
    global randompaper
    global randomscissors
    global randomrock2
    global randompaper2
    global randomscissors2
    
    if ctx.message.author.id == readyplay:
        if readyplayer2 == 1:
            return
        if vibral == str(randomrock2):
            await bot.send_message(ctx.message.author, "**Вы выбрали** ``камень``")
            player2choose = "rock"
        if vibral == str(randomscissors2):
            await bot.send_message(ctx.message.author, "**Вы выбрали** ``ножницы``")
            player2choose = "scissors"
        if vibral == str(randompaper2):
            await bot.send_message(ctx.message.author, "**Вы выбрали** ``бумагу``")
            player2choose = "paper"

    if readyplay == "":
        return
    if ctx.message.author.id == rps:
        if readyplayer1 == 1:
            return
        if vibral == str(randomrock):
            await bot.send_message(ctx.message.author, "**Вы выбрали** ``камень``")
            player1choose = "rock"
        if vibral == str(randomscissors):
            await bot.send_message(ctx.message.author, "**Вы выбрали** ``ножницы``")
            player1choose = "scissors"
        if vibral == str(randompaper):
            await bot.send_message(ctx.message.author, "**Вы выбрали** ``бумагу``")
            player1choose = "paper"
            
@bot.command(pass_context=True)
async def rpsready(ctx):
    global rps
    global player1choose
    global player2choose
    global choosed
    global readyplay
    global readyplayer1
    global readyplayer2
    
    if ctx.message.author.id == readyplay:
        if player2choose == "":
            await bot.send_message(ctx.message.author, "Для начала поставьте что-нибудь.")
        else:
            readyplayer2 = 1
            await bot.send_message(ctx.message.channel, "<@{}> готов. Ожидаем противника...".format(ctx.message.author.id))
        
        if readyplayer1 == 1:
            await bot.send_message(ctx.message.channel, "Противник готов, результат через 5 секунд.")
            await asyncio.sleep(5)
            
            if player2choose == "rock":
                if player1choose == "paper":
                    await bot.send_message(ctx.message.channel, "Выиграл противник (<@{}>). Вы в муте.".format(rps))
                    
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                    await bot.add_roles(ctx.message.author, mute_role)
                    
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    

                elif player1choose == "scissors":
                    await bot.send_message(ctx.message.channel, "Вы победили. Ваш противник в муте.")
                    
                    knbPlayer = discord.Server.get_member(ctx.message.server, user_id=rps)
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                    await bot.add_roles(knbPlayer, mute_role)
                    
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    
                else:
                        
                    await bot.send_message(ctx.message.channel, "Ничья.")
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    
            if player2choose == "paper":
                if player1choose == "scissors":
                    await bot.send_message(ctx.message.channel, "Выиграл противник (<@{}>). Вы в муте.".format(rps))
                    
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                    await bot.add_roles(ctx.message.author, mute_role)
                    
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    

                elif player1choose == "rock":
                    await bot.send_message(ctx.message.channel, "Вы победили. Ваш противник в муте.")
                    
                    knbPlayer = discord.Server.get_member(ctx.message.server, user_id=rps)
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                    await bot.add_roles(knbPlayer, mute_role)
                    
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    
                else:
                        
                    await bot.send_message(ctx.message.channel, "Ничья.")
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    
            if player2choose == "scissors":
                if player1choose == "rock":
                    await bot.send_message(ctx.message.channel, "Выиграл противник (<@{}>). Вы в муте.".format(rps))
                    
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                    await bot.add_roles(ctx.message.author, mute_role)
                    
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    

                elif player1choose == "paper":
                    await bot.send_message(ctx.message.channel, "Вы победили. Ваш противник в муте.")
                    
                    knbPlayer = discord.Server.get_member(ctx.message.server, user_id=rps)
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                    await bot.add_roles(knbPlayer, mute_role)
                    
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    
                else:
                        
                    await bot.send_message(ctx.message.channel, "Ничья.")
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    
    if readyplay == "":
        return
    if ctx.message.author.id == rps:
        if player1choose == "":
            await bot.send_message(ctx.message.author, "Для начала поставьте что-нибудь.")
        else:
            readyplayer1 = 1
            await bot.send_message(ctx.message.channel, "<@{}> готов. Ожидаем противника...".format(ctx.message.author.id))
        
        if readyplayer2 == 1:
            await bot.send_message(ctx.message.channel, "Противник готов, результат через 5 секунд.")
            await asyncio.sleep(5)
            
            if player1choose == "rock":
                if player2choose == "paper":
                    await bot.send_message(ctx.message.channel, "Выиграл противник (<@{}>). Вы в муте.".format(readyplay))
                    
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                    await bot.add_roles(ctx.message.author, mute_role)
                    
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    

                elif player2choose == "scissors":
                    await bot.send_message(ctx.message.channel, "Вы победили. Ваш противник в муте.")
                    
                    knbPlayer = discord.Server.get_member(ctx.message.server, user_id=readyplay)
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                    await bot.add_roles(knbPlayer, mute_role)
                    
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    
                else:
                        
                    await bot.send_message(ctx.message.channel, "Ничья.")
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    
            if player1choose == "paper":
                if player2choose == "scissors":
                    await bot.send_message(ctx.message.channel, "Выиграл противник (<@{}>). Вы в муте.".format(readyplay))
                    
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                    await bot.add_roles(ctx.message.author, mute_role)
                    
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    

                elif player2choose == "rock":
                    await bot.send_message(ctx.message.channel, "Вы победили. Ваш противник в муте.")
                    
                    knbPlayer = discord.Server.get_member(ctx.message.server, user_id=readyplay)
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                    await bot.add_roles(knbPlayer, mute_role)
                    
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    
                else:
                        
                    await bot.send_message(ctx.message.channel, "Ничья.")
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    
            if player1choose == "scissors":
                if player2choose == "rock":
                    await bot.send_message(ctx.message.channel, "Выиграл противник (<@{}>). Вы в муте.".format(readyplay))
                    
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                    await bot.add_roles(ctx.message.author, mute_role)
                    
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    

                elif player2choose == "paper":
                    await bot.send_message(ctx.message.channel, "Вы победили. Ваш противник в муте.")
                    
                    knbPlayer = discord.Server.get_member(ctx.message.server, user_id=readyplay)
                    mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                    await bot.add_roles(knbPlayer, mute_role)
                    
                    choosed = ""
                    readyplay = ""
                    rps = ""
                    
                else:
                        
                    await bot.send_message(ctx.message.channel, "Ничья.")
                    choosed = ""
                    readyplay = ""
                    rps = ""
        
@bot.command(pass_context=True) #РАЗМУТИТЬ СЕБЯ
async def morph(ctx, *nicknam):

    if "Earth Wind and Fire" in (role.name for role in ctx.message.author.roles):
        
        newnick = ' '.join(nicknam)
        
        embed = discord.Embed(title = "**{}** стал **{}**.".format(ctx.message.author.name, newnick), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/75/Mikitaka_using_EW%26F.png/revision/latest/scale-to-width-down/640?cb=20160930225803")
        await bot.send_message(ctx.message.channel, embed=embed)

        await bot.change_nickname(ctx.message.author, newnick)
        
@bot.command(pass_context=True) #СОЗДАТЬ
async def room(ctx, roomN : str):

    if "Highway Star" in (role.name for role in ctx.message.author.roles):
        
        newroom = ' '.join(roomN)
        embed = discord.Embed(title = "**{}** создал новую комнату **{}**.".format(ctx.message.author.name, newroom), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/7a/Highway_Star_manifests_itself.png/revision/latest/scale-to-width-down/640?cb=20161007225611")
        await bot.send_message(ctx.message.channel, embed=embed)

        everyone = discord.PermissionOverwrite(read_messages=False)
        mine = discord.PermissionOverwrite(read_messages=True)
        
        newchannel = await bot.create_channel(ctx.message.server, newroom, (ctx.message.server.default_role, everyone), (ctx.message.author, mine))
        
        await asyncio.sleep(60)
        
        await bot.delete_channel(newchannel)
        
@bot.command(pass_context=True) #СОСАТЬ
async def suck(ctx, member : discord.Member):
    global highw
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if ctx.message.author.id == member.id:
        return
    if "Highway Star" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** стал новой целью **{}**.".format(member.name, ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/dd/HS_burrows_into_Rohan.png/revision/latest/scale-to-width-down/640?cb=20161007225428")
        await bot.send_message(ctx.message.channel, embed=embed)

        highw = member.id
        
@bot.command(pass_context=True) #ВОЗДУХ АТАКА
async def airshoot(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Stray Cat" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** выстрелил воздухом в **{}**".format(ctx.message.author.name, member.name), description = "*«Мяу»*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e0/Stray_Cat_Shooting_Air.gif")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(6)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True) #ЗОЛУШКА
async def reflect(ctx, member : discord.Member):
    global reflecting
    
    if ctx.message.author.id == member.id:
        await bot.send_message(ctx.message.channel, "**Нельзя использовать этот стенд на себе.**")
        return
    if "Super Fly" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** теперь отражает мут в **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/6e/SF_Damage_Reverse.gif/revision/latest?cb=20161028193303")
        await bot.send_message(ctx.message.channel, embed=embed)
        reflecting = member.id
        
@bot.command(pass_context=True) #БУМАЖКА
async def paper(ctx, member : discord.Member):
    global wutface
    
    if ctx.message.author.id == member.id:
        await bot.send_message(ctx.message.channel, "**Нельзя использовать этот стенд на себе.**")
        return
    if "Enigma" in (role.name for role in ctx.message.author.roles):
        if member.id == wutface:
            embed = discord.Embed(title = "**{}** превратил в бумагу **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/45/Enigma_power.gif")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            wutface = ""
            
            paperrole = discord.utils.find(lambda r: r.name == "Превращён в бумагу", ctx.message.server.roles)
            
            if paperrole is None:
                await bot.create_role(ctx.message.author.server, name="Превращён в бумагу")
                papersrole = discord.utils.find(lambda r: r.name == "Превращён в бумагу", ctx.message.server.roles)
                await bot.add_roles(member, papersrole)
            else:
                await bot.add_roles(member, paperrole)
                
@bot.command(pass_context=True) #ШЁПОТ
async def whisper(ctx, member : discord.Member, *args):

    if "Cheap Trick" in (role.name for role in ctx.message.author.roles):
        whispering = ' '.join(args)
        await bot.delete_message(ctx.message)
        await bot.send_message(member, "*{}*".format(whispering))
        
@bot.command(pass_context=True) #РОФЛАН
async def rofl(ctx):

    if "Roflan Crusader" in (role.name for role in ctx.message.author.roles):
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            randomebalo = ['<:roflanEbalo:432615847794835457>', '<:roflanPride:467261074085904394>', '<:fedorAhuelEbalo:464441709070385182>', '<a:roflanLUL:478437941967060993>']
        else:
            randomebalo = ['<:roflanEbalo:432615847794835457>', '<:roflanPride:467261074085904394>', '<:fedorAhuelEbalo:464441709070385182>']
        await bot.send_message(ctx.message.channel, random.choice(randomebalo))
        
@bot.command(pass_context=True) #РОФЛАН
async def degr(ctx, member : discord.Member):
    global degrod
    global degradations
    global degradations2
    
    degradations2 = round(degradations / 2.5)
    if degradations2 < 0:
        degradations2 = 0

    if "Roflan Crusader" in (role.name for role in ctx.message.author.roles):
        degrod = member.id
        if "Over Heaven" in (role.name for role in ctx.message.author.roles):
            await asyncio.sleep(degradations)
        elif "Requiem" in (role.name for role in ctx.message.author.roles):
            await asyncio.sleep(45)
        else:
            await asyncio.sleep(35)
        degrod = ""
        
        
@bot.command(pass_context=True) #РОФЛАН
async def ultradegr(ctx):
    global degrodi
    global degradations
    global degradations2
    
    degradations2 = round(degradations / 2.5)
    if degradations2 < 0:
        degradations2 = 0

    if "Roflan Crusader" in (role.name for role in ctx.message.author.roles):
        if "Over Heaven" in (role.name for role in ctx.message.author.roles):
            degrodi = 1
            await asyncio.sleep(degradations2)
            degrodi = 0
        elif "Requiem" in (role.name for role in ctx.message.author.roles):
            degrodi = 1
            await asyncio.sleep(7)
            degrodi = 0
        
        
        
        
        
        
        
        
        
#5 ЧАСТЬ

@bot.command(pass_context=True) #РАЗМУТИТЬ
@commands.cooldown(1, 25, commands.BucketType.user)
async def glife(ctx, member : discord.Member):
    global newlife
    global BOT_ID
    if "Gold Experience" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** создал жизнь в **{}**.".format(ctx.message.author.name, member.name), description = "*{} снова обрёл жизнь.*".format(member.name), color = 0xffff00)
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            embed.set_image(url="https://cdn.discordapp.com/attachments/473403386599964672/476410589523083284/5cd2cbe5528d28cc.PNG")
        else:
            embed.set_image(url="https://cdn.discordapp.com/attachments/473403386599964672/476410589523083284/5cd2cbe5528d28cc.PNG")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        if "В муте" in (role.name for role in member.roles):
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
            
        else:
            if member == ctx.message.author:
                await bot.send_message(ctx.message.channel, "Нельзя использовать эту абилку на себе.")
                return
            if member.id == BOT_ID:
                await bot.send_message(ctx.message.channel, "Нельзя использовать эту абилку на этом юзере.")
                return
            newlife = member.id
            await asyncio.sleep(15)
            newlife = ""
        
@bot.command(pass_context=True) #ОБНУЛ
async def zero(ctx, member : discord.Member):
    global zeroed
    if "Gold Experience" in (role.name for role in ctx.message.author.roles):
        if "Requiem" not in (role.name for role in ctx.message.author.roles):
            return
        embed = discord.Embed(title = "**{}** обнулил **{}**.".format(ctx.message.author.name, member.name), description = "*{} теперь не сможет юзать бота.*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/482429308791554079/unknown.png")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        zeroed = member.id
        
        
@bot.command(pass_context=True) #ОБНУЛ
async def zip(ctx, member : discord.Member):
    global zipped
    global zipped_channel
    if zipped != "":
        await bot.send_message(ctx.message.channel, "Предыдущая застёжка пока активна.")
        return
    if "Sticky Fingers" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** сделал застёжку-молнию в **{}**.".format(ctx.message.author.name, member.name), description = "Теперь пока вы пишите сообщения в новом канале, этот пользователь будет в муте.", color = 0xffff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/473403386599964672/476410583697063936/8ffffd812e623f40.PNG")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        everyone = discord.PermissionOverwrite(read_messages=False)
        mine = discord.PermissionOverwrite(read_messages=True)
        
        zipped = member.id
        
        zipped_channel = await bot.create_channel(ctx.message.server, str(member.name), (ctx.message.server.default_role, everyone), (ctx.message.author, mine))
        await asyncio.sleep(50)
        await bot.delete_channel(zipped_channel)
        zipped = ""
        
@bot.command(pass_context=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def zipper(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    
    
    if "Sticky Fingers" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "ARIARIARI, **{}**.".format(member.name), description = "*ARRIVEDERCI!* ``Мут на 6 секунд``", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b1/SF_multiple_fast_punching.png/revision/latest/scale-to-width-down/604?cb=20150625032040")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(6)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
        
        
@bot.command(pass_context=True) #ЗАПИСЬ
async def record(ctx, member : discord.Member):
    global recording
    global wrec
    global BOT_ID
    if "Moody Blues" in (role.name for role in ctx.message.author.roles):
        if member.id == BOT_ID:
            await bot.send_message(ctx.message.channel, "Нельзя использовать стенд на этом юзере.")
            return
        elif member.id == "274809987837198346":
            await bot.send_message(ctx.message.channel, "Нельзя использовать стенд на этом юзере.")
            return
        elif member.id == "208283620203429888":
            await bot.send_message(ctx.message.channel, "Нельзя использовать стенд на этом юзере.")
            return
        embed = discord.Embed(title = "**{}** теперь записывает **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/29/MoodyBluesAbilityActivation.jpg/revision/latest/scale-to-width-down/497?cb=20170216052600")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        recording = member.id
        wrec = ctx.message.author.id
        await asyncio.sleep(300)
        recording = ""
        wrec = ""
        
@bot.command(pass_context=True) #ЗАПИСЬ
async def stop(ctx):
    global recording
    global wrec
    if "Moody Blues" in (role.name for role in ctx.message.author.roles):
        if recording != "":
            embed = discord.Embed(title = "**{}** остановил запись.".format(ctx.message.author.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/8e/Moodybluesfirst.png/revision/latest/scale-to-width-down/275?cb=20161028094156")
            await bot.send_message(ctx.message.channel, embed=embed)
                
            recording = ""
            wrec = ""
        else:
            embed = discord.Embed(title = "Запись **не** включена.".format(ctx.message.author.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/8e/Moodybluesfirst.png/revision/latest/scale-to-width-down/275?cb=20161028094156")
            await bot.send_message(ctx.message.channel, embed=embed)
            
@bot.command(pass_context=True) #МУТ 4-ЁХ
@commands.cooldown(1, 8, commands.BucketType.user)
async def bully(ctx, member : discord.Member, smember : discord.Member, tmember : discord.Member, fmember : discord.Member):

    if "В муте" in (role.name for role in member.roles):
        return
    if "В муте" in (role.name for role in smember.roles):
        return
    if "В муте" in (role.name for role in tmember.roles):
        return
    if "В муте" in (role.name for role in fmember.roles):
        return
    if "Sex Pistols" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** выстрелил в **{}**, **{}**, **{}** и в **{}**.".format(ctx.message.author.name, member.name, smember.name, tmember.name, fmember.name), description = "*Они попали в мут на 5 минут.*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://media.giphy.com/media/fnrQxeyCIb4XRd2cuq/giphy.gif")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        await bot.add_roles(smember, mute_role)
        await bot.add_roles(tmember, mute_role)
        await bot.add_roles(fmember, mute_role)
        
        await asyncio.sleep(300)
        
        muted_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, muted_role)
        await bot.remove_roles(smember, muted_role)
        await bot.remove_roles(tmember, muted_role)
        await bot.remove_roles(fmember, muted_role)
        
@bot.command(pass_context=True) #АЭРО
async def aero(ctx, member : discord.Member, smember : discord.Member):
    global aero
    if aero == 1:
        return
    if "Aerosmith" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "VOLAVOLAVOLA, **{}**, **{}**.".format(member.name, smember.name), description = "*... VOLARE VIA!*".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/be/AerosmithAttackingFormaggio.jpg/revision/latest/scale-to-width-down/300?cb=20161029055929")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        aero = 1
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        await bot.add_roles(smember, mute_role)
        
        await asyncio.sleep(600)
        
        embed = discord.Embed(title = "**{}** и **{}** размучены.".format(member.name, smember.name), description = "*{} снова может юзать бота.*".format(ctx.message.author.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/be/AerosmithAttackingFormaggio.jpg/revision/latest/scale-to-width-down/300?cb=20161029055929")
        await bot.send_message(ctx.message.channel, embed=embed)
        aero = 0
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        await bot.remove_roles(smember, mute_role)
        
@bot.command(pass_context=True) #АЭРО
async def virused(ctx, member : discord.Member):
    global virus
    global virus_S
    if "Purple Haze" in (role.name for role in ctx.message.author.roles):
        if virus != "":
            return
        embed = discord.Embed(title = "**{}** заразил вирусом **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/f/f8/IllusoInfected.jpg/revision/latest?cb=20170405095225")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        virus = member.id
        virus_S = 0
            
        await asyncio.sleep(120)
        
        virus_S = 1
        
        await asyncio.sleep(120)
        
        virus_S = 2
        
        await asyncio.sleep(120)
        
        virus_S = 0
        virus = ""
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True) #СОФТЕНЕД
@commands.cooldown(1, 8, commands.BucketType.user)
async def soft(ctx, member : discord.Member):
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Spice Girl" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "WAAAAANNABEEEEEEEEEE, **{}**!".format(member.name), description = "*{} замучен на 3 секунды, следующая его команда не сработает*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/50/WANABEEEEEEEEEEE.png/revision/latest/scale-to-width-down/310?cb=20150528102651")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        mutess_role = discord.utils.find(lambda r: r.name == 'Смягчён', ctx.message.server.roles)
        await bot.add_roles(member, mutess_role)
        
        await asyncio.sleep(3)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def swordr(ctx, member : discord.Member, smember : discord.Member, tmember : discord.Member):
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Silver Chariot" in (role.name for role in ctx.message.author.roles):
        if "Requiem" in (role.name for role in ctx.message.author.roles):
        
            embed = discord.Embed(title = "HORA HORA HORA, {}, {}, {}!".format(member.name, smember.name, tmember.name), description = "*ХОРА ХОРА ХОРА, {}, {}, {}!*".format(member.name, smember.name, tmember.name), color = 0xffff00)
            embed.set_image(url="https://i.kym-cdn.com/photos/images/original/000/449/361/47b.jpg")
            await bot.send_message(ctx.message.channel, embed=embed)
        
            if "Tower of Gray" in (role.name for role in member.roles):
                if random.randint(0, 1) == 1:
                    embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                    await bot.send_message(ctx.message.channel, embed=embed)
                    return
                
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
            await bot.add_roles(smember, mute_role)
            await bot.add_roles(tmember, mute_role)
        
            await asyncio.sleep(4)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
            await bot.remove_roles(smember, mute_role)
            await bot.remove_roles(tmember, mute_role)
            
@bot.command(pass_context=True)
async def self(ctx, member : discord.Member):
    global mutesec
    global sha_bomb
    global mutesec2
    global act3freeze
    if "Silver Chariot" in (role.name for role in ctx.message.author.roles):
        if "Requiem" in (role.name for role in ctx.message.author.roles):
        
            embed = discord.Embed(title = "**{}** принудил **стенд {}** атаковать своего владельца!".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://i.kym-cdn.com/photos/images/original/000/449/361/47b.jpg")
            await bot.send_message(ctx.message.channel, embed=embed)
        
            if "Tower of Gray" in (role.name for role in member.roles):
                if random.randint(0, 1) == 1:
                    embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                    await bot.send_message(ctx.message.channel, embed=embed)
                    return
                    
            if "The World" in (role.name for role in member.roles):
                embed = discord.Embed(title = "MUDA MUDA MUDA, {}!".format(member.name), description = "*«БЕСПОЛЕЗНО БЕСПОЛЕЗНО БЕСПОЛЕЗНО, {}!»*".format(member.name), color = 0xffff00)
                embed.set_image(url="https://media1.tenor.com/images/f793f8e06058e79b2efe7e30ad239640/tenor.gif?itemid=5455737")
                await bot.send_message(ctx.message.channel, embed=embed)
                
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(7)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
            if "Star Platinum" in (role.name for role in member.roles):
        
                embed = discord.Embed(title = "ORA ORA ORA, {}!".format(member.name), description = "*«ОРА ОРА ОРА, {}!»*".format(member.name), color = 0xffff00)
                embed.set_image(url="https://i.kym-cdn.com/photos/images/original/001/196/436/c92.gif")
                await bot.send_message(ctx.message.channel, embed=embed)

                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(5)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
            if "Hierophant Green" in (role.name for role in member.roles):
        
                embed = discord.Embed(title = "ИЗУМРУДНЫЙ ВСПЛЕСК!", description = "*{} атаковали.*".format(member.name), color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/powerlisting/images/8/81/Hierophant_Green%27s_Emerald_Splash%21%21%21%21_JoJo.gif/revision/latest?cb=20180412154853")
                await bot.send_message(ctx.message.channel, embed=embed)
                
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(4)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
            if "Ebony Devil" in (role.name for role in member.roles):
        
                embed = discord.Embed(title = "Дьявол **{}** атаковал **{}**.".format(member.name, member.name), description = "*{} атаковали.*".format(member.name), color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/76/EbonyDevilAttacking.jpg/revision/latest/scale-to-width-down/640?cb=20140523223228")
                await bot.send_message(ctx.message.channel, embed=embed)
                
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(mutesec)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
            if "Killer Queen" in (role.name for role in member.roles):
        
                embed = discord.Embed(title = "{} использовал на {} вторую бомбу.".format(member.name, member.name), description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/53/SHA_initial_appearance.png/revision/latest/scale-to-width-down/640?cb=20160826191428")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                sha_bomb = member.id
                
            if "Yellow Temperance" in (role.name for role in member.roles):
                embed = discord.Embed(title = "{} атаковал слизью {}.".format(member.name, member.name), description = "*{} атаковали. Он попал в мут на {} секунд.*".format(member.name, mutesec2), color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/77/Rubber_Soul_Anime.png/revision/latest?cb=20140530194339")
                await bot.send_message(ctx.message.channel, embed=embed)
                
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(mutesec2)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
            if "Horus" in (role.name for role in member.roles):
        
                embed = discord.Embed(title = "**{}** атаковал **{}** глыбой льда.".format(member.name, member.name), description = "*{} атаковали. Он в муте на 3 секунды.*".format(member.name), color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/5a/Horus_kills_a_man.png/revision/latest/scale-to-width-down/640?cb=20150411065137")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(3)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
            if "Crazy Diamond" in (role.name for role in member.roles):
        
                embed = discord.Embed(title = "DORARARA, {}!".format(member.name), description = "*«ДОРАРАРА, {}!»*".format(member.name), color = 0xffff00)
                embed.set_image(url="https://i.imgur.com/6xdbtkW.gif?noredirect")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(5)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
            if "Echoes ACT3" in (role.name for role in member.roles):
        
                embed = discord.Embed(title = "**S-H-I-T**.", description = "*``«Г-О-В-Н-О»``* **{} был заморожен.**".format(member.name), color = 0xffff00)
                embed.set_image(url=    "https://vignette.wikia.nocookie.net/jjba/images/6/67/ACT3_3_freeze.png/revision/latest/scale-to-width-down/640?cb=20160904163229")
                await bot.send_message(ctx.message.channel, embed=embed)

                act2 = 0
                act3freeze = member.id
                
            if "Pearl Jam" in (role.name for role in member.roles):
                embed = discord.Embed(title = "**{}** накормил **{}** *итким блюдом*.".format(member.name, member.name), description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/39/PearlJamOkuyasuGuts.jpg/revision/latest/scale-to-width-down/640?cb=20170204192747")
                await bot.send_message(ctx.message.channel, embed=embed)

                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
                await asyncio.sleep(300)
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
        
                zdorovii = discord.utils.find(lambda r: r.name == 'Здоровый', ctx.message.server.roles)
                await bot.add_roles(member, zdorovii)
        
                embed = discord.Embed(title = "**{}** полностью здоров.".format(member.name), description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/74/Okuyasu_feeling_refreshed.png/revision/latest/scale-to-width-down/640?cb=20160603202410")
                await bot.send_message(ctx.message.channel, embed=embed)
            if "Ratt" in (role.name for role in member.roles):
        
                embed = discord.Embed(title = "**{}** выстрелил ядом в **{}**.".format(member.name, member.name), description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b7/Ratt%27s_scope.png/revision/latest/scale-to-width-down/640?cb=20160715205610")
                await bot.send_message(ctx.message.channel, embed=embed)

                poisoned = member.id
                messagoison = ""
            if "Stray Cat" in (role.name for role in member.roles):
        
                embed = discord.Embed(title = "**{}** выстрелил воздухом в **{}**".format(member.name, member.name), description = "*«Мяу»*".format(member.name), color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e0/Stray_Cat_Shooting_Air.gif")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(6)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
            if "King Crimson" in (role.name for role in member.roles):
        
                embed = discord.Embed(title = "{} разорвал {}".format(member.name, member.name), description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/db/King_Crimson_Bruno_Buccellati.jpg/revision/latest/scale-to-width-down/312?cb=20150523144936")
                await bot.send_message(ctx.message.channel, embed=embed)
                
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(6)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
@bot.command(pass_context=True) #ЗОЛУШКА
async def timeerase(ctx):
    if "King Crimson" in (role.name for role in ctx.message.author.roles):
        global user_bomb
        user_bomb = ""

        global sha_bomb
        sha_bomb = ""

        global ripple_id
        ripple_id = ""

        global ignite_id
        ignite_id = ""

        global puppet
        puppet = ""

        global jawed
        jawed = ""

        global top_speed
        top_speed = 0

        global barn
        barn = ""

        global barned
        barned = 0

        global attackship
        attackship = 0

        global mutesec
        mutesec = 1

        global mutesec2
        mutesec2 = 2

        global skilling
        skilling = 0

        global hanged
        hanged = ""

        global canshoot
        canshoot = 0

        global shooting
        shooting = ""

        global emp_w
        emp_w = ""

        global parazit
        parazit = ""

        global paraziting
        paraziting = ""

        global word_need
        word_need = ""

        global justly
        justly = ""

        global loved
        loved = ""

        global loving
        loving = ""

        global charges
        charges = 0

        global posses
        posses = ""

        global target
        target = ""

        global brat
        brat = ""

        global oblik
        oblik = ""

        global tooksword
        tooksword = ""

        global shocked
        shocked = ""

        global baby
        baby = ""

        global playing_with
        playing_with = ""

        global randomnum
        randomnum = 0

        global randomnum2
        randomnum2 = 0

        global ready
        ready = 0

        global ready2
        ready2 = 0

        global darbi
        darbi = ""

        global froze
        froze = ""

        global playcar
        playcar = ""

        global darbis
        darbos = ""

        global car1pos
        car1pos = 0

        global car2pos
        car2pos = 0

        global carready
        carready = 0

        global carready2
        carready2 = 0

        global game_started
        game_started = 0

        global race
        race = ""

        global race2
        race2 = ""

        global voided
        voided = ""

        global evolving
        evolving = 0

        global sound
        sound = ""

        global soundword
        soundword = ""

        global act2
        act2 = 0

        global act3freeze
        act3freeze = ""

        global booked
        booked = ""

        global bookab
        bookab = 0

        global watered
        watered = ""

        global badtarget
        badtarget = ""

        global voicecharge
        voicecharge = 0

        global locked
        locked = ""

        global mon
        mon = 0

        global maniq
        maniq = ""

        global mimi
        mimi = ""

        global lovedel
        lovedel = ""

        global achtung
        achtung = 0

        global poisoned
        poisoned = 0

        global messagoison
        messagoison = ""

        global harvatiya
        harvatiya = 0

        global changenickcan
        changenickcan = ""

        global bites_dust
        bites_dust = ""

        global rps
        rps = ""

        global player1choose
        player1choose = ""

        global player2choose
        player2choose = ""

        global readyplay
        readyplay = ""

        global choosed
        choosed = ""

        global readyplayer1
        readyplayer1 = 0

        global readyplayer2
        readyplayer2 = 0

        global randomrock
        randomrock = ""

        global randompaper
        randompaper = ""

        global randomscissors
        randomscissors = ""

        global randomrock2
        randomrock2 = ""

        global randompaper2
        randompaper2 = ""

        global randomscissors2
        randomscissors = ""

        global reflecting
        reflecting = ""

        global wutface
        wutface = ""

        global degrod
        degrod = ""

        global highw
        highw = ""

        global zeroed
        zeroed = ""

        global zipped
        zipped = ""

        global recording
        recording = ""

        global wrec
        wrec = ""

        global aero
        aero = 0

        global virus
        virus = ""

        global virus_S
        virus_S = 0

        global littled
        littled = ""

        global hidden
        hidden = ""

        global hooked
        hooked = 0

        global aging
        aging = ""

        global muting
        muting = 0

        global iceduser
        iceduser = ""

        global ici
        ici = 0

        global user_lie
        user_lie = ""

        global lie_word
        lie_word = ""

        global lie_to
        lie_to = ""

        global invisiblity
        invisiblity = ""

        global molded
        molded = ""

        global molding
        molding = ""

        global stoned
        stoned = ""

        global nitka
        nitka = ""

        global ghost
        ghost = ""

        global invade
        invade = ""

        global invading
        invading = ""

        global weather
        weather = 0

        global dcharge
        dcharge = 1

        global disc
        disc = ""

        global disced
        disced = ""

        global discmute
        discmute = 0

        global gravitied
        gravitied = 0

        global evolvedd
        evolvedd = 0

        global spinning
        spinning = 0

        global spinin
        spinin = ""

        global spini
        spini = 0

        global spinner
        spinner = ""

        global spinenergy
        spinenergy = 0

        global tickettoride
        tickettoride = 0

        global stealed
        stealed = 5

        global degrodi
        degrodi = 0

        global newlife
        newlife = ""

        global degradations
        degradations = 0

        global degradations2
        degradations2 = 0
        
        global gayporn
        gayporn = ""
        
        global sha_bombe
        sha_bombe = ""

        global sha_bombe2
        sha_bombe2 = ""

        global sha_bombe3
        sha_bombe3 = ""

        global sha_bombe4
        sha_bombe4 = ""
        
        
        global muted_all_users
        
        if muted_all_users == 2:
            return
            
        embed = discord.Embed(title = "**{}** стёр время.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/00/HalfASecond.png/revision/latest/scale-to-width-down/469?cb=20170201094855")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        muted_all_users = 2
        
        mgs = []
        async for x in bot.logs_from(ctx.message.channel, limit = 5):
            mgs.append(x)
        await bot.delete_messages(mgs)
        
        
        for x in mgs:
            await bot.send_message(ctx.message.author, "<@{}> : ~~{}~~".format(x.author.id, x.content))
            
        await asyncio.sleep(3)
        
        mgs = []
        async for x in bot.logs_from(ctx.message.channel, limit = 5):
            mgs.append(x)
        await bot.delete_messages(mgs)
        
        
        for x in mgs:
            await bot.send_message(ctx.message.author, "<@{}> : ~~{}~~".format(x.author.id, x.content))
            
        await asyncio.sleep(3)
        
        mgs = []
        async for x in bot.logs_from(ctx.message.channel, limit = 5):
            mgs.append(x)
        await bot.delete_messages(mgs)
        
        
        for x in mgs:
            await bot.send_message(ctx.message.author, "<@{}> : ~~{}~~".format(x.author.id, x.content))
            
        await asyncio.sleep(2)
        
        muted_all_users = 0
        await bot.send_message(ctx.message.author, "Время стёрто.")
      
@bot.command(pass_context=True)
async def punch(ctx, member : discord.Member):
    global tickettoride
    global muted_all_users
    if "King Crimson" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "{} разорвал {}".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/db/King_Crimson_Bruno_Buccellati.jpg/revision/latest/scale-to-width-down/312?cb=20150523144936")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        if muted_all_users == 2:
            await asyncio.sleep(10)
        else:
            await asyncio.sleep(6)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
    if "Dirty Deeds Done Dirt Cheap" in (role.name for role in ctx.message.author.roles):
        if tickettoride == 0:
            embed = discord.Embed(title = "{} атаковал {}".format(ctx.message.author.name, member.name), description = "Мут на 5 секунд.", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/4d/D4c_sbr69.png/revision/latest/scale-to-width-down/350?cb=20160323142852")
            await bot.send_message(ctx.message.channel, embed=embed)
                
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
        
            await asyncio.sleep(5)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True)
@commands.cooldown(1, 20, commands.BucketType.user)
async def dshadow(ctx, member : discord.Member):
    global currentHour
    currentHour = datetime.datetime.now().hour
    curHour = int(currentHour)
    
    print (str(currentHour))
    if "Black Sabbath" in (role.name for role in ctx.message.author.roles):
        if currentHour >= 16:
            return
        embed = discord.Embed(title = "**{}** замутил на 10 секунд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/3c/BS_Shadow_hiding.png/revision/latest/scale-to-width-down/363?cb=20150626050513")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(10)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True)
@commands.cooldown(1, 15, commands.BucketType.user)
async def vshadow(ctx, member : discord.Member, smember : discord.Member):
    global currentHour
    currentHour = datetime.datetime.now().hour
    curHour = int(currentHour)
    
    print (str(currentHour))
    if "Black Sabbath" in (role.name for role in ctx.message.author.roles):
        if currentHour < 16:
            return
        embed = discord.Embed(title = "**{}** замутил **{}, {}** на 5 секунд.".format(ctx.message.author.name, member.name, smember.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/3/3c/BS_Shadow_hiding.png/revision/latest/scale-to-width-down/363?cb=20150626050513")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        await bot.add_roles(smember, mute_role)
        
        await asyncio.sleep(5)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        await bot.remove_roles(smember, mute_role)
        
@bot.command(pass_context=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def deflate(ctx, member : discord.Member):
    if "Soft Machine" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "{} сделал лёгким {}".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b2/Naranciadeflated.png/revision/latest/scale-to-width-down/309?cb=20161028101722")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        mute_role = discord.utils.find(lambda r: r.name == 'Лёгкий', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
@bot.command(pass_context=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def llock(ctx, member : discord.Member):
    if "Kraft Work" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** убрал возможность писать сообщения **{}** в этом канале.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/81/Jojopv5-00_00_18--20130612-174653-0-.JPG/revision/latest/scale-to-width-down/640?cb=20130622133903")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        await bot.edit_channel_permissions(ctx.message.channel, member, overwrite)
        
        await asyncio.sleep(300)

        await bot.delete_channel_permissions(ctx.message.channel, member)
        
@bot.command(pass_context=True)
async def shrink(ctx, member : discord.Member):
    global littled
    if "Little Feet" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "{} уменьшил {}".format(ctx.message.author.name, member.name), description = "*Теперь {} не может использовать команды бота, а его сообщения уменьшены.*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/22/LittleFeet.png/revision/latest?cb=20161029061702")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        littled = member.id
        
        
@bot.command(pass_context=True)
async def createmirror(ctx, member : discord.Member):
    global meme
    global zerkal_kanal
    if meme != "":
        return
    if "Man in the Mirror" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** забрал **{}** в свой *зазеркаленный мир.*".format(ctx.message.author.name, member.name), description = "".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/43/Man_In_The_Mirror.png/revision/latest/scale-to-width-down/209?cb=20150521171059")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        meme = member.id
        
        everyone = discord.PermissionOverwrite(read_messages=False)
        mine = discord.PermissionOverwrite(read_messages=True)
        
        zerkal_kanal = await bot.create_channel(ctx.message.server, "зазеркалье", (ctx.message.server.default_role, everyone), (ctx.message.author, mine), (member, mine))
        await asyncio.sleep(60)
        await bot.delete_channel(zerkal_kanal)
        
@bot.command(pass_context=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def mirattack(ctx, member : discord.Member):
    global meme
    global zerkal_kanal
    if ctx.message.channel != zerkal_kanal:
        return
    if member.id != meme:
        return
    if "Man in the Mirror" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** атаковал **{}** в зеркале.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/MitMPunch.PNG/revision/latest/scale-to-width-down/429?cb=20170329044714")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(5)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True)
async def hide(ctx, member : discord.Member):
    global hidden
    if hidden != "":
        return
    if "В муте" in (role.name for role in member.roles):
        embed = discord.Embed(title = "{} не может спрятать {}.".format(ctx.message.author.name, member.name), description = "*Он уже в муте.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/49/MrPresidentRoom.png/revision/latest/scale-to-width-down/488?cb=20170413051142")
        await bot.send_message(ctx.message.channel, embed=embed)
        return
    if "Mr.President" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "{} спрятал {}".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/49/MrPresidentRoom.png/revision/latest/scale-to-width-down/488?cb=20170413051142")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        hidden = member.id
        await asyncio.sleep(60)
        hidden = ""
        
@bot.command(pass_context=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def hook(ctx, member : discord.Member):
    global hooked
    if hooked == 1:
        return
    if "Beach Boy" in (role.name for role in ctx.message.author.roles):
        if member.voice_channel == None:
            return
        embed = discord.Embed(title = "**{}** атаковал **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/c1/BBPhase.jpg/revision/latest/scale-to-width-down/640?cb=20170413052637")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        hooked = 1
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(600)
        
        hooked = 0
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True)
async def age(ctx, member : discord.Member):
    global aging
    if "В муте" not in (role.name for role in member.roles):
        return
    if "The Grateful Dead" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** вырастил **{}**.".format(ctx.message.author.name, member.name), description = "*{} дал возможность {} написать сообщение или воспользоваться командой в муте.*".format(ctx.message.author.name, member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/c0/GFA-TGD.jpg/revision/latest/scale-to-width-down/640?cb=20170413141444")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        aging = member.id
        
@bot.command(pass_context=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def homu(ctx, member : discord.Member):
    global muting
    if "В муте" in (role.name for role in member.roles):
        return
    if "Baby Face" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "**{}** замутил **{}** на **{}** секунд.".format(ctx.message.author.name, member.name, muting), description = "*{} атаковали.*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/4e/BF_back_head.png/revision/latest/scale-to-width-down/511?cb=20150627140947")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        mutting = muting
        muting = 0
        
        await asyncio.sleep(mutting)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def temp(ctx, member : discord.Member):
    global iceduser
    if member.id != iceduser:
        return
    if "White Album" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** атаковал **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/7b/WAGWFirst.jpg/revision/latest/scale-to-width-down/390?cb=20170430040628")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(4)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def liq(ctx, member : discord.Member):
    if "В муте" in (role.name for role in member.roles):
        return
    if "Clash" in (role.name for role in ctx.message.author.roles):
        if member.voice_channel != None:
            embed = discord.Embed(title = "**{}** атаковал **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/ca/ClashNaranciaTears.jpg/revision/latest/scale-to-width-down/391?cb=20170515143253")
            await bot.send_message(ctx.message.channel, embed=embed)
                
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
        
            await asyncio.sleep(5)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
        else:
            embed = discord.Embed(title = "**{}** атаковал **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/c/ca/ClashNaranciaTears.jpg/revision/latest/scale-to-width-down/391?cb=20170515143253")
            await bot.send_message(ctx.message.channel, embed=embed)
                
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
        
            await asyncio.sleep(3)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
            
            
@bot.command(pass_context=True)
async def lie(ctx, member : discord.Member):
    global user_lie
    global lie_word
    global lie_to
    if "Talking Head" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** переместил свой стенд в **{}**.".format(ctx.message.author.name, member.name), description = "*Все слова сбросились.*".format(ctx.message.author.name, member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/8f/TalkingHeadFirst.jpg/revision/latest/scale-to-width-down/640?cb=20170514222908")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        user_lie = member.id
        lie_word = ""
        lie_to = ""
        
@bot.command(pass_context=True)
async def lying(ctx, wordo : str, *worde):
    global user_lie
    global lie_word
    global lie_to
    if user_lie == "":
        await bot.send_message(ctx.message.channel, "Для начала переместите свой стенд в кого-то, <@{}>.".format(ctx.message.author.id))
        return
    if "Talking Head" in (role.name for role in ctx.message.author.roles):
        
        lie_word = wordo
        lie_to = ' '.join(worde)
        
        embed = discord.Embed(title = "**{}** поменял слова.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/9/94/TalkingHeadTongue1.jpg/revision/latest/scale-to-width-down/446?cb=20170515143851")
        await bot.send_message(ctx.message.channel, embed=embed)
        
@bot.command(pass_context=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def enabsorb(ctx, member : discord.Member):
    global charges
    global voicecharge
    if "В муте" in (role.name for role in member.roles):
        return
    if "Notorious B.I.G" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** атаковал **{}**.".format(ctx.message.author.name, member.name), description = "*5-ти секундный мут.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/81/Notoriousbigpre.jpg/revision/latest/scale-to-width-down/192?cb=20150523185219")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        if "Sun" in (role.name for role in member.roles):
            charges = 0
        if "Red Hot Chili Pepper" in (role.name for role in member.roles):
            voicecharge = 0
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(5)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True)
async def invisible(ctx, member : discord.Member):
    global invisiblity
    if "Metallica" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** сделал невидимым **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b7/Metallicainvisiblity.jpg/revision/latest/scale-to-width-down/297?cb=20150607155343")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        invisiblity = member.id

@bot.command(pass_context=True)
async def vis(ctx, member : discord.Member):
    global invisiblity
    if "Metallica" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** убрал невидимость.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b7/Metallicainvisiblity.jpg/revision/latest/scale-to-width-down/297?cb=20150607155343")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        invisiblity = ""
        
@bot.command(pass_context=True)
async def mold(ctx, member : discord.Member):
    global molded
    if "Green Day" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** теперь плесневеет.".format(member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/bc/Green_Day_with_Secco.png/revision/latest/scale-to-width-down/640?cb=20161231083827")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        molded = member.id
        
@bot.command(pass_context=True)
async def unmold(ctx, member : discord.Member):
    global molded
    if "Green Day" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "{} убрал плесень.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/bc/Green_Day_with_Secco.png/revision/latest/scale-to-width-down/640?cb=20161231083827")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        molded = ""
        
@bot.command(pass_context=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def ground(ctx, member : discord.Member, smember : discord.Member):
    if "Oasis" in (role.name for role in ctx.message.author.roles):
        if member.voice_channel == None and smember.voice_channel == None:
            embed = discord.Embed(title = "**{}** атаковал **{}**, **{}**.".format(ctx.message.author.name, member.name, smember.name), description = "*Мут на 6 секунд.*", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/60/SeccoPavementSpit.jpg/revision/latest/scale-to-width-down/195?cb=20170612180238")
            await bot.send_message(ctx.message.channel, embed=embed)
                
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
            await bot.add_roles(smember, mute_role)
        
            await asyncio.sleep(6)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
            await bot.remove_roles(smember, mute_role)
        else:
            embed = discord.Embed(title = "Можно атаковать только людей не в войсе, **{}**.".format(ctx.message.author.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/e6/SeccoEatsMud.PNG/revision/latest/scale-to-width-down/523?cb=20170612180136")
            await bot.send_message(ctx.message.channel, embed=embed)
            
@bot.command(pass_context=True)
async def stone(ctx, member : discord.Member):
    global stoned
    
    if member.id == stoned:
        return
    if "Rolling Stones" in (role.name for role in ctx.message.author.roles):
        if "В муте" not in (role.name for role in member.roles):
            await bot.send_message(ctx.message.channel, "Можно использовать только на людей в муте.")
            return
        embed = discord.Embed(title = "**{}** дал вечный мут **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/2/2b/Rolling_Stones%27s_shape_turn_into_Bucciarati.png/revision/latest/scale-to-width-down/460?cb=20161123103659")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if stoned != "":
            stone_user = discord.Server.get_member(ctx.message.server, user_id=stoned)
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(stone_user, mute_role)
        stoned = member.id
        
@bot.command(pass_context=True)
async def unstone(ctx):
    global stoned
    
    if stoned == "":
        return
    if "Rolling Stones" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** убрал вечный мут.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/86/Rolling_Stones.png/revision/latest/scale-to-width-down/350?cb=20140822162552")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        stone_user = discord.Server.get_member(ctx.message.server, user_id=stoned)
        if "В муте" in (role.name for role in stone_user.roles):
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(stone_user, mute_role)
        stoned = ""
        
@bot.command(pass_context=True)
async def stringed(ctx, member : discord.Member):
    global nitka
    if "Stone Free" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** превратил **{}** в нить.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        nitka = member.id
        
@bot.command(pass_context=True)
async def unstring(ctx):
    global nitka
    if "Stone Free" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** убрал превращение.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/ea/SO_Chapter_45_Cover_B.jpg/revision/latest/scale-to-width-down/624?cb=20140817215233")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        nitka = "" 

@bot.command(pass_context=True)
async def dub(ctx, member : discord.Member):
    if "Kiss" in (role.name for role in ctx.message.author.roles):
        if "Hierophant Green" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Hierophant Green", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "The Fool" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "The Fool", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Tower of Gray" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Tower of Gray", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Dark Blue Moon" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Dark Blue Moon", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Emperor" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Emperor", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Wheel of Fortune" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Wheel of Fortune", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Sun" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Sun", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Death 13" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Death 13", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Judgement" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Judgement", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Geb" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Geb", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Bastet" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Bastet", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Sethan" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Sethan", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Horus" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Horus", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Aqua Necklace" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Aqua Necklace", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Ratt" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Ratt", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Love Deluxe" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Love Deluxe", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Pearl Jam" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Pearl Jam", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Stray Cat" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Stray Cat", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Cheap Trick" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Cheap Trick", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Moody Blues" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Moody Blues", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Mr.President" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Mr.President", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Beach Boy" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Beach Boy", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Clash" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Clash", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        elif "Talking Head" in (role.name for role in member.roles):
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/d/d6/SO_Chapter_9.jpg/revision/latest/scale-to-width-down/312?cb=20140817213026")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            a_role = discord.utils.find(lambda r: r.name == "Kiss", ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, a_role)
            
            b_role = discord.utils.find(lambda r: r.name == "Talking Head", ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, b_role)
        else:
            await bot.send_message(ctx.message.channel, "Нельзя дублировать этот стенд, **{}.**".format(ctx.message.author.name))     


@bot.command(pass_context=True)
async def ghost(ctx, member : discord.Member):
    global ghost
    if "Burning Down the House" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "{} превратил {} в призрака.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/61/BDtHP.png/revision/latest/scale-to-width-down/350?cb=20150607141943")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        ghost = member.id
        
@bot.command(pass_context=True)
async def unghost(ctx, member : discord.Member):
    global ghost
    if member.id != ghost:
        return
    if "Burning Down the House" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "{} снял с {} превращение в призрака.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/6/61/BDtHP.png/revision/latest/scale-to-width-down/350?cb=20150607141943")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        ghost = ""
        
@bot.command(pass_context=True)
async def invasion(ctx, member : discord.Member):
    global invade
    global invading
    global BOT_ID
    if "Foo Fighters" in (role.name for role in ctx.message.author.roles):
        if member.id == BOT_ID:
            await bot.send_message(ctx.message.channel, "Нельзя использовать этот стенд на этом пользователе.")
            return
        if member.id == "274809987837198346":
            await bot.send_message(ctx.message.channel, "Нельзя использовать этот стенд на этом пользователе.")
            return
        if member.id == "208283620203429888":
            await bot.send_message(ctx.message.channel, "Нельзя использовать этот стенд на этом пользователе.")
            return
        embed = discord.Embed(title = "{} читает {}.".format(ctx.message.author.name, member.name), description = "*Теперь его удалённые сообщения пересылаются в ЛС.*", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/a3/Foofighterstwinface.jpg/revision/latest/scale-to-width-down/640?cb=20170221224002")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        invade = member.id
        invading = ctx.message.author.id
        
@bot.command(pass_context=True)
async def plankton(ctx, member : discord.Member):
    if "В муте" in (role.name for role in member.roles):
        return
    if "Foo Fighters" in (role.name for role in ctx.message.author.roles):
        randommut = random.randint(3, 7)
        embed = discord.Embed(title = "**{}** атаковал **{}**.".format(ctx.message.author.name, member.name), description = "*Мут на {} секунд.*".format(randommut), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/53/Ffgun.jpg/revision/latest/scale-to-width-down/352?cb=20170221230233")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(randommut)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True)
async def wset(ctx, u : str):
    global weather
    if "Weather Report" in (role.name for role in ctx.message.author.roles):
        if u == "1":
            wsign = ":sunny:"
            weather = 0
        elif u == "2":
            wsign = ":cloud_rain:"
            weather = 1
        elif u == "3":
            wsign = ":cloud_lightning:"
            weather = 2
        elif u == "4":
            wsign = ":cloud_snow:"
            weather = 3
        embed = discord.Embed(title = "**{}** поменял погоду.".format(ctx.message.author.name), description = "*Теперь идёт {}*".format(wsign), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/42/WeatherRP.png/revision/latest/scale-to-width-down/350?cb=20150607144211")
        await bot.send_message(ctx.message.channel, embed=embed)
        
@bot.command(pass_context=True)
async def wlist(ctx):
    if "Weather Report" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**Список погодных условий.**", description = "", color = 0xffff00)
        
        embed.add_field(name="~wset 1", value="Поставить солнечную погоду. :sunny: Отключить все эффекты этого стенда.", inline=True)
        embed.add_field(name="~wset 2", value="Поставить дождь. :cloud_rain: Растекаются сообщения всех людей.", inline=True)
        embed.add_field(name="~wset 3", value="Поставить грозу. :cloud_lightning: Каждое сообщение - мут на 6 секунд.", inline=True)
        embed.add_field(name="~wset 4", value="Поставить снег. :cloud_snow: Спам в ЛС, когда человек пишет сообщение.", inline=True)
        
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/4/42/WeatherRP.png/revision/latest/scale-to-width-down/350?cb=20150607144211")
        await bot.send_message(ctx.message.author, embed=embed)
        
@bot.command(pass_context=True)
async def diver(ctx, member : discord.Member):
    global dcharge
    if "В муте" in (role.name for role in member.roles):
        return
    if "Diver Down" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** атаковал **{}**.".format(ctx.message.author.name, member.name), description = "*Мут на {} секунды.*".format(dcharge), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/71/Anasui.png/revision/latest/scale-to-width-down/640?cb=20131008120914")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(dcharge)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True)
async def extract(ctx, member : discord.Member):
    global disc
    global discmute
    global disced
    global BOT_ID
    if disc != "":
        await bot.send_message(ctx.message.channel, "Вы уже извлекли диск. Прежде чем извлекать новый, загрузите в кого-нибудь предыдущий.")
        return
    if member.id == BOT_ID:
        await bot.send_message(ctx.message.channel, "Нельзя использовать этот стенд на <@{}>.".format(member.id))
        return
    if "Whitesnake" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "{} извлёк диск из {}.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/51/WhiteSnakeAbility.png/revision/latest/scale-to-width-down/405?cb=20150509183917")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        disc = member.name
        disced = member.id
        if "В муте" in (role.name for role in member.roles):
            discmute = 1
        else:
            discmute = 0
            
        await bot.send_message(ctx.message.author, "Вы **извлекли диск** из <@{}>.".format(member.id))
        if discmute == 1:
            await bot.send_message(ctx.message.author, "**Диск:**\nНазвание диска: **{}**\nНомер диска: **{}**\nВ муте: **да**".format(disc, disced))
        else:
            await bot.send_message(ctx.message.author, "**Диск:**\nНазвание диска: **{}**\nНомер диска: **{}**\nВ муте: **нет**".format(disc, disced))
            
@bot.command(pass_context=True)
async def insert(ctx, member : discord.Member):
    global disc
    global discmute
    global disced
    global BOT_ID
    if disc == "":
        await bot.send_message(ctx.message.channel, "Вы ещё не извлекли диск.")
        return
    if member.id == BOT_ID:
        await bot.send_message(ctx.message.channel, "Нельзя использовать этот стенд на <@{}>.".format(member.id))
        return
    if "Whitesnake" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "{} импортировал диск в {}.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/51/WhiteSnakeAbility.png/revision/latest/scale-to-width-down/405?cb=20150509183917")
        await bot.send_message(ctx.message.channel, embed=embed)
                
        await bot.change_nickname(member, disc)
        disced = member.id
        if discmute == 1:
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
        else:
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
            
        await bot.send_message(ctx.message.author, "Вы **импортировали** диск в <@{}>.".format(member.id))
        
        if discmute == 1:
            await bot.send_message(ctx.message.author, "**Диск:**\nНазвание диска: **{}**\nНомер диска: **{}**\nВ муте: **да**".format(disc, disced))
        else:
            await bot.send_message(ctx.message.author, "**Диск:**\nНазвание диска: **{}**\nНомер диска: **{}**\nВ муте: **нет**".format(disc, disced))
            
        disc = ""
        disced = ""
        discmute = 0
            
@bot.command(pass_context=True)
async def gravity(ctx):
    global gravitied
    if "C-Moon" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** поменял гравитацию.".format(ctx.message.author.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/7a/Fd145b68c03cab537f5bc3c157696856.jpg/revision/latest/scale-to-width-down/304?cb=20141026045008")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        gravitied += 1
        if gravitied >= 2:
            gravitied = 0
            
@bot.command(pass_context=True)
async def aceltime(ctx):
    global harvatiya
    global mon
    global muted_all_users
    global star_stop
    global oi

    if "Made in Heaven" in (role.name for role in ctx.message.author.roles):
        if random.randint(0, 3) == 1:
            if oi == "":
                embed = discord.Embed(title = "**{}** ускорил время.".format(ctx.message.author.name), description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/9/92/StHEffects.jpg/revision/latest/scale-to-width-down/300?cb=20140924111722")
                await bot.send_message(ctx.message.channel, embed=embed)
            
                mgs = []
                async for x in bot.logs_from(ctx.message.channel, limit = 99):
                    mgs.append(x)
                await bot.delete_messages(mgs)
            
                everyone = discord.PermissionOverwrite(read_messages=True)
                mine = discord.PermissionOverwrite(manage_messages=True, manage_channels=True)
            
                if oi != None or oi != "":
                    oi = await bot.create_channel(ctx.message.server, "{}".format(ctx.message.channel.name), (ctx.message.server.default_role, everyone), (ctx.message.author, mine))

                    await bot.send_message(ctx.message.author, "Вы создали новую вселенную. У вас есть полное управление ей. Команды в ней:\n``~hmute - замутить ВСЕХ на 4 секунды``\n``~hattack - замутить на 7 секунд``\n``~hone - заспамить эвриванами``")
            
                    await asyncio.sleep(400)
            
                    await bot.send_message(ctx.message.author, "Вселенная уничтожена.")
                    await bot.delete_channel(oi)
                    oi = ""
        else:
            embed = discord.Embed(title = "**{}** ускорил время.".format(ctx.message.author.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/9/92/StHEffects.jpg/revision/latest/scale-to-width-down/300?cb=20140924111722")
            await bot.send_message(ctx.message.channel, embed=embed)
        
            muted_all_users = 1
            star_stop = 4
        
            await asyncio.sleep(3)
            
            star_stop = 0
            muted_all_users = 0
        
@bot.command(pass_context=True)
async def hmute(ctx):
    global muted_all_users
    global star_stop
    global oi
    if "Made in Heaven" in (role.name for role in ctx.message.author.roles):
        if ctx.message.channel == oi:
            await bot.send_message(ctx.message.channel, "**{}** замутил всех на 4 секунды.".format(ctx.message.author.name))
            muted_all_users = 1
            star_stop = 0
            await asyncio.sleep(4)
            muted_all_users = 0
            star_stop = 0
            
@bot.command(pass_context=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def hattack(ctx, member : discord.Member):
    global oi
    if "В муте" in (role.name for role in member.roles):
        return
    if "Made in Heaven" in (role.name for role in ctx.message.author.roles):
        if ctx.message.channel == oi:
            await bot.send_message(ctx.message.channel, "**{}** замутил **{}** на 7 секунд.".format(ctx.message.author.name, member.name))

            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)

            await asyncio.sleep(7)
            
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
            
@bot.command(pass_context=True)
async def hone(ctx):
    global oi
    if "Made in Heaven" in (role.name for role in ctx.message.author.roles):
        if ctx.message.channel == oi:
            await bot.send_message(ctx.message.channel, "@everyone")
            await bot.send_message(ctx.message.channel, "@everyone")
            await bot.send_message(ctx.message.channel, "@everyone")
            await bot.send_message(ctx.message.channel, "@everyone")
            await bot.send_message(ctx.message.channel, "@everyone")
            await bot.send_message(ctx.message.channel, "@everyone")
            await bot.send_message(ctx.message.channel, "@everyone")
            await bot.send_message(ctx.message.channel, "@everyone")
            await bot.send_message(ctx.message.channel, "@everyone")
            await bot.send_message(ctx.message.channel, "@everyone")
            
@bot.command(pass_context=True)
async def spin(ctx):
    global spinning
    global spinenergy
    if "Tusk ACT1" in (role.name for role in ctx.message.author.roles):
        spinning += 1
        await bot.send_message(ctx.message.channel, "Вы набираете *энергию кручения*: ``{}``.".format(spinning))
        
        
        if spinning >= 230:
            spinning = 0
            
            mute_role = discord.utils.find(lambda r: r.name == 'Tusk ACT2', ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, mute_role)
            
            mute_role = discord.utils.find(lambda r: r.name == 'Tusk ACT1', ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, mute_role)
            await bot.send_message(ctx.message.channel, "**Клык** эволюционировал.")
    if "Tusk ACT2" in (role.name for role in ctx.message.author.roles):
        spinning += 1
        await bot.send_message(ctx.message.channel, "Вы набираете *энергию кручения*: ``{}``.".format(spinning))
        
        
        if spinning >= 350:
            spinning = 0
            
            mute_role = discord.utils.find(lambda r: r.name == 'Tusk ACT3', ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, mute_role)
            
            mute_role = discord.utils.find(lambda r: r.name == 'Tusk ACT2', ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, mute_role)
            await bot.send_message(ctx.message.channel, "**Клык** эволюционировал.")
    if "Tusk ACT3" in (role.name for role in ctx.message.author.roles):
        spinning += 1
        await bot.send_message(ctx.message.channel, "Вы набираете *энергию кручения*: ``{}``.".format(spinning))
        
        
        if spinning >= 430:
            spinning = 0
            
            mute_role = discord.utils.find(lambda r: r.name == 'Tusk ACT4', ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, mute_role)
            
            mute_role = discord.utils.find(lambda r: r.name == 'Tusk ACT3', ctx.message.server.roles)
            await bot.remove_roles(ctx.message.author, mute_role)
            await bot.send_message(ctx.message.channel, "**Клык** эволюционировал.")
    if "Tusk ACT4" in (role.name for role in ctx.message.author.roles):
        spinning += 1
        await bot.send_message(ctx.message.channel, "Вы набираете *энергию кручения*: ``{}``.".format(spinning))
    if "Ball Breaker" in (role.name for role in ctx.message.author.roles):
        spinenergy += 1
        await bot.send_message(ctx.message.channel, "Вы набираете *энергию кручения*: ``{}``.".format(spinenergy))
        
        
@bot.command(pass_context=True)
async def nail(ctx, member : discord.Member):
    global spinning
    global spinin
    global spini
    if spinning == 0:
        return
    if "Tusk ACT1" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** запустил крутящимися ногтями в **{}**.".format(ctx.message.author.name, member.name), description = "Он попал в мут на {} секунд. Теперь ногти вращаются в нём.".format(spinning), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/58/TuskAct1color.png/revision/latest/scale-to-width-down/350?cb=20140813205839")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        spinin = member.id
        spini = 5
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
            
        await asyncio.sleep(spinning)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
        spinin = ""
        spini = 0
        spinning = 0
        
    if "Tusk ACT2" in (role.name for role in ctx.message.author.roles):
        spi = spinning * 2
        embed = discord.Embed(title = "**{}** запустил крутящимися ногтями в **{}**.".format(ctx.message.author.name, member.name), description = "Он попал в мут на {} секунд.".format(spi), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/79/Tuskversion2.jpg/revision/latest/scale-to-width-down/283?cb=20180626170720")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(spi)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
        spi = 0
        spinning = 0
        
@bot.command(pass_context=True)
async def whole(ctx, member : discord.Member):
    global spinning
    global spinner
    if spinning == 0:
        return
    if "Tusk ACT3" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** начал вращаться.".format(member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/a/aa/TuskAct3color.png/revision/latest/scale-to-width-down/350?cb=20140813205954")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        spinner = member.id
        await asyncio.sleep(spinning)
        spinner = ""
        spinning = 0
        
@bot.command(pass_context=True)
async def ginfspin(ctx, member : discord.Member):
    global spinning
    global spinner
    global spinin
    global spini
    if spinning == 0:
        return
    if "Tusk ACT4" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** теперь бесконечно вращается.".format(member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/11/TuskAct4color.png/revision/latest/scale-to-width-down/350?cb=20140813210059")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        spinner = member.id
        spi = spinning * 2
        spinning = 0
            
        await asyncio.sleep(spi)
        
        spinner = ""
        spi = 0
        
@bot.command(pass_context=True)
async def bspin(ctx, member : discord.Member):
    global spinenergy
    if "Ball Breaker" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** теперь вращается.".format(member.name), description = "", color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/5/52/BallBreakercolor.png/revision/latest/scale-to-width-down/255?cb=20140813205719")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        spinenergys = spinenergy
        
        mute_role = discord.utils.find(lambda r: r.name == 'Крутится', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        await asyncio.sleep(spinenergys)
        
        mute_role = discord.utils.find(lambda r: r.name == 'Крутится', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
        spinenergy -= spinenergys
        if spinenergy < 0:
            spinenergy = 0
            
@bot.command(pass_context=True)
async def ticket(ctx):
    global tickettoride
    global takingstand
    if "Dirty Deeds Done Dirt Cheap" in (role.name for role in ctx.message.author.roles):
        if takingstand == 1:
            await bot.send_message(ctx.message.channel, "Использовать эту команду пока нельзя.")
            return
        if tickettoride == 0:
            embed = discord.Embed(title = "**{}** активировал **Ticket to Ride**.".format(ctx.message.author.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/bc/TicketToRidecolor.png/revision/latest/scale-to-width-down/303?cb=20140813210411")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            tickettoride = 1
        else:
            embed = discord.Embed(title = "**{}** деактивировал **Ticket to Ride**.".format(ctx.message.author.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/bc/TicketToRidecolor.png/revision/latest/scale-to-width-down/303?cb=20140813210411")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            tickettoride = 0
            
@bot.command(pass_context=True)
async def hop(ctx, member : discord.Member):
    global tickettoride
    global takingstand
    if "Dirty Deeds Done Dirt Cheap" in (role.name for role in ctx.message.author.roles):
        if takingstand == 1:
            await bot.send_message(ctx.message.channel, "Подождите пока пропадёт предыдущий стенд.")
            return
        if tickettoride == 0:
            embed = discord.Embed(title = "**{}** дублировал стенд **{}**.".format(ctx.message.author.name, member.name), description = "", color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/e/ee/D4Ccolor.png/revision/latest/scale-to-width-down/258?cb=20140813212210")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            if "The World" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "The World", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "The World", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                ab_role = discord.utils.find(lambda r: r.name == "Over Heaven", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, ab_role)
                takingstand = 0
                
            if "Star Platinum" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Star Platinum", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Star Platinum", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                ab_role = discord.utils.find(lambda r: r.name == "Over Heaven", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, ab_role)
                takingstand = 0
                
            if "Hermit Purple" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Hermit Purple", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Hermit Purple", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Magician's Red" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Magician's Red", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Magician's Red", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Hierophant Green" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Hierophant Green", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Hierophant Green", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Silver Chariot" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Silver Chariot", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Silver Chariot", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                ab_role = discord.utils.find(lambda r: r.name == "Requiem", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, ab_role)
                takingstand = 0
                
            if "The Fool" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "The Fool", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "The Fool", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Tower of Gray" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Tower of Gray", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Tower of Gray", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Dark Blue Moon" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Dark Blue Moon", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Dark Blue Moon", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Strength" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Strength", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Strength", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Ebony Devil" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Ebony Devil", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Ebony Devil", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Yellow Temperance" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Yellow Temperance", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Yellow Temperance", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Hanged Man" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Hanged Man", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Hanged Man", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Emperor" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Emperor", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Emperor", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Empress" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Empress", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Empress", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Wheel of Fortune" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Wheel of Fortune", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Wheel of Fortune", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Justice" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Justice", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Justice", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Lovers" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Lovers", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Lovers", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Sun" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Sun", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Sun", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Death 13" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Death 13", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Death 13", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Judgement" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Judgement", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Judgement", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "High Priestess" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "High Priestess", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "High Priestess", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Geb" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Geb", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Geb", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Khnum" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Khnum", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Khnum", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Tohth" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Tohth", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Tohth", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Anubis" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Anubis", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Anubis", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Bastet" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Bastet", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Bastet", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Sethan" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Sethan", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Sethan", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Osiris" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Osiris", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Osiris", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Horus" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Horus", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Horus", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Atum" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Atum", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Atum", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Cream" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Cream", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Cream", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Crazy Diamond" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Crazy Diamond", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Crazy Diamond", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Killer Queen" in (role.name for role in member.roles):
                if "Alternate" in (role.name for role in member.roles):
                    return
            
                b_role = discord.utils.find(lambda r: r.name == "Killer Queen", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Killer Queen", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                ab_role = discord.utils.find(lambda r: r.name == "Matured", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, ab_role)
                takingstand = 0
                
            if "The Hand" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "The Hand", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "The Hand", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Echoes Egg" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Echoes Egg", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Echoes Egg", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Echoes ACT1" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Echoes ACT1", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Echoes ACT1", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Echoes ACT2" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Echoes ACT2", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Echoes ACT2", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Echoes ACT3" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Echoes ACT3", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Echoes ACT3", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Heaven's Door" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Heaven's Door", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Heaven's Door", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Aqua Necklace" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Aqua Necklace", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Aqua Necklace", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Bad Company" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Bad Company", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Bad Company", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Red Hot Chili Pepper" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Red Hot Chili Pepper", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Red Hot Chili Pepper", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "The Lock" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "The Lock", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "The Lock", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Surface" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Surface", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Surface", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Love Deluxe" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Love Deluxe", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Love Deluxe", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Pearl Jam" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Pearl Jam", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Pearl Jam", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Achtung Baby" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Achtung Baby", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Achtung Baby", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Ratt" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Ratt", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Ratt", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Harvest" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Harvest", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Harvest", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Cinderella" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Cinderella", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Cinderella", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Atom Heart Father" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Atom Heart Father", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Atom Heart Father", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Boy II Man" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Boy II Man", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Boy II Man", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Earth Wind and Fire" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Earth Wind and Fire", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Earth Wind and Fire", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Highway Star" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Highway Star", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Highway Star", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Stray Cat" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Stray Cat", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Stray Cat", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Super Fly" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Super Fly", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Super Fly", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Enigma" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Enigma", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Enigma", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Cheap Trick" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Cheap Trick", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Cheap Trick", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Gold Experience" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Gold Experience", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Gold Experience", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                ab_role = discord.utils.find(lambda r: r.name == "Requiem", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, ab_role)
                takingstand = 0
                
            if "Sticky Fingers" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Sticky Fingers", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Sticky Fingers", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Moody Blues" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Moody Blues", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Moody Blues", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Sex Pistols" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Sex Pistols", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Sex Pistols", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Aerosmith" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Aerosmith", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Aerosmith", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Purple Haze" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Purple Haze", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Purple Haze", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Spice Girl" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Spice Girl", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Spice Girl", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "King Crimson" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "King Crimson", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "King Crimson", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Black Sabbath" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Black Sabbath", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Black Sabbath", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Soft Machine" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Soft Machine", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Soft Machine", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Kraft Work" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Kraft Work", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Kraft Work", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Little Feet" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Little Feet", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Little Feet", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Man in the Mirror" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Man in the Mirror", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Man in the Mirror", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Mr.President" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Mr.President", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Mr.President", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Beach Boy" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Beach Boy", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Beach Boy", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "The Grateful Dead" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "The Grateful Dead", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "The Grateful Dead", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Baby Face" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Baby Face", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Baby Face", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "White Album" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "White Album", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "White Album", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Clash" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Clash", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Clash", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Talking Head" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Talking Head", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Talking Head", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Notorious B.I.G" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Notorious B.I.G", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Notorious B.I.G", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Metallica" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Metallica", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Metallica", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Green Day" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Green Day", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Green Day", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Oasis" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Oasis", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Oasis", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Rolling Stones" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Rolling Stones", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Rolling Stones", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Stone Free" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Stone Free", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Stone Free", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Burning Down the House" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Burning Down the House", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Burning Down the House", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Foo Fighters" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Foo Fighters", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Foo Fighters", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Weather Report" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Weather Report", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Weather Report", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Diver Down" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Diver Down", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Diver Down", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Whitesnake" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Whitesnake", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Whitesnake", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "C-Moon" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "C-Moon", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "C-Moon", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
            if "Made in Heaven" in (role.name for role in member.roles):
            
                b_role = discord.utils.find(lambda r: r.name == "Made in Heaven", ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, b_role)
                takingstand = 1
                await asyncio.sleep(30)
                a_role = discord.utils.find(lambda r: r.name == "Made in Heaven", ctx.message.server.roles)
                await bot.remove_roles(ctx.message.author, a_role)
                takingstand = 0
                
@bot.command(pass_context=True)
async def steal(ctx):
    global stealed
    global charges
    global voicechrages
    global dcharge
    global mutesec
    global mutesec2
    global harvatiya
    global muting
    global spinning
    global degradations
    global degradations2
    global spinenergy
    if "Soft and Wet" in (role.name for role in ctx.message.author.roles):
        if charges > 0:
            stealed += charges
            charges = 0
            
            await bot.send_message(ctx.message.channel, "Вы украли заряды. Теперь их {}.".format(stealed))
        if voicechrages > 0:
            stealed += voicechrages
            voicechrages = 0
            
            await bot.send_message(ctx.message.channel, "Вы украли заряды. Теперь их {}.".format(stealed))
        if dcharge > 0:
            stealed += dcharge
            dcharge = 0
            
            await bot.send_message(ctx.message.channel, "Вы украли заряды. Теперь их {}.".format(stealed))
        if mutesec > 0:
            stealed += mutesec
            mutesec = 0
            
            await bot.send_message(ctx.message.channel, "Вы украли заряды. Теперь их {}.".format(stealed))
        if mutesec2 > 0:
            stealed += mutesec2
            mutesec2 = 0
            
            await bot.send_message(ctx.message.channel, "Вы украли заряды. Теперь их {}.".format(stealed))
        if harvatiya > 0:
            stealed += harvatiya
            harvatiya = 0
            
            await bot.send_message(ctx.message.channel, "Вы украли заряды. Теперь их {}.".format(stealed))
        if muting > 0:
            stealed += muting
            muting = 0
            
            await bot.send_message(ctx.message.channel, "Вы украли заряды. Теперь их {}.".format(stealed))
        if spinning > 0:
            stealed += spinning
            spinning = 0
            
            await bot.send_message(ctx.message.channel, "Вы украли заряды. Теперь их {}.".format(stealed))
        if degradations > 0:
            stealed += degradations
            degradations = 0
            
            await bot.send_message(ctx.message.channel, "Вы украли заряды. Теперь их {}.".format(stealed))
        if degradations2 > 0:
            stealed += degradations2
            degradations2 = 0
            
            await bot.send_message(ctx.message.channel, "Вы украли заряды. Теперь их {}.".format(stealed))
        if spinenergy > 0:
            stealed += spinenergy
            spinenergy = 0
            
            await bot.send_message(ctx.message.channel, "Вы украли заряды. Теперь их {}.".format(stealed))
            
@bot.command(pass_context=True)
async def newstand(ctx):
    if "Made in Heaven" in (role.name for role in ctx.message.author.roles):
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            await bot.send_message(ctx.message.author, "Чтобы **создать стенд**, сперва, вы должны его **настроить**. Этот стенд можно выдать **только** другому человеку.\n``~setstandname (текст) - поставить название стенда``\n``~setstandpic (ссылка) - поставить ссылку на картинку стенда``\n``~setability (1-5) - поставить абилку для нового стенда``\n``~abilitylist - список абилок``\n``~setstand (юзер) - создать стенд и выдать его кому-то``\n``~deletestand - удалить свой предыдущий стенд и сделать новый``")
            
@bot.command(pass_context=True)
async def abilitylist(ctx):

    if "Made in Heaven" not in (role.name for role in ctx.message.author.roles):
        return
        
    if ujeusing == 1:
        await bot.send_message(ctx.message.author, "Для начала удалите предыдущий стенд.")
        return
        
    if "Made in Heaven" in (role.name for role in ctx.message.author.roles):
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            await bot.send_message(ctx.message.author, "``Способности для будущего стенда:``\n``1`` - замутить кого-нибудь на 5 секунд\n``2`` - заспамить человеку в ЛС\n``3`` - кидать человек гей-порно в ЛС\n``4`` - размутить человека (себя нельзя)\n``5`` - стереть 10 сообщений с задержкой в 10 секунд``")
            
@bot.command(pass_context=True)
async def setability(ctx, abili : str):
    global stand_name
    global standability
    global ujeusing
    
    if "Made in Heaven" not in (role.name for role in ctx.message.author.roles):
        return
        
    if ujeusing == 1:
        await bot.send_message(ctx.message.author, "Для начала удалите предыдущий стенд.")
        return
    
    if abili == "1":
        standability = "mute"
        stand_ab = "~standmute - замутить на 5 секунд"
        await bot.send_message(ctx.message.author, "1")
    elif abili == "2":
        standability = "spam"
        stand_ab = "~standspam - заспамить уведомлениями в ЛС"
        await bot.send_message(ctx.message.author, "2")
    elif abili == "3":
        standability = "gay"
        stand_ab = "~standgay - гей-порно в ЛС при каждом сообщении"
        await bot.send_message(ctx.message.author, "3")
    elif abili == "4":
        standability = "un"
        stand_ab = "~standun - размутить человека (нельзя использовать на себя)"
        await bot.send_message(ctx.message.author, "4")
    elif abili == "5":
        standability = "erase"
        stand_ab = "~standerase - стереть 10 сообщений (кулдавн этой команды 10 секунд)"
        await bot.send_message(ctx.message.author, "5")
    else:
        await bot.send_message(ctx.message.author, "Абилки с таким номером нет.")
        return
    
    if "Made in Heaven" in (role.name for role in ctx.message.author.roles):
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            await bot.send_message(ctx.message.author, "``Информация о стенде, который вы создаёте сейчас:``\nИмя стенда: ``{}``\nВладелец стенда: ``Пока нет``\nСпособности стенда:\n``{}``".format(stand_name, stand_ab))
            
@bot.command(pass_context=True)
async def setstandpic(ctx, ssilka : str):
    global standpic
    
    if "Made in Heaven" not in (role.name for role in ctx.message.author.roles):
        return
        
    if ujeusing == 1:
        await bot.send_message(ctx.message.author, "Для начала удалите предыдущий стенд.")
        return
    
    if "Made in Heaven" in (role.name for role in ctx.message.author.roles):
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            standpic = ssilka
            await bot.send_message(ctx.message.author, "``Вы поставили картинку для вашего стенда:`` {}\n``Если она сейчас не отобразилась, значит ссылка указана неправильно, попробуйте поставить другую или исправить эту.``".format(standpic))
            
@bot.command(pass_context=True)
async def setstandname(ctx, *args):
    global stand_name
    global standability
    
    if "Made in Heaven" not in (role.name for role in ctx.message.author.roles):
        return
        
    if ujeusing == 1:
        await bot.send_message(ctx.message.author, "Для начала удалите предыдущий стенд.")
        return
    
    if standability == "mute":
        stand_ab = "~standmute - замутить на 5 секунд"
    elif standability == "spam":
        stand_ab = "~standspam - заспамить уведомлениями в ЛС"
    elif standability == "gay":
        stand_ab = "~standgay - гей-порно в ЛС при каждом сообщении"
    elif standability == "un":
        stand_ab = "~standun - размутить человека (нельзя использовать на себя)"
    elif standability == "erase":
        stand_ab = "~standerase - стереть 10 сообщений (кулдавн этой команды 10 секунд)"
    else:
        stand_ab = "Не выбрана"
    
    if "Made in Heaven" in (role.name for role in ctx.message.author.roles):
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            stand_name = ' '.join(args)
            await bot.send_message(ctx.message.author, "``Информация о стенде, который вы создаёте сейчас:``\nИмя стенда: ``{}``\nВладелец стенда: ``Пока нет``\nСпособности стенда:\n``{}``".format(stand_name, stand_ab))
            
@bot.command(pass_context=True)
async def setstand(ctx, member : discord.Member):
    global stand_name
    global standability
    global standpic
    global ujeusing
    
    if "Made in Heaven" not in (role.name for role in ctx.message.author.roles):
        return
        
    if ujeusing == 1:
        await bot.send_message(ctx.message.author, "Для начала удалите предыдущий стенд.")
        return
    
    if standability == "":
        await bot.send_message(ctx.message.author, "Вы не настроили стенд до конца. Поставьте ему способность.")
        return
        
    if stand_name == "":
        await bot.send_message(ctx.message.author, "Вы не настроили стенд до конца. Поставьте ему имя.")
        return
        
    if standpic == "":
        await bot.send_message(ctx.message.author, "Вы не настроили стенд до конца. Поставьте ссылку на картинку стенда.")
        return
        
    if ctx.message.author == member:
        await bot.send_message(ctx.message.author, "Нельзя использовать этот стенд на себе.")
        return
    
    if "Made in Heaven" in (role.name for role in ctx.message.author.roles):
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            await bot.create_role(ctx.message.author.server, name="{}".format(stand_name))
            await bot.send_message(ctx.message.author, "``Вы создали новый стенд ({}) и выдали его {}.``".format(stand_name, member.name))
            
            newstando = discord.utils.find(lambda r: r.name == "{}".format(stand_name), ctx.message.server.roles)
            await bot.add_roles(member, newstando)
            
            ujeusing = 1
            
@bot.command(pass_context=True)
async def deletestand(ctx):
    global stand_name
    global standability
    global standpic
    global ujeusing
    
    if "Made in Heaven" not in (role.name for role in ctx.message.author.roles):
        return
        
    if ujeusing == 0:
        await bot.send_message(ctx.message.author, "Вы ещё не создали стенд.")
        return
    
    if "Made in Heaven" in (role.name for role in ctx.message.author.roles):
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            role_delete = discord.utils.find(lambda r: r.name == "{}".format(stand_name), ctx.message.server.roles)
            await bot.delete_role(ctx.message.author.server, role_delete)
            
            ujeusing = 0
            stand_name = ""
            standability = ""
            standpic = ""
            
            await bot.send_message(ctx.message.author, "``Вы удалили предыдущий стенд.``")
            
@bot.command(pass_context=True)
async def standmute(ctx, member : discord.Member):
    global stand_name
    global standability
    if "{}".format(stand_name) in (role.name for role in ctx.message.author.roles):
        if stand_name == "":
            return
        if standability == "mute":
            await bot.send_message(ctx.message.channel, "**{}** замутил **{}** на **5 секунд**, атаковав своим стендом.".format(ctx.message.author.name, member.name))
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
            
            await asyncio.sleep(5)
            
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
            
@bot.command(pass_context=True)
async def standspam(ctx, member : discord.Member):
    global stand_name
    global standability
    if "{}".format(stand_name) in (role.name for role in ctx.message.author.roles):
        if stand_name == "":
            return
        if standability == "spam":
            await bot.send_message(ctx.message.channel, "**{}** заспамил уведомлениями в ЛС **{}**".format(ctx.message.author.name, member.name))
        
            await bot.send_message(member, "<@{}>".format(member.id))
            await bot.send_message(member, "<@{}>".format(member.id))
            await bot.send_message(member, "<@{}>".format(member.id))
            await bot.send_message(member, "<@{}>".format(member.id))
            await bot.send_message(member, "<@{}>".format(member.id))
            await bot.send_message(member, "<@{}>".format(member.id))
            await bot.send_message(member, "<@{}>".format(member.id))
            await bot.send_message(member, "<@{}>".format(member.id))
            
@bot.command(pass_context=True)
async def standgay(ctx, member : discord.Member):
    global stand_name
    global standability
    global gayporn
    if "{}".format(stand_name) in (role.name for role in ctx.message.author.roles):
        if stand_name == "":
            return
        if standability == "gay":
            await bot.send_message(ctx.message.channel, "**{}** теперь получает гей-порно в ЛС.".format(member.name))
        
            gayporn = member.id
            
            
@bot.command(pass_context=True)
async def standun(ctx, member : discord.Member):
    global stand_name
    global standability
    
    if member == ctx.message.author:
        return
        
    if "{}".format(stand_name) in (role.name for role in ctx.message.author.roles):
        if stand_name == "":
            return
        if standability == "un":
            await bot.send_message(ctx.message.channel, "**{}** размутил **{}**".format(ctx.message.author.name, member.name))
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
            
@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def standerase(ctx):
    global stand_name
    global standability
        
    if "{}".format(stand_name) in (role.name for role in ctx.message.author.roles):
        if stand_name == "":
            return
        if standability == "erase":
            mgs = []
            async for x in bot.logs_from(ctx.message.channel, limit = 10):
                mgs.append(x)
            await bot.delete_messages(mgs)
            
            await bot.send_message(ctx.message.channel, "**{}** стёр 10 сообщений.".format(ctx.message.author.name))
            
@bot.command(pass_context=True)
async def untime(ctx):
    global muted_all_users
    global star_stop
        
    if "Crazy Diamond" in (role.name for role in ctx.message.author.roles):
        if "Requiem" in (role.name for role in ctx.message.author.roles):
            await bot.send_message(ctx.message.channel, "**{}** вернул *время*.".format(ctx.message.author.name))   
            muted_all_users = 0
            star_stop = 0
            
@bot.command(pass_context=True)
async def urya(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Moody Blues" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "URYAAAAA, {}!".format(member.name), description = "*«УРЯЯЯЯЯ, {}!»*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://media.giphy.com/media/xUmO1mtejVad55vo0l/giphy.gif")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(4)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True)
async def shibo(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Killer Queen" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "	SHIBOBOBO, {}!".format(member.name), description = "*«СИБОБОБО, {}!»*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://i.kym-cdn.com/photos/images/original/001/204/319/316.gif")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(3)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
            
@bot.command(pass_context=True)
async def ubasha(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Purple Haze" in (role.name for role in ctx.message.author.roles):
        
        embed = discord.Embed(title = "UBASHAAAA, {}!".format(member.name), description = "*«УБАШАААА, {}!»*".format(member.name), color = 0xffff00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/09/PurpleHazevsIlluso.jpg/revision/latest/scale-to-width-down/475?cb=20170405100436")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        if "Tower of Gray" in (role.name for role in member.roles):
            if random.randint(0, 1) == 1:
                embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                await bot.send_message(ctx.message.channel, embed=embed)
                return
                
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(3)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True)
async def getinfo(ctx, member : discord.Member):
        
    if "Paisley Park" in (role.name for role in ctx.message.author.roles):
            
        await bot.send_message(ctx.message.author, "``Вот все сообщения {} за последние 50 сообщений:``".format(member.name))
        
        mgs = []
        async for x in bot.logs_from(ctx.message.channel, limit = 50):
            if x.author == member:
                await bot.send_message(ctx.message.author, "<@{}> : {}".format(x.id, x.content))
                
        await bot.send_message(ctx.message.author, "``-----------------------------------------------``")
        
@bot.command(pass_context=True)
@commands.cooldown(1, 60, commands.BucketType.user)
async def bubble(ctx, member : discord.Member):
    global mutesec
    if "Ebony Devil" in (role.name for role in member.roles):
        mutesec += 1
    if "В муте" in (role.name for role in member.roles):
        return
    if "Killer Queen" in (role.name for role in ctx.message.author.roles):
        if "Alternate" in (role.name for role in ctx.message.author.roles):
        
            embed = discord.Embed(title = "**{}** создал пузырьки под кожей **{}**".format(member.name), description = "*Мут на 10 секунд.*".format(member.name), color = 0xffff00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/b/b7/KQBubbleSasame.png/revision/latest/scale-to-width-down/269?cb=20180728203054")
            await bot.send_message(ctx.message.channel, embed=embed)
        
            if "Tower of Gray" in (role.name for role in member.roles):
                if random.randint(0, 1) == 1:
                    embed = discord.Embed(title = "Удалось увернуться от атаки.", description = "", color = 0xffff00)
                    embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/8/80/Tower-of-Gray_AnimeAV.png/revision/latest?cb=20160414185549")
                    await bot.send_message(ctx.message.channel, embed=embed)
                    return
                
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
        
            await asyncio.sleep(10)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
            
@bot.command(pass_context=True)
async def ovlist(ctx):
        
    if "Jonathan Joestar" in (role.name for role in ctx.message.author.roles):
            
        await bot.send_message(ctx.message.channel, "``Вот все овердрайвы вашего хамона ({}):``\n``sy - солнечно-жёлтый (200 энергии)``\n``lm - жизненного магнетизма (150 энергии)``\n``mso - серебрянно-металический (150 энергии)``\n``dpo - глубокопроходящий (передать свою энергию Джозефу)(150 энергии)``\n``so - песочный (100 энергии)``\n``sc - алый (50 энергии)``\n``ov - обычный (15 энергии)``".format(ctx.message.author.name))
        
    if "Joseph Joestar" in (role.name for role in ctx.message.author.roles):
            
        await bot.send_message(ctx.message.channel, "``Вот все овердрайвы вашего хамона ({}):``\n``sy - солнечно-жёлтый (200 энергии)``\n``lm - жизненного магнетизма (150 энергии)``\n``mso - серебрянно-металический (150 энергии)``\n``dpo - глубокопроходящий (передать свою энергию Джонатану)(150 энергии)``\n``so - песочный (100 энергии)``\n``sc - алый (50 энергии)``\n``ov - обычный (15 энергии)``".format(ctx.message.author.name))
        
@bot.command(pass_context=True)
async def overdrive(ctx, type : str, member : discord.Member):
    global rippleenergy
    global rippleenergy2
    global ignite_id
    if "В муте" in (role.name for role in member.roles):
        if type != "lm":
            return
    else:
        if type == "lm":
            return
    
    if "Jonathan Joestar" in (role.name for role in ctx.message.author.roles):
        if type == "sy":
            if rippleenergy >= 200:
                rippleenergy -= 200
                
                embed = discord.Embed(title = "САНРАЙТО ЙЕРО ОВАДРАЙВО, **{}**".format(member.name), description = "*Мут на 20 минут.*", color = 0xFFFF00)
                embed.set_image(url="https://media.giphy.com/media/uFmH3dmRn4nDwlJGOu/giphy.gif")
                await bot.send_message(ctx.message.channel, embed=embed)

                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(600)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
        elif type == "lm":
            if rippleenergy >= 150:
                rippleenergy -= 150
                
                embed = discord.Embed(title = "СИЙМИ ДЖИКИ НО ОВАДРАЙВО, **{}**".format(member.name), description = "*Вы размутили {}.*".format(member.name), color = 0xFFFF00)
                embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/485039703318462465/unknown.png")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
        elif type == "mso":
            if rippleenergy >= 150:
                rippleenergy -= 150
                
                embed = discord.Embed(title = "МЕТАР СИРВА ОВАРДРАЙВО, **{}**".format(member.name), description = "*Мут на 10 минут.*".format(member.name), color = 0xFFFF00)
                embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/485041253193482241/unknown.png")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
        elif type == "dpo":
            if rippleenergy >= 150:
                rippleenergy2 += rippleenergy
                rippleenergy = 0
                
                embed = discord.Embed(title = "ДИПАС ОВАРДРАЙВО, **{}**".format(member.name), description = "*Вы передали энергию Джозефу и попали в мут.*", color = 0xFFFF00)
                embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/485042985541566464/unknown.png")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, mute_role)
                
        elif type == "so":
            if rippleenergy >= 100:
                rippleenergy -= 100
                
                embed = discord.Embed(title = "СЕНДО ХАМОН ОВАРДРАЙВО, **{}**".format(member.name), description = "*Мут на 6 минут.*".format(rippleenergy), color = 0xFFFF00)
                embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/485043660753469441/unknown.png")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(360)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
        elif type == "sc":
            if rippleenergy >= 50:
                rippleenergy -= 50
                
                embed = discord.Embed(title = "СУКАРЕТ ОВЕРДРАЙВО, **{}**".format(member.name), description = "*Мут на 1 минуту и данный пользователь горит 3 минуты.*".format(rippleenergy), color = 0xFFFF00)
                embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/485044331762155520/unknown.png")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(60)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
                ignite_id = member.id
                await asyncio.sleep(120)
                ignite_id = ""
                
        elif type == "ov":
            if rippleenergy >= 15:
                rippleenergy -= 15
                
                embed = discord.Embed(title = "ХАМОН ОВЕРДРАЙВО, **{}**".format(member.name), description = "*Мут на 8 секунд.*".format(rippleenergy), color = 0xFFFF00)
                embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/485046164060897290/unknown.png")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(8)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
        else:
            await bot.send_message(ctx.message.channel, "Такого типа овердрайва нет. **({})**".format(type))
            
    if "Joseph Joestar" in (role.name for role in ctx.message.author.roles):
        if type == "sy":
            if rippleenergy2 >= 200:
                rippleenergy2 -= 200
                
                embed = discord.Embed(title = "САНРАЙТО ЙЕРО ОВАДРАЙВО, **{}**".format(member.name), description = "*Мут на 20 минут.*", color = 0xFFFF00)
                embed.set_image(url="https://media.giphy.com/media/uFmH3dmRn4nDwlJGOu/giphy.gif")
                await bot.send_message(ctx.message.channel, embed=embed)

                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(600)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
        elif type == "lm":
            if rippleenergy2 >= 150:
                rippleenergy2 -= 150
                
                embed = discord.Embed(title = "СИЙМИ ДЖИКИ НО ОВАДРАЙВО, **{}**".format(member.name), description = "*Вы размутили {}.*".format(member.name), color = 0xFFFF00)
                embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/485039703318462465/unknown.png")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
        elif type == "mso":
            if rippleenergy2 >= 150:
                rippleenergy2 -= 150
                
                embed = discord.Embed(title = "МЕТАР СИРВА ОВАРДРАЙВО, **{}**".format(member.name), description = "*Мут на 10 минут.*".format(member.name), color = 0xFFFF00)
                embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/485041253193482241/unknown.png")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
        elif type == "dpo":
            if rippleenergy2 >= 150:
                rippleenergy += rippleenergy2
                rippleenergy2 = 0
                
                embed = discord.Embed(title = "ДИПАС ОВАРДРАЙВО, **{}**".format(member.name), description = "*Вы передали энергию Джонатану и попали в мут.*", color = 0xFFFF00)
                embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/485042985541566464/unknown.png")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(ctx.message.author, mute_role)
                
        elif type == "so":
            if rippleenergy2 >= 100:
                rippleenergy2 -= 100
                
                embed = discord.Embed(title = "СЕНДО ХАМОН ОВАРДРАЙВО, **{}**".format(member.name), description = "*Мут на 6 минут.*", color = 0xFFFF00)
                embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/485043660753469441/unknown.png")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(360)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
        elif type == "sc":
            if rippleenergy2 >= 50:
                rippleenergy2 -= 50
                
                embed = discord.Embed(title = "СУКАРЕТ ОВЕРДРАЙВО, **{}**".format(member.name), description = "*Мут на 1 минуту и данный пользователь горит 3 минуты.*", color = 0xFFFF00)
                embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/485044331762155520/unknown.png")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(60)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
                ignite_id = member.id
                await asyncio.sleep(120)
                ignite_id = ""
                
        elif type == "ov":
            if rippleenergy2 >= 15:
                rippleenergy2 -= 15
                
                embed = discord.Embed(title = "ХАМОН ОВЕРДРАЙВО, **{}**".format(member.name), description = "*Мут на 8 секунд.*", color = 0xFFFF00)
                embed.set_image(url="https://cdn.discordapp.com/attachments/470567218497847296/485046164060897290/unknown.png")
                await bot.send_message(ctx.message.channel, embed=embed)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.add_roles(member, mute_role)
        
                await asyncio.sleep(8)
        
                mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
                await bot.remove_roles(member, mute_role)
                
        else:
            await bot.send_message(ctx.message.channel, "Такого типа овердрайва нет. **({})**".format(type))
                
@bot.command(pass_context=True)
async def s(ctx, *lul):
    global nextthing
    if "Joseph Joestar" in (role.name for role in ctx.message.author.roles):
        nextthing = " ".join(lul)
    
        embed = discord.Embed(title = "И СЛЕДУЮЩЕЕ, ЧТО ТЫ СКАЖЕШЬ: **{}**".format(nextthing), description = "", color = 0xFFFF00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/0a/JosephTricksWamuu.PNG/revision/latest/scale-to-width-down/640?cb=20170131062756")
        await bot.send_message(ctx.message.channel, embed=embed)
        
@bot.command(pass_context=True)
async def posseser(ctx, member : discord.Member):
    global karss
    global rippleenergy
    global rippleenergy2
    
    if "Ultimate" in (role.name for role in ctx.message.author.roles):
        return
    
    if "Kars" in (role.name for role in ctx.message.author.roles):
        if "Jonathan Joestar" in (role.name for role in member.roles):
            if rippleenergy > 0:
                await bot.send_message(ctx.message.channel, "Вы поглотили {} энергии хамона.".format(rippleenergy))
                karss += rippleenergy
                
                if karss >= 400:
                    await bot.send_message(ctx.message.author, "Вы можете активировать камень Эйша.")
                rippleenergy = 0
        elif "Joseph Joestar" in (role.name for role in member.roles):
            if rippleenergy2 > 0:
                await bot.send_message(ctx.message.channel, "Вы поглотили {} энергии хамона.".format(rippleenergy2))
                karss += rippleenergy2
                
                if karss >= 400:
                    await bot.send_message(ctx.message.author, "Вы можете активировать камень Эйша.")
                rippleenergy2 = 0
        else:
            await bot.send_message(ctx.message.channel, "Можно использовать эту абилку только на Джонатана или Джозефа.")
            
@bot.command(pass_context=True)
async def attacker(ctx, member : discord.Member):
    global karss
    
    if "В муте" in (role.name for role in member.roles):
        return
        
    if "Kars" in (role.name for role in ctx.message.author.roles):
        if "Ultimate" in (role.name for role in ctx.message.author.roles):
            karss += 1
            embed = discord.Embed(title = "**{}** атаковал **{}**".format(ctx.message.author.name, member.name), description = "Он замутил его на *{}* секунд и получил энергию.".format(karss), color = 0xFFFF00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/7/7f/KarsBird.png/revision/latest/scale-to-width-down/640?cb=20131127011920")
            await bot.send_message(ctx.message.channel, embed=embed)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.add_roles(member, mute_role)
        
            await asyncio.sleep(karss)
        
            mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
            await bot.remove_roles(member, mute_role)
            return
    
    if "Kars" in (role.name for role in ctx.message.author.roles):
        embed = discord.Embed(title = "**{}** атаковал **{}**".format(ctx.message.author.name, member.name), description = "Он замутил его на *{}* секунд.".format(karss), color = 0xFFFF00)
        embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/1/19/KarsBladeReveal.PNG/revision/latest/scale-to-width-down/640?cb=20170205215433")
        await bot.send_message(ctx.message.channel, embed=embed)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.add_roles(member, mute_role)
        
        await asyncio.sleep(karss)
        
        mute_role = discord.utils.find(lambda r: r.name == 'В муте', ctx.message.server.roles)
        await bot.remove_roles(member, mute_role)
        
@bot.command(pass_context=True)
async def aja(ctx):
    global karss
        
    if "Ultimate" in (role.name for role in ctx.message.author.roles):
        return
    
    if "Kars" in (role.name for role in ctx.message.author.roles):
        if karss >= 400:
            karss = 3
            embed = discord.Embed(title = "**ВЫ АКТИВИРОВАЛИ КРАСНЫЙ КАМЕНЬ ЭЙША.** ВЫ СТАЛИ СОВЕРШЕННОЙ ФОРМОЙ ЖИЗНИ, **{}**.".format(ctx.message.author.name.upper()), description = "", color = 0xFFFF00)
            embed.set_image(url="https://vignette.wikia.nocookie.net/jjba/images/0/07/Kars_awakened.png/revision/latest/scale-to-width-down/640?cb=20160325084229")
            await bot.send_message(ctx.message.channel, embed=embed)
            
            mute_role = discord.utils.find(lambda r: r.name == 'Ultimate', ctx.message.server.roles)
            await bot.add_roles(ctx.message.author, mute_role)
        else:
            await bot.send_message(ctx.message.channel, "Пока у вас нет камня Эйша.")
            
@bot.command(pass_context=True)
async def github(ctx):
    await bot.send_message(ctx.message.channel, "``GitHub:``\nhttps://github.com/finalfanx/jojo-discordpy-bot")
        
    
bot.run(BOT_TOKEN)