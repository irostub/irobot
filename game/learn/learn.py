from discord.ext import commands
import discord
import pymysql


class Learn(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.conn = pymysql.connect(
            host="localhost", user="root", password="", db="irobot", charset="utf8"
        )
        self.curs = self.conn.cursor()
        self.sql = ""

    @commands.command(name="학습")
    async def Command_study(self, ctx, *args):
        input = args[0]
        output = ""
        for i in range(len(args)):
            if i == 0:
                continue
            if i == len(args) - 1:
                output = output + args[i]
            else:
                output = output + args[i] + " "

        id = ctx.author.id
        teacher = ctx.author.name

        self.sql = "select * from learn where input = %s limit 1;"

        rows_count = self.curs.execute(self.sql, input)
        rows = self.curs.fetchall()

        if rows_count > 0:
            await ctx.channel.send("이미 알고있던거 있음")
        else:
            print("here")
            self.sql = "insert into learn values(%s ,%s ,%s ,%s);"
            self.curs.execute(self.sql, (id, input, teacher, output))
            self.conn.commit()
            await ctx.channel.send(
                "잘배웠어요, 고마워요. 휴먼!\n입력 : " + input + "\n출력 : " + output
            )

    # @commands.command(db)
    # async def addf(self,ctx):
    #     a=0


def setup(client):
    client.add_cog(Learn(client))
