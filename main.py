import discord
from datetime import datetime, timedelta
import json
import time

client = discord.Client()
json_open = open('id.json', 'r')
json_load = json.load(json_open)

server_id = json_load['server_id']
syukkinbo_channel_id = json_load['syukkinbo_channel_id']
bot_token = json_load['bot_token']




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
