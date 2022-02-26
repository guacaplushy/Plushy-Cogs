from redbot.core.commands import *
from nword import filter

class AntiNWord(Cog):
  @Cog.listener()
  async def on_message(self, message):
      d = filter(message)
      if d:
          message.member.ban()
          message.delete()
      
    
def setup(bot):
  bot.add_cog(AntiNWord())