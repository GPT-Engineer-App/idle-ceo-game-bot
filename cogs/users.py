from discord.ext import commands
from db_manager import DBManager

class Users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DBManager()

    @commands.command()
    async def register(self, ctx):
        user_id = ctx.author.id
        username = str(ctx.author)
        self.db.register_user(user_id, username)
        await ctx.send(f'User {username} registered successfully!')

    @commands.command()
    async def profile(self, ctx):
        user_id = ctx.author.id
        profile = self.db.get_user_profile(user_id)
        await ctx.send(f'Profile: {profile}')

def setup(bot):
    bot.add_cog(Users(bot))