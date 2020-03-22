import discord
import settings
from discord.ext import commands

token = settings.token
client = commands.Bot(command_prefix= '!이로 ',help_command=None)

extensions = ['cogs.GameCommands','cogs.HelpCommands','cogs.ReplyCommands','game.chat.ChatGame']

'''봇이 시작될 때'''
@client.event
async def on_ready():
    print("iro bot is ready")
    game = discord.Game("!이로 도움말")
    await client.change_presence(status=discord.Status.online, activity= game)

for extensions in extensions:
    try:
        client.load_extension(extensions)
    except Exception as error:
        print("x")

'''RUN BOT'''
client.run(token)