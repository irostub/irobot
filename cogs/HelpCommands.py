from discord.ext import commands
import discord


class HelpCommends(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(name="도움", invoke_without_command=True)
    async def helpCommand(self, ctx):
        embed = discord.Embed(
            title="~이로 도움말~",
            description="제게 시킬 수 있는 건 이런 것들이 있어요!"
            " 아직 공사중이라서 완벽히 지원하지 않는 명령어도 있답니다!\n`!이로 도움 [명령어]`",
            color=0xFFFF80,
        )
        embed.set_author(
            name="안녕하세오...이로에오", icon_url="https://i.imgur.com/h3qAGqV.png"
        )
        embed.set_thumbnail(url="https://i.imgur.com/6J9DDq6.png")
        embed.add_field(name="`대화`", value="이로에게 말을 걸어주세요!", inline=False)
        embed.add_field(name="`학습`", value="이로에게 말을 가르쳐주세요!", inline=False)
        embed.add_field(name="`채팅`", value="채팅을 쳐서 레벨을 올려볼까요?", inline=False)
        embed.add_field(name="`강화`", value="무기를 강화해보자구요!", inline=False)
        embed.set_footer(text="@irobot made by irostub")
        await ctx.channel.send(embed=embed)

    @helpCommand.command(name="학습")
    async def helpCommand_study(self, ctx):
        embed = discord.Embed(
            title="~학습 기능~",
            description="제게 뭘 가르치고 싶으신가요? 이상한건 넣지말아주세요? 아시죠? "
            "학습시킨 대사는 대화 기능을 통해 사용할 수 있어요!\n`!이로 학습 [명령어] [sub]`",
            color=0xFFFF80,
        )
        embed.add_field(
            name="`<입력대사> , <출력대사>`",
            value="가르치고 싶은 말을 <입력대사> 에 그 대답을 <출력대사> 에 넣어주세요! ','를 빼먹으시면 안돼요!",
            inline=False,
        )
        embed.add_field(
            name="`망각 <잊을대사>`",
            value="잊게 하고싶은 말을 <잊을대사> 에 넣어주세요. 자신이 학습시킨 대사만 잊게 할 수 있어요",
            inline=False,
        )
        embed.add_field(name="`기록`", value="자신이 학습시킨 대사의 목록이에요!", inline=False)
        embed.set_footer(text="@irobot made by irostub")
        await ctx.channel.send(embed=embed)

    @helpCommand.command(name="대화")
    async def helpCommand_reply(self, ctx):
        embed = discord.Embed(
            title="~대화 기능~",
            description="저랑 얘기를 하고 싶다구요? 혹시 제가 모르는게 있다면 학습기능을 통해 알려주세요 =w=\n`!이로 [짧은대사]`",
            color=0xFFFF80,
        )
        embed.add_field(
            name="`자폭`",
            value="날..없앨꺼야..? 정말로..? <:TwT:625349630317821972>",
            inline=False,
        )
        embed.add_field(name="`이로`", value="저요? 제 주인님이요?", inline=False)
        embed.add_field(name="`<Undefined>`", value="특수 대사 3", inline=False)
        embed.add_field(name="`<Undefined>`", value="특수 대사 4", inline=False)
        embed.set_footer(text="@irobot made by irostub")
        await ctx.channel.send(embed=embed)

    @helpCommand.command(name="채팅")
    async def helpCommand_game(self, ctx):
        embed = discord.Embed(
            title="~채팅레벨 기능~",
            description="채팅을 쳐서 당신의 디코력을 뽐내보세요. 현자타임을 찾기 딱 좋아요!"
            "후추 업데이트에서 채팅으로 얻은 경험치와 무기강화가 연동될꺼에요!\n`!이로 채팅 [명령어]`",
            color=0xFFFF80,
        )
        embed.add_field(name="`룰`", value="룰을 가르쳐드릴까요?", inline=False)
        embed.add_field(name="`랭킹`", value="화려한 디코력을 확인해볼까요?", inline=False)
        embed.add_field(name="`검색 <ID>`", value="<ID>의 디코력을 확인할 수 있어요", inline=False)
        embed.add_field(name="`시스템`", value="현재 채팅레벨 기능의 설정이에요", inline=False)
        embed.set_footer(text="@irobot made by irostub")
        await ctx.channel.send(embed=embed)

    @helpCommand.command(name="강화")
    async def helpCommand_forge(self, ctx):
        embed = discord.Embed(
            title="~강화 게임~", description="\n`!이로 강화 [명령어]`", color=0xFFFF80
        )
        embed.set_thumbnail(url="https://i.imgur.com/SXKirYF.png")
        embed.add_field(name="`실행`", value="강화를 하자구욧!", inline=False)
        embed.add_field(
            name="`상태`", value="자신의 강화 상태와 강화보호권, 확률증가권 개수를 보여줘요~", inline=False
        )
        embed.add_field(
            name="`강보`", value="강보권(강화보호권)를 사용할 수 있어요. 강화가 실패하기 전까지 보호해줘요", inline=False
        )
        embed.add_field(
            name="`확증`", value="확률 증가권을 사용할 수 있어요. 중첩은 안된답니다!", inline=False
        )
        embed.add_field(name="`검색 <ID>`", value="<ID>의 현재 강화 상태정보를 보여줘요", inline=False)
        embed.add_field(name="`전당`", value="누가 이 명예의 전당에 오를 수 있을까요?", inline=False)
        embed.set_footer(text="@irobot made by irostub")
        await ctx.channel.send(embed=embed)

    # @commands.has_any_role(command str)


def setup(client):
    client.add_cog(HelpCommends(client))
