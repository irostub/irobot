import discord
import openpyxl
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("iro bot is ready")
    game = discord.Game("'이로야 메뉴판' 치면 이로봇 작동")
    await client.change_presence(status=discord.Status.online, activity= game)

"""메세지 받고 응답"""
@client.event
async def on_message(message):
    '''명령어 차트'''
    if message.content.startswith("이로야 메뉴판"):
        await message.channel.send(embed =
                        discord.Embed(title="~이로봇 메뉴판~", description="1.이로야 바보\n    호에에에...저한테 왜그러세요\n2.이로야 뭐해?\n\t글쎄요? 뭘 하고있을까요?\n3.이로야 방송\n\t방송의 소개는 요기에서!",color=0xfcffb0))
    if message.content.startswith("이로야 바보"):
        await message.channel.send("이로는 바보가 아뉜데요~ 반사~ <:ye:556403426662023173>")
    if message.content.startswith("이로야 뭐해?"):
        await message.channel.send("벽보고 가위바위보 하고있었어요..같이 놀아줄래요..? <:nop:648089526140665857>")
    if message.content.startswith("이로야 방송"):
        await message.channel.send("손자님의 방송은 https://www.twitch.tv/g147f89d/ 에요! <:ye:556403426662023173> 잘부탁드려요!\n초인기 스트리머 손! 자! 에욧. 헤헷\n제일 잘나가는 클립은 https://www.twitch.tv/g147f89d/clip/TentativeCrunchyPangolinMikeHogu 에요!!")
    '''if message.content.startswith("이로야 채팅레벨시스템"):
        await  message.channel.send(embed = discord.Embed(message.channel,title = "~채팅 레벨 시스템~", description="\n1. 경험치 배율\n2. 획득 경험치 배율\n 3."))'''

    if message.content.startswith("이로야 학습"):
        file = openpyxl.load_workbook("study.xlsx")
        studySheet = file.active

        index = studySheet["A1"].value

        for i in range(1,index):
            if studySheet["B"+ i ].value == message.content:
                await message.channel.send("이미 학습한 내용이에요!\n"+message.content+"에 대한 답변은 "+ studySheet["C"+i]+"에요! 어때요?")
                return



    '''채팅 경험치'''
    if message.content.startswith("") and message.author.id != 681631352722161693:
        file = openpyxl.load_workbook("level.xlsx")
        sheet = file.active
        exp = []

        for j in range(1,31):
            reb = j
            rex = 0

            exp.append((j+2)*j*10)

        for j in range(0,30):
            print(exp[j])

        i = 1
        while True:
            '''구 유저 채팅'''
            if sheet["A"+str(i)].value == str(message.author.id):
                await asyncio.sleep(3)
                if sheet["C"+str(i)].value < 30:
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




client.run("")