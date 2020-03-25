import discord
from discord.ext import commands
import pymysql
import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

class ChatGame(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.expTable = []
        self.initExpTable()
        self.conn = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'irobot', charset = 'utf8')
        self.curs = self.conn.cursor()
        self.sql = ""

    def initExpTable(self):
        for i in range(1 , 31):
            self.expTable.append((i+5) * i * 10)

    async def levelUpMessage(self,ctx,level,exp):
        embed = discord.Embed(title="채팅력 레벨 1UP:exclamation:", description="맙소사! 디코력이 올라갔어요!", color=ctx.author.color)
        embed.set_author(name=ctx.author.nick)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="레벨 증가", value= str(level-1)+" -> "+str(level), inline=True)
        embed.add_field(name="경험치 상한 해제", value= "현재 경험치 -> "+str(exp) + "\n다음 레벨 경험치-> " + str(self.expTable[level-1]), inline=False)
        embed.set_footer(text="@your discord power up,..hummm baka")
        await ctx.channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.content.startswith("") and not ctx.author.bot:
            self.sql = "select * from chat_player where id = %s;"
            rows_count = self.curs.execute(self.sql,ctx.author.id)
            row = self.curs.fetchall()
            totalSec = int((datetime.datetime.utcnow() - epoch).total_seconds())
            if rows_count > 0:
                id = row[0][0]
                exp = int(row[0][1])
                level = int(row[0][2])
                date = row[0][3]

                time_diff = int(totalSec - date)
                print(time_diff)
                print(totalSec)
                print(date)
                if time_diff >= 10:
                    if level <= 30:
                        exp += 5
                        if exp < self.expTable[level-1]:
                            self.sql = "update chat_player set exp = " + str(exp) + ", date = "+ str(totalSec) +" where id = " + id + ";"
                            self.curs.execute(self.sql)
                            self.conn.commit()
                        else : #exp >= self.expTable[level-1]
                            level += 1
                            self.sql = "update chat_player set exp = " + str(exp) + ",level = " + str(
                                level) +", date = "+str(totalSec)+ " where id = " + id + ";"
                            self.curs.execute(self.sql)
                            self.conn.commit()
                            await self.levelUpMessage(ctx,level,exp)



            if rows_count <= 0:
                self.sql = "insert into chat_player values("+str(ctx.author.id)+",0,1,"+str(totalSec)+");"
                self.curs.execute(self.sql)
                self.conn.commit()




def setup(client):
    client.add_cog(ChatGame(client))
