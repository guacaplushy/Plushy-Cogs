from redbot.core import commands
from redbot.core import Config

class ErrorMessage(commands.Cog):
  def __init__(self, bot : commands.Bot):
    self.config = Config.get_conf(self, identifier=835962021)
    default_global = {
      "message": "An error occured: {error}",
    }
    self.config.register_global(**default_global)
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    await ctx.send(self.config.message().replace("{error}", str(error)))

def setup(bot : commands.Bot):
  bot.add_cog(ErrorMessage(bot=bot))
