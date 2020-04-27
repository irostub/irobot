import discord
import requests
import asyncio
from json import loads

twitch = "twitch id in here"
name = "nick"
channel = client.get_channel("channel code in here")
a = 0
while True:
    headers = {"Client-ID": "client id"}
    response = requests.get(
        "https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers
    )
    try:
        if loads(response.text)["data"][0]["type"] == "live" and a == 0:
            await channel.send(name + "님이 트위치에서 방송을 합니다!")
            a = 1
    except:
        a = 0
    await asyncio.sleep(10)

# need twitch broadcast alert function here
