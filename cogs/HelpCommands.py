from discord.ext import commands


class HelpCommends(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(name='도움말', invoke_without_command=True)
    async def helpCommand(self, ctx):
        await ctx.channel.send("전체 도움말 목록")

    @helpCommand.command(name='채팅레벨')
    async def helpCommand_game(self, ctx):
        await ctx.channel.send("")

    @helpCommand.command(name='대화')
    async def helpCommand_reply(self, ctx):
        await ctx.channel.send("")

    @helpCommand.command(name='rpg게임')
    async def helpCommand_rpg(self, ctx):
        await ctx.channel.send("")

    # @commands.has_any_role(command str)


def setup(client):
    client.add_cog(HelpCommends(client))