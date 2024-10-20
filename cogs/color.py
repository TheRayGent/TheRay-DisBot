from disnake.ext import commands
import disnake

class ColorChoice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def animals(inter: disnake.ApplicationCommandInteraction):
        """Sends a message with our dropdown containing the animals"""

        await inter.response.send_message(
            "What is your favorite type of animal?",
            components=[
                disnake.ui.StringSelect(
                    custom_id="fav_animal",
                    options=[
                        disnake.SelectOption(label="Dog", description="Dogs are your favorite type of animal", value='YA'),
                        "Cat",
                        "Snake",
                        "Gerbil"
                    ],
                    min_values=0
                )
            ],
        )
    @commands.Cog.listener('on_dropdown')
    async def fav_animal_listener(self, inter: disnake.MessageInteraction):
        # First we should check if the interaction is for the `fav_animal` dropdown we created
        # and ignore if it isn't.
        if inter.component.custom_id != "fav_animal":
            return

        # Now we can respond with the user's favorite animal
        await inter.response.send_message(f"A{inter.values}")


def setup(bot: commands.Bot):
    bot.add_cog(ColorChoice(bot))