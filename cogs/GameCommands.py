from discord.ext import commands

class GameCommends(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(name = '채팅레벨', invoke_without_command = True)
    async def gameCommand(self,ctx):
        await ctx.channel.send("채팅레벨시스템 헬프메세지")

    @gameCommand.command(name = '룰')
    async def gameCommand_help(self,ctx):
        await ctx.channel.send("룰 도움말")

    @gameCommand.command(name = '조회')
    async def gameCommand_show(self,ctx):
        await ctx.channel.send("조회 도움말")
        
    @gameCommand.command(name = '랭킹')
    async def gameCommand_rank(self,ctx):
        await ctx.channel.send("랭킹 도움말")

    #@commands.has_any_role(command str)

def setup(client):
    client.add_cog(GameCommends(client))