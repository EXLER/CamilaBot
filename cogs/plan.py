import os
import logging
from pathlib import Path

import requests
import discord
from discord.ext import commands


class Plan(commands.Cog):
    """
    View or change the lesson plan for separate groups.
    """

    def __init__(self, bot):
        self.bot = bot

        os.makedirs("data/plan", exist_ok=True)

    @commands.command()
    async def plan(self, ctx):
        """Display the lesson plan for the group represented by user's role"""
        file = None
        embed = discord.Embed()
        for role in ctx.message.author.roles:
            if os.path.isfile(f"data/plan/{role}.png"):
                file = discord.File(f"data/plan/{role}.png", filename=f"{role}.png")
                embed.set_image(url=f"attachment://{role}.png")
                break

        if not file:
            await ctx.send("Żadna z twoich grup nie posiada przypisanego planu!")
            return

        await ctx.send(file=file, embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def changeplan(self, ctx, group: str):
        """Change the lesson plan for a given group with attached image"""
        async with ctx.typing():
            group = group.lower()
            print(ctx.guild.roles)
            if group not in [str(role).lower() for role in ctx.guild.roles]:
                await ctx.send("Wybrana grupa nie istnieje na serwerze!")
                return

            if not ctx.message.attachments:
                await ctx.send("Wiadomość nie zawiera załączonego planu!")
                return

            plan_image = ctx.message.attachments[0]
            if plan_image.url.endswith((".png", ".gif", ".jpg", ".jpeg")):
                img_data = requests.get(plan_image.url).content

                with open(Path("data", "plan", f"{group}.png"), "wb") as handler:
                    handler.write(img_data)
                    logging.info(f"Downloaded {plan_image.url} as {group} plan")
            else:
                await ctx.send("Załącznik nie jest zdjęciem!")
                return

        await ctx.send("Nowy plan ustawiony!")


def setup(bot):
    bot.add_cog(Plan(bot))
