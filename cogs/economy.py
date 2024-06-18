from discord.ext import commands
from db_manager import DBManager

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DBManager()

    @commands.command()
    async def balance(self, ctx):
        user_id = ctx.author.id
        balance = self.db.get_balance(user_id)
        await ctx.send(f'Your balance is {balance[0]} coins.')

    @commands.command()
    async def earn(self, ctx, amount: int):
        user_id = ctx.author.id
        self.db.update_balance(user_id, amount)
        await ctx.send(f'You earned {amount} coins!')

    @commands.command()
    async def spend(self, ctx, amount: int):
        user_id = ctx.author.id
        self.db.update_balance(user_id, -amount)
        await ctx.send(f'You spent {amount} coins!')

def setup(bot):
    bot.add_cog(Economy(bot))