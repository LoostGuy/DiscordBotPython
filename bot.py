import discord
import os
import logging
import json
from discord.ext import commands, tasks
from pathlib import Path

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

#Config
secret_file = json.load(open(cwd+'/botConfig/secret.json'))
bot = commands.Bot(command_prefix='.', case_sensitive=False)
bot.config_token = secret_file['token']
logging.basicConfig(level=logging.INFO)

#events
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(bot.config_token)