import discord
from discord.ext import commands
from config import token

# Replace 'your-bot-token' with your actual bot token
BOT_TOKEN = token

# Intents are required to specify what permissions your bot needs
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command to send the embed
@bot.command()
async def embed(ctx):
    embed = discord.Embed(
        title="Welcome to the BOT system! ",
        description="This is an embedded message.",
        color=discord.Color.blue()
    )

    # Check if the bot has an avatar
    if bot.user.avatar:
        embed.set_author(name="Test 01", icon_url=bot.user.avatar.url)
    else:
        embed.set_author(name="Test 01")

    embed.add_field(name="Field 1", value="Some value", inline=False)
    embed.add_field(name="Field 2", value="Another value", inline=True)
    embed.set_footer(text="This is a footer")

    await ctx.send(embed=embed)

# Start the bot
bot.run(BOT_TOKEN)
