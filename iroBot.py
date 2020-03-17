import discord
import openpyxl
import asyncio
import random

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
    if str(message.content) == "이로야":
        await message.channel.send("왜 부르셨죠?")

    if str(message.content) == "이로야 메뉴판":
        embed = discord.Embed(title="~이로봇 메뉴판~",
                              description="부르셨나요 주인님? 무엇을 주문하시겠어요? 아래의 메뉴에서 골라주세요.",
                              color=0xfcffb0)
        embed.add_field(name="설마 아니죠..?", value="이로야 바보", inline=False)
        embed.add_field(name="궁금해요!", value="이로야 뭐해?", inline=False)
        embed.add_field(name="방송", value="이로야 방송", inline=False)
        embed.add_field(name="레벨링 시스템", value="이로야 레벨", inline=False)
        await message.channel.send(embed = embed)

    if message.content.startswith("이로야 바보"):
        ran = random.randint(0,5)
        if ran == 0:
            await message.channel.send("이로는 바보가 아뉜데요~ 반사~ <:ye:556403426662023173>")
            '''await asyncio.sleep(3000)'''
            '''await message.edit(content="<:ye:556403426662023173>")'''
        if ran == 1:
            await message.channel.send("<:Zkick:622776629093072896>")
        if ran == 2:
            await message.channel.send("지켜보겠습니다. 주인님. 밤길 조심하시길...<:hate:623830011874639872>")
        if ran == 3:
            await message.channel.send("네! 저는 바보에오 <:O_:624586351085355027>")
        if ran == 4:
            await message.channel.send("<:gesori:626761719796072448>")
        if ran == 5:
            await message.channel.send("왜에에에에에에!! <:_cry:618801401052659712>")

    if message.content.startswith("이로야 뭐해?"):
        await message.channel.send("벽보고 가위바위보 하고있었어요..같이 놀아줄래요..? <:nop:648089526140665857>")
    if message.content.startswith("이로야 방송"):
        await message.channel.send("지금은 방송에 대한 소개가 없어요. 생기면 알려드릴게요 <:idonthaveEar:556398411499438090>")
    if message.content.startswith("이로야 레벨"):
        '''await message.channel.send(embed=discord.Embed(message.channel,title = "~채팅 레벨 시스템~", description="\n1. 경험치 증가율 공식은 (x+2)*x*10 입니다.\n2. 현재 획득 경험치량은 3초에 한번씩 계산하여 채팅당 +5점입니다.\n3. 현재 만렙은 30까지 설정되어있습니다."),color=0xfcffb0)'''
        await message.channel.send("아직은 비밀이에요 =w=")

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
                        '''await message.channel.send(message.channel,embed =
                        discord.Embed(title="레벨 업!" , description="레벨이 올랐습니다. \n현재 레벨 : "+ str(sheet["C"+ str(i)].value)+"\n경험치" + str(sheet["B"+str(i)].value),color=0xfcffb0))'''
                    file.save("level.xlsx")
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