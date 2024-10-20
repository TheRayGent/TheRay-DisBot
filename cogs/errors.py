from disnake.ext import commands
import disnake

class ErrorsCheck(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_slash_command_error(self, inter: disnake.ApplicationCommandInteraction, error: commands.CommandError):
        print('Error:', error)
        if isinstance(error, commands.errors.NotOwner):
            await inter.response.send_message("Эту комманду может использовать только владелец бота!", flags=disnake.MessageFlags(ephemeral=True), delete_after=5.0)

def setup(bot: commands.Bot):
    bot.add_cog(ErrorsCheck(bot))