from disnake.ext import commands
import disnake

class Miscellaneous(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command()
    @commands.is_owner()
    async def test(inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"{inter.author._roles}")

def setup(bot: commands.Bot):
    bot.add_cog(Miscellaneous(bot))