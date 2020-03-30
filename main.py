import discord
from datetime import datetime, timedelta
import json
import time
import os

client = discord.Client()


server_id = int(os.environ['SERVER_ID'])
syukkinbo_channel_id = int(os.environ['SYUKKIN_ID'])
bot_token = str(os.environ['BOT_TOKEN_ID'])



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_voice_state_update(member, before, after): 
    if member.guild.id == server_id and before.channel != after.channel:
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(syukkinbo_channel_id)

        if before.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {after.channel.name} に参加しました。'
            time.sleep(1)
            await alert_channel.send(msg)
        elif after.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。'
            time.sleep(1)
            await alert_channel.send(msg) 
            

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '霊圧' in message.content:
        await message.channel.send('消えた・・・？')


client.run(bot_token)
