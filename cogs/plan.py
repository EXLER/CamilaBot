import os
import urllib

import discord
from discord.ext import commands

from utils import log


class Plan(commands.Cog):
    """
    View or change the lesson plan for separate groups.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def plan(self, ctx):
        """Display the lesson plan for given group.
           usage: !plan"""
        file = None
        embed = discord.Embed()
        for role in ctx.message.author.roles:
            if role.name == "Informatyka":
                if os.path.isfile("data/informatyka.png"):
                    file = discord.File(
                        "data/informatyka.png", filename="informatyka.png"
                    )
                    embed.set_image(url="attachment://informatyka.png")
                else:
                    await ctx.send(
                        "Brakuje planu dla grupy informatyka! Użyj komendy !changeplan aby dodać nowy plan."
                    )
                    return
                break
            elif role.name == "Automatyka":
                if os.path.isfile("data/automatyka.png"):
                    file = discord.File(
                        "data/automatyka.png", filename="automatyka.png"
                    )
                    embed.set_image(url="attachment://automatyka.png")
                else:
                    await ctx.send(
                        "Brakuje planu dla grupy automatyka! Użyj komendy !changeplan aby dodać nowy plan."
                    )
                    return
                break

        if file == None:
            await ctx.send(
                "Potrzebujesz posiadać przypisaną rolę: Informatyk, Automatyk"
            )
            return

        await ctx.send(file=file, embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def changeplan(self, ctx, group: str, link: str):
        """Change the lesson plan for given group. Must have plan image attached.
           usage: !changeplan <Informatyka | Automatyka>"""
        group = group.lower()
        if group != "informatyka" and group != "automatyka":
            await ctx.send("Wybierz jedną z możliwości: informatyka, automatyka")
            return

        urllib.request.urlretrieve(link, f"data/{group}.png")


def setup(bot):
    bot.add_cog(Plan(bot))
