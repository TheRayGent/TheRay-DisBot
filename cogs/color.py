from disnake.ext import commands
import disnake

class ColorChoice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def color(inter: disnake.ApplicationCommandInteraction, colors: disnake.Role = None):
        print(inter.guild.roles[4].members[0].guild.members)
        await inter.response.send_message(
            f"{inter.guild.members}"
            
        )
        '''components=[
                disnake.ui.StringSelect(
                    custom_id="color_choice",
                    options=[
                        disnake.SelectOption(label="Dog", description="Dogs are your favorite type of animal", value='YA'),
                        "Cat",
                        "Snake",
                        "Gerbil"
                    ],
                    min_values=0
                )
            ]'''
    
    @commands.Cog.listener('on_dropdown')
    async def color_listener(self, inter: disnake.MessageInteraction):
        if inter.component.custom_id != "fav_animal":
            return
        await inter.response.send_message(f"A{inter.values}")


def setup(bot: commands.Bot):
    bot.add_cog(ColorChoice(bot))