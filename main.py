import disnake
from disnake.ext import commands
bot = commands.Bot(command_prefix=disnake.ext.commands.when_mentioned)

if __name__ == '__main__':
    @bot.event
    async def on_ready():
        print(f"{bot.user} работает!")
    
    bot.load_extension("cogs.color")

    @bot.event
    async def on_slash_command_error(inter: disnake.ApplicationCommandInteraction, error: commands.CommandError):
        print(error.args)
        if isinstance(error, commands.errors.NotOwner):
            await inter.response.send_message("Эту комманду может использовать только владелец бота!", flags=disnake.MessageFlags(ephemeral=True), delete_after=5.0)

    

    @bot.slash_command(description='Перезагрузка когов', default_member_permissions=disnake.Permissions(administrator=True))
    @commands.is_owner()
    async def reload(inter: disnake.ApplicationCommandInteraction, cog_name: str = commands.Param(choices=['Все коги']+[j for j, j1 in bot.extensions.items()])):
        if cog_name == 'Все коги':
            for i in [j for j, j1 in bot.extensions.items()]:
                bot.reload_extension(i)
                print(i, 'перезагружен!')
            await inter.response.send_message('Все коги перезагружены!')
        else:
            bot.reload_extension(cog_name)
            print(cog_name, 'перезагружен!')
            await inter.response.send_message(f'{cog_name} перезагружен!')
    
        

bot.run("MTI5MjQ2MzI5NTMwMjk5MjAwNA.G6PHIF.mFVY3WVNb9dZkwEIPNUJuyKN8MLoMjpkC_U-Wg")