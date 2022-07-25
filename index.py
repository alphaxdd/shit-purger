import os
import discord
from discord.ext import commands

#command clean
token = "" #ur dc acc token
prefix = ";" #selfbot prefix

print("trash purger")

os.system('color f')
bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.command()
async def clean(ctx, limit: int=None):
   passed = 0
   failed = 0
   async for msg in ctx.message.channel.history(limit=limit):
       if msg.author.id == bot.user.id:
           try:
               await msg.delete()
               passed += 1
           except:
               failed += 1
   os.system('color f')
   print(f" [Done] {passed} Deleted messages and {failed} faileds.")
   os.system('color 9')

bot.run(token, bot=False)
