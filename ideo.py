
import discord

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Let's go !")

def chercher(prefix, suffix, namespace, content, liste):
    items = content.split(prefix)[1:]
    for item in items:
        if suffix in item:
            link = namespace + item.split(suffix)[0].replace(" ","_")
            if not "|" in link:
                liste.append("["+link+"](<https://ideopedia.miraheze.org/wiki/"+link+">)")

@bot.event
async def on_message(message:discord.Message):
    if message.author.bot: return

    liste = []

    chercher("[[",   "]]", "",         message.content, liste)
    chercher("{{",   "}}", "Modèle:",  message.content, liste)
    chercher("{{A|", "}}", "Article:", message.content, liste)
    
    if len(liste)>0:
        await message.channel.send(", ".join(liste))

# go !
with open(r"./token.lock", 'r') as file:
    token = file.read().strip("\n")
bot.run(token)