
import discord
import re

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
            page = item.split(suffix)[0].replace(" ","_")
            if len(page)>0 and not "|" in page:
                lien = namespace + page
                liste.append("["+lien+"](<https://ideopedia.miraheze.org/wiki/"+lien+">)")

@bot.event
async def on_message(message:discord.Message):
    if message.author.bot: return

    liste = []

    # ignorer `...` et {{{...}}}
    contenu = re.sub("{{{[^{]*}}}","",re.sub("`[^`]+`","",message.content))

    chercher("[[",   "]]", "",         contenu, liste)
    chercher("{{",   "}}", "Modèle:",  contenu, liste)
    chercher("{{A|", "}}", "Article:", contenu, liste)
    
    if len(liste)>0:
        await message.channel.send(", ".join(liste))

# go !
with open(r"./token.lock", 'r') as file:
    token = file.read().strip("\n")
bot.run(token)