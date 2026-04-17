
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/", intents=discord.Intents.default(), help_command=CustomHelpCommand())

@bot.event
async def on_ready():
    print("Let's go !")

@bot.event
async def on_message(message:discord.Message):
    if message.author.bot: return

    content = message.content
    afters = content.split("[[")[1:]
    for item in afters:
        if "]]" in item:
            link = item.split("]]")[0]
            await message.channel.send("["+link+"](<https://ideopedia.miraheze.org/wiki/"+link+">)")

# go !
with open(r"./token.lock", 'r') as file:
    token = file.read().strip("\n")
bot.run(token)