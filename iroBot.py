import discord
import settings
from discord.ext import commands

token = settings.token
client = commands.Bot(command_prefix='!이로 ', help_command=None)

extensions = ['cogs.GameCommands', 'cogs.HelpCommands', 'cogs.ReplyCommands', 'game.chat.ChatGame','game.learn.learn']

'''봇이 시작될 때'''


@client.event
async def on_ready():
    print("iro bot is ready")
    game = discord.Game("!이로 도움")
    await client.change_presence(status=discord.Status.online, activity=game)

# 채널 message에서 해당 채널의 모든 맴버를 get
# @client.event
# async def on_message(message):
#     mem = message.channel.members
#     print(mem)

for extensions in extensions:
    try:
        client.load_extension(extensions)
    except Exception as error:
        print('{} cannot be loaded. [{}]'.format(extensions, error))

'''RUN BOT'''
client.run(token)
