import discord
import os

client = discord.Client()
@client.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드 봇 이름:" + client.user.name)
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("컴마스터봇 베타v1.0ㅣ컴마야 도움말"))

@client.event
async def on_message(message):
    if message.content == ("컴마스터"):
        await message.channel.send("천재")
    if message.content == ("commaster"):
        await message.channel.send("kind youtuber!")

@client.event
async def on_message(message):
    if message.content == "컴마야 도움말":
        embed = discord.Embed(title="컴마스터 봇", description="명령어들 (도움말)", color=0x00ff00)

        embed.add_field(name="컴마스터", value="대답 : 천재", inline=False)
        embed.add_field(name="commaster", value="대답 : kind youtuber!", inline=False)

        embed.add_field(name="컴마야 도움말", value="명령어 알려주는 명령어(?)같은 (?) ( 뭐가 어케된거야 )", inline=False)
        embed.add_field(name="컴마야 개발자에게 후원", value="https://toon.at/donate/donate-com", inline=False)

        embed.set_footer(text="Bot Made by. 컴마스터#5830 | Donate : https://toon.at/donate/donate-com")
        await message.channel.send (embed=embed)

        
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
