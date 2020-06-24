from discord.ext import commands


class Calendar(commands.Cog):
    """
    Schedule one-time or repeating events.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calendar(self, ctx):
        """Usage of the calendar command"""
        await ctx.send(
            "Usage: !calendar <event_name> <date>" "\nDate format: HH:MM DD:MM:YYYY"
        )


def setup(bot):
    bot.add_cog(Calendar(bot))
