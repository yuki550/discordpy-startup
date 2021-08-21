import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

q = []
@client.event
async def on_message(message):
    global q
    if message.author.bot:
        return
    elif message.content.startswith('qadd'):
        q.append(message.content[5:])
        await message.add_reaction('👍')
    elif message.content == 'qrand':
        if(len(q) == 0):
            await message.channel.send('問題がありません。')
        else:
            await message.channel.send(random.choice(q))
    elif message.content == 'qclear':
        q = []
        await message.channel.send('初期化しました。')
    elif message.content == 'qlist':
#discordは2000文字以上のメッセージを送れません。
        sub = 0
        while True:
            if sub + 1500 < len(str(q)):
                await message.channel.send('```py\n' + str(q)[sub:sub + 1500] + '```')
            elif sub < len(str(q)) - 8:
                await message.channel.send('```py\n' + str(q)[sub:] + '```')
            else:
                break
            sub += 1500
    elif message.content.startswith('qrem'):
        q.remove(message.content[5:])
        await message.add_reaction('👍')

bot = os.environ[DISCORD_BOT_TOKEN]

bot.run(token)
