import redbot.core.commands.*

class Purge(Cog):
  @command()
  async def purge(self, ctx, limit = 999999999999999999999999999 : int):
    await ctx.channel.purge(limit=limit)
    
def setup(bot):
  bot.add_cog(new Purge())
