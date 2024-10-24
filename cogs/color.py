from disnake.ext import commands
import disnake

class ColorChoice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def colors(inter: disnake.ApplicationCommandInteraction, message: str,
                    color1: disnake.Role = commands.Param(name='color_red', default=None),
                    color2: disnake.Role = commands.Param(name='color_orange', default=None),
                    color3: disnake.Role = commands.Param(name='color_yellow', default=None),
                    color4: disnake.Role = commands.Param(name='color_green', default=None),
                    color5: disnake.Role = commands.Param(name='color_light_blue', default=None),
                    color6: disnake.Role = commands.Param(name='color_blue', default=None),
                    color7: disnake.Role = commands.Param(name='color_pink', default=None),
                    color8: disnake.Role = commands.Param(name='color_violet', default=None),
                    color9: disnake.Role = commands.Param(name='color_white', default=None),
                    color10: disnake.Role = commands.Param(name='color_black', default=None)
                    ):
        coloremojidict=[
            '<:red:1298797800191955044>',
            '<:orrange:1298797777345708102>',
            '<:yellow:1298797846384083005>',
            '<:green:1298797748556136580>',
            '<:light_blue:1298797762057601054>',
            '<:blue:1298797739445850183>',
            '<:pink:1298797790625005628>',
            '<:violett:1298797814410776618>',
            '<:white:1298797829904404621>',
            '<:black:1298797726108094494>' 
        ]
        colorrolelist = []
        colorlist = [color1, color2, color3, color4, color5, color6, color7, color8, color9, color10]
        for i in range(len(colorlist)):
            if colorlist[i] != None:
                colorrolelist.append(disnake.SelectOption(label=colorlist[i].name, value=colorlist[i].id, emoji=coloremojidict[i]))
        if colorrolelist != []:
            await inter.response.send_message(
                message,
                components=[
                    disnake.ui.StringSelect(
                        custom_id="color_choice",
                        options=colorrolelist,
                        min_values=0,
                        max_values=1
                    )
                ]
            )
        else: await inter.response.send_message('Вы не выбрали ни одну роль!', flags=disnake.MessageFlags(ephemeral=True), delete_after=10.0)
    
        
        
    @commands.slash_command()
    @commands.is_owner()
    async def test(inter: disnake.ApplicationCommandInteraction):
        print(inter.channel.members)
        await inter.response.send_message(f"{inter.guild.members}")
    
    @commands.Cog.listener('on_dropdown')
    async def color_listener(self, inter: disnake.MessageInteraction):
        if inter.component.custom_id != "color_choice":
            return
        await inter.response.send_message(f"{inter.values}")


def setup(bot: commands.Bot):
    bot.add_cog(ColorChoice(bot))