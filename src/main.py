import discord
from zalando_bot import ZalandoBot

TOKEN = 'here goes your token'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!kod'):
        await message.channel.send('Twój kod jest generowany')
        bot = ZalandoBot(1)
        code = bot.generate_code()
        await message.channel.send(str(code))

client.run(TOKEN)
