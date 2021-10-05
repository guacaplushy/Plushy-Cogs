from redbot.core.commands import *

class Purge(Cog):
  @command()
  async def purge(self, ctx, limit : int = 999999999999999999999999999):
    await ctx.channel.purge(limit=limit)
    
def setup(bot):
  bot.add_cog(Purge())
