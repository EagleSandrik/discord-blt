from config import token
import discord
import random

def gen_pass(pass_length = 8):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("Bye!")
    elif message.content.startswith('bot'):
        await message.channel.send("Bot is currently running!")
    elif  message.content.lower().startswith("$passgen"):
        await message.channel.send(gen_pass())
    elif message.content.lower().startswith("$abt"):
        await message.channel.send("About me! I am a bot. Thats kinda it...")
    elif message.content.lower().startswith("$list"):
        await message.channel.send("`$abt`,`$hello`,`$bye`,`$passgen`,`$list`.")
    elif message.content.lower().startswith(">admin"):
        await message.channel.send("Current admin of this bot is <@790254318389166111>")
    elif message.content.lower().startswith("$whois"):
        await message.channel.send("EagleSandrik,(<@790254318389166111>) Account made in 2020, Badges: HyperSquad (<:hyper:1273324937503047720>) Nitro (<:nitro:1273324914274730148>), Booster (<a:booster:1273324877469847603>), Legacy (<:legacy:1273324851104448570>)")

    else:
        await message.channel.send(message.content)

client.run(token)
#----------------------------------------------------------






