import disnake
from disnake.ext import commands
bot = commands.Bot(command_prefix=disnake.ext.commands.when_mentioned)

@bot.event
async def on_ready():
    print(f"{bot.user} работает!")

@bot.slash_command(description='тестовая комманда')
async def test(inter):
    await inter.response.send_message('Тест')

bot.run("MTI5MjQ2MzI5NTMwMjk5MjAwNA.G6PHIF.mFVY3WVNb9dZkwEIPNUJuyKN8MLoMjpkC_U-Wg")