from disnake.ext import commands
import disnake

class ColorChoice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description='color')
    async def color(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message('Тест')

def setup(bot: commands.Bot):
    bot.add_cog(ColorChoice(bot))