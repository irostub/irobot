import discord
import openpyxl

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("iro bot is ready")
    game = discord.Game("이로 복제")
    await client.change_presence(status=discord.Status.online, activity= game)

"""메세지 받고 응답"""
@client.event
async def on_message(message):
    '''명령어 차트'''
    if message.content.startswith("=iro help"):
        await message.channel.send("commend is empty")
    if message.content.startswith("=iro baka"):
        await message.channel.send("you too!")
    if message.content.startswith("=iro"):
        await message.channel.send("")
    if message.content.startswith("=iro baka"):
        await message.channel.send("you too!")
    if message.content.startswith("=iro help"):
        await message.channel.send("commend is empty")
    if message.content.startswith("=iro baka"):
        await message.channel.send("you too!")
    if message.content.startswith("=iro help"):
        await message.channel.send("commend is empty")
    if message.content.startswith("=iro baka"):
        await message.channel.send("you too!")

    '''채팅 경험치'''
    if message.content.startswith("") and message.author.id != 681631352722161693:
        file = openpyxl.load_workbook("level.xlsx")
        sheet = file.active
        exp = [10,20,30,40,50]
        i = 1
        while True:
            '''구 유저 채팅'''
            if sheet["A"+str(i)].value == str(message.author.id):
                '''점수주기'''
                sheet["B"+str(i)].value = sheet["B"+str(i)].value+5
                if sheet["B"+str(i)].value >= exp[sheet["C"+str(i)].value-1]:
                    sheet["C"+str(i)].value = sheet["C"+str(i)].value +1
                    await message.channel.send(message.channel,embed =
                    discord.Embed(title="레벨 업!" , description="레벨이 올랐습니다. \n현재 레벨 : "+ str(sheet["C"+ str(i)].value)+"\n경험치" + str(sheet["B"+str(i)].value),color=0xfcffb0))
                file.save("level.xlsx")
                discord
                break

            '''유저가 신규 채팅'''
            if sheet["A" + str(i)].value == None:
                sheet["A"+str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 0
                sheet["C" + str(i)].value = 1
                file.save("level.xlsx")
                break
            i+=1




client.run('''DiscordBot Token''')