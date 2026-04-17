
import discord

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Let's go !")

@bot.event
async def on_message(message:discord.Message):
    if message.author.bot: return

    trigger = False
    liste = []

    content = message.content
    afters = content.split("[[")[1:]
    for item in afters:
        if "]]" in item:
            link = item.split("]]")[0]
            trigger = True
            liste.append("["+link+"](<https://ideopedia.miraheze.org/wiki/"+link+">)")
    
    if trigger:
        message.channel.send(", ".join(liste))

# go !
with open(r"./token.lock", 'r') as file:
    token = file.read().strip("\n")
bot.run(token)