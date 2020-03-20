import discord
import openpyxl
import asyncio
import random
import sys

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
        ran3 = random.randint(0,2)
        if ran3 == 0:
            await message.channel.send("왜 부르셨죠? <:what:628253366774136852>")
        if ran3 == 1:
            await message.channel.send("아..아앗 잠시만! <:ueeeeeeeeAA:645990546426429450> \n덕분에 수레를 탔네요. 고마워요.<:zombiro:624176632424300554>")
        if ran3 == 2:
            await message.channel.send("...<:hate:623830011874639872>")

    if str(message.content) == "이로야 메뉴판":
        embed = discord.Embed(title="~이로봇 메뉴판~",
                              description="부르셨나요 주인님? 무엇을 주문하시겠어요? \n아래의 메뉴에서 골라주세요.",
                              color=0xfcffb0)
        embed.add_field(name="설마 아니죠..?", value="이로야 바보", inline=False)
        embed.add_field(name="궁금해요!", value="이로야 뭐해?", inline=False)
        embed.add_field(name="방송", value="이로야 방송", inline=False)
        embed.add_field(name="레벨링 시스템", value="이로야 레벨", inline=False)
        embed.add_field(name="학습 시스템", value="이로야 학습 입력 출력", inline=False)
        embed.add_field(name="~~자폭 시퀸스~~", value="이로야 ~~자폭해~~", inline=False)
        await message.channel.send(embed = embed)

    if message.content == "이로야 자폭해":
        await message.channel.send("*** 자폭 시퀸스를 작동시킵니까 Y/N ***")
        ctx = message.author
        try:
            remsg = await client.wait_for('message',check=lambda message : message.author==ctx,timeout=10.0)

            if remsg.content == "y" or remsg.content == "Y":
                pic = "https://cdn.discordapp.com/attachments/689486389980692498/689556155760115732/self_destruction.jpg"
                embed = discord.Embed(color=0xfcffb0)
                embed.set_image(url=pic)
                await message.channel.send(embed=embed)
                await message.channel.send("""
```diff
-CAUTION-CAUTION-CAUTION-CAUTION-CAUTION-CAUTION-
```
""")
                await message.channel.send(embed= discord.Embed(title = "-__***SELF DESTRUCT SEQUENCE ENGAGED***__-",color=0xff0000))
                await message.channel.send("""
```diff
-CAUTION-CAUTION-CAUTION-CAUTION-CAUTION-CAUTION-
---Goodbye---
```
""")
                ran = random.randint(1,100)
                if ran >= 99:
                    await client.logout()
                    client.close()
                else:
                    msg = await message.channel.send("이로봇 클라이언트 복구중...")
                    await asyncio.sleep(2.0)
                    await msg.edit(content = "복구 진행율 12% --클라이언트 모듈 재확인 중")
                    await asyncio.sleep(3.0)
                    await msg.edit(content = "복구 진행율 48% --모듈 실행 및 초기화 중")
                    await asyncio.sleep(9.0)
                    await msg.edit(content = "복구 진행율 96% --데이터 불러오기 및 무결성 검사 중")
                    await asyncio.sleep(2.0)
                    await msg.edit(content = "복구 진행율 100% --복구 작업 종료 중")
                    await asyncio.sleep(2.0)
                    await msg.edit(content="이로봇 클라이언트가 복구 되었습니다.")
                    await message.channel.send("|| "+str(message.author).split("#")[0]+", 나한테 왜 그랬어? :knife: ||")
            else:
                await message.channel.send("자폭 시퀸스 가동을 취소합니다.")
        except asyncio.TimeoutError:
            await message.channel.send("입력 시간이 초과되었습니다. 자폭 시퀸스 가동을 취소합니다.")


    if "이로야" in message.content:
        if "바보" in message.content:
            ran = random.randint(0,6)
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
            if ran == 6:
                await message.channel.send("너무해오..<:TwT:625349630317821972>")

    if "이로야" in message.content:
        if "사랑" in message.content:
            ran = random.randint(0,1)
            if ran == 0:
                await message.channel.send("고마워욧 <:DABONG:655795237868011537>")
            if ran == 1:
                await message.channel.send("저도 좋아하고 있어요 XD")

        if "너무해" in message.content:
            await message.channel.send("그러게 왜 그러셨어요. 이제부터 잘 해주세요!")

    if message.content.startswith("이로야 뭐해"):
        ran = random.randint(0,4)
        if ran == 0:
            await message.channel.send("벽보고 가위바위보 하고있었어요..같이 놀아줄래요..? <:nop:648089526140665857>")
        if ran == 1:
            await message.channel.send("네.생.각 <:nemui:619842429314400258>")
        if ran == 2:
            await message.channel.send("RR3라는 녀석을 어떻게 처리할까 계획을 세우고있었어요 <:emoji_42:673959929605783596>")
        if ran == 3:
            await message.channel.send("그래 그녀석은 여기를 이렇게 묶고 요렇게 해서 미국으로 보내줘야지..(중얼중얼) <:yandereIro:646691446086434835>")
        if ran == 4:
            await message.channel.send("주인님이 공부하라고한 아재개그? 라는걸 외우고 있었어요.\n음...어디보자 택시기사가 좋아하는 동물은 뭘까요???\n\n||타이거<:__:556410154434691097>||")

    if message.content.startswith("이로야 방송"):
        await message.channel.send("지금은 방송에 대한 소개가 없어요. 생기면 알려드릴게요 <:idonthaveEar:556398411499438090>")
    if message.content.startswith("이로야 학습"):
        await message.channel.send("아직 학습 시스템은 제가 할 수 없는 일이에요! 조금만 기다려주시면 열심히 배워올게요! <:idonthaveEar:556398411499438090>")
    if message.content.startswith("이로야 레벨"):
        await message.channel.send(embed=discord.Embed(title = "~채팅 레벨 시스템~", description="\n1. 경험치 증가율 공식은 (x+2)*x*10 이에요\n2. 현재 획득 경험치량은 3초에 한번씩 계산하여 채팅당 +5점이에요\n3. 현재 만렙은 30까지 설정되어있어요",color=0xfcffb0))

    '''if message.content.startswith("이로야 학습"):
        file = openpyxl.load_workbook("study.xlsx")
        studySheet = file.active

        index = studySheet["A1"].value

        for i in range(1,index):
            if studySheet["B"+ i ].value == message.content:
                await message.channel.send("이미 학습한 내용이에요!\n"+message.content+"에 대한 답변은 "+ studySheet["C"+i]+"에요! 어때요?")
                return
'''


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