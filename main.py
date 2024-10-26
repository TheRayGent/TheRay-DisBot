from configparser import ConfigParser
import disnake
from disnake.ext import commands
cfg = ConfigParser()
bot = commands.Bot(command_prefix=commands.when_mentioned, reload=True, intents=disnake.Intents.all())
cfg.read('cfg.cfg')
if __name__ == '__main__':
    @bot.event
    async def on_ready():
        print(f"{bot.user} работает!")
    bot.load_extension("cogs.color")
    bot.load_extension("cogs.errors")

    @bot.slash_command(description='Перезагрузка когов', default_member_permissions=disnake.Permissions(administrator=True))
    @commands.is_owner()
    async def reload(inter: disnake.ApplicationCommandInteraction, cog_name: str = commands.Param(default=None, choices=[j for j, j1 in bot.extensions.items()])):
        if cog_name == None:
            for i in [j for j, j1 in bot.extensions.items()]:
                bot.reload_extension(i)
                print(i, 'перезагружен!')
            await inter.response.send_message('Все коги перезагружены!')
        else:
            bot.reload_extension(cog_name)
            print(cog_name, 'перезагружен!')
            await inter.response.send_message(f'{cog_name} перезагружен!')
bot.run(cfg.get('Default', 'bot_key'))
