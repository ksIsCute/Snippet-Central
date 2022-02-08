import discord
from discord.ext import commands

class name(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_ready(self):
    print(f"Cog {cog.name} online!")
    
def setup(bot): 
  bot.add_cog(help(bot))
