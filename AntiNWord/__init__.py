from redbot.core.commands import *
from .nword import filter

class AntiNWord(Cog):
  @Cog.listener()
  async def on_message(self, message):
      d = filter(message.content)
      if d:
          await message.author.ban(reason="racist D:")
          await message.delete()
      
    
def setup(bot):
  bot.add_cog(AntiNWord())