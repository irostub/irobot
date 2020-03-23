from discord.ext import commands
import discord
import random
import asyncio


class ReplyCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     if message.content.startswith('text'):
    #         await message.channel.send("text")

    @commands.command(name='<Undefined>', aliases=['Undefined'])
    async def undefcall(self, ctx):
        await ctx.channel.send("이걸 제게 말했다구요? 정말 할게 없었나보네오<:_tyeayea:619838526074126346> 보상으로 이곳에 당신이 원하는 특수대사를 넣어드리죠. 주인님께 말해주세요.")

    @commands.command(name='이로', aliases=['이로님', '이로야'])
    async def selfcall(self, ctx):
        await ctx.channel.send("제 주인님은 iro_bound (입이 멋대로..움직여버렷:carrot::carrot:) 킹갓제네럴엠페러충무공마제스티하이퍼울트라판타스틱익스트림지니어스해요<:TwT:625349630317821972> ")

    @commands.command(name = '자폭', aliases = ['자폭해','사라져','미워'])
    async def destruction(self, ctx):
        await ctx.channel.send("*** 자폭 시퀸스를 작동시킵니까 Y/N ***")
        author = ctx.author
        try:
            rems = await self.client.wait_for('message',check = lambda message : ctx.author == author, timeout=10.0)

            if rems.content == "y" or rems.content == "Y":
                pic = "https://cdn.discordapp.com/attachments/689486389980692498/689556155760115732/self_destruction.jpg"
                embed = discord.Embed(color=0xfcffb0)
                embed.set_image(url=pic)
                await ctx.channel.send(embed=embed)
                await ctx.channel.send("""
```diff
-CAUTION-CAUTION-CAUTION-CAUTION-CAUTION-CAUTION-
```
""")
                await ctx.channel.send(
                    embed=discord.Embed(title="-__***SELF DESTRUCT SEQUENCE ENGAGED***__-", color=0xff0000))
                await ctx.channel.send("""
```diff
-CAUTION-CAUTION-CAUTION-CAUTION-CAUTION-CAUTION-
---Goodbye---
```
""")
                ran = random.randint(1, 100)
                if ran >= 95:
                    await self.client.logout()
                    await self.client.close()
                else:
                    msg = await ctx.channel.send("이로봇 클라이언트 복구중...")
                    await asyncio.sleep(2.0)
                    await msg.edit(content="복구 진행율 12% --클라이언트 모듈 재확인 중")
                    await asyncio.sleep(3.0)
                    await msg.edit(content="복구 진행율 48% --모듈 실행 및 초기화 중")
                    await asyncio.sleep(9.0)
                    await msg.edit(content="복구 진행율 96% --데이터 불러오기 및 무결성 검사 중")
                    await asyncio.sleep(2.0)
                    await msg.edit(content="복구 진행율 100% --복구 작업 종료 중")
                    await asyncio.sleep(2.0)
                    await msg.edit(content="이로봇 클라이언트가 복구 되었습니다.")
                    await ctx.channel.send(
                        "|| " + str(ctx.author).split("#")[0] + ", 나한테 왜 그랬어? :knife: ||")
            else:
                await ctx.channel.send("자폭 시퀸스 가동을 취소합니다.")
        except asyncio.TimeoutError:
            await ctx.channel.send("입력 시간이 초과되었습니다. 자폭 시퀸스 가동을 취소합니다.")


    # @commands.has_any_role(command str)


def setup(client):
    client.add_cog(ReplyCommands(client))