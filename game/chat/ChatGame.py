from discord.ext import commands
import pymysql


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

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.content.startswith("") and ctx.author.id != 681631352722161693:
            self.sql = "select * from chat_player where id = %s;"
            rows_count = self.curs.execute(self.sql,ctx.author.id)
            row = self.curs.fetchall()
            if rows_count > 0:
                id = row[0][0]
                exp = int(row[0][1])
                level = int(row[0][2])

                if level <= 30:
                    exp += 5
                    if exp >= self.expTable[level-1] :
                        level += 1
                        await ctx.channel.send(str(ctx.author).split("#")[0] + "님 채팅력 UP!")
                    self.sql = "update chat_player set exp = "+str(exp)+",level = "+str(level)+" where id = " + id+ ";"
                    self.curs.execute(self.sql)
                    self.conn.commit()

            if rows_count <= 0:
                self.sql = "insert into chat_player values("+str(ctx.author.id)+",0,1);"
                self.curs.execute(self.sql)
                self.conn.commit()





def setup(client):
    client.add_cog(ChatGame(client))
