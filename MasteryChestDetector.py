import discord
from discord.ext import commands
import BotCommands as botcomm


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!' , intents=intents)

@client.event
async def on_message(message):
    if message.content.startswith('!sandik'):
        args = message.content.split()
        if len(args) == 3:
            ad = args[1]
            tag = args[2]
            credits = botcomm.callpuuids(ad, tag)
            s = credits[0]
            a = credits[1]
            p = credits[2]
            tb = str(botcomm.doeverything(p, s, a))
            with open('sonuclar.txt', 'w') as f:
                f.write(tb)

            # dosyayı kanala gönderme
            with open('sonuclar.txt', 'rb') as f:
                await message.reply(file=discord.File(f))
        else:
            await message.channel.send("Kullanım: !kayit <ad> <tag>")


client.run("token") # write ur token here
   