import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", case_insensitive=True, help_command=None)

@bot.event
async def on_ready():
  print("online!")

bot.run(TOKEN)
