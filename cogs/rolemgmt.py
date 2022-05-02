__author__ = 'Justin Panchula'
__copyright__ = 'Copyright 2022'
__credits__ = 'Justin Panchula, Zach Lesniewski'
__license__ = 'MIT License'
__version__ = '0.1.0'
__status__ = 'Indev'
__doc__ = """Role management functions"""

# Imports
import discord
from discord.ext.commands import Cog


class RoleMGMT(Cog):
    """
    Role management functions
    """
    # Init
    def __init__(self, bot) -> None:
        self.bot = bot

    # Check if loaded
    @Cog.listener()
    async def on_ready():
        print('Role Managment Cog loaded')


# Add to bot
def setup(bot) -> None:
    bot.add_cog(RoleMGMT(bot))
