await bot.change_presence(activity=discord.Game(name="a game")) # playing status (type 1)
await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url)) # streaming status (type 2)
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song")) # listening status (type 3)
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie")) # watching status (type 4)
await bot.change_presence(activity=discord.Activity(type=5, name="the hunger games")) # competing in status (type 5)
#these all support fstrings and variables inside of them


status=discord.Status.idle
status=discord.Status.dnd # do not disturb
status=discord.Status.invisible
status=discord.Status.online
