from discord.ext import commands
from db_manager import DBManager

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DBManager()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_money(self, ctx, user_id: int, amount: int):
        self.db.update_balance(user_id, amount)
        await ctx.send(f'Added {amount} coins to user {user_id}.')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reset_user(self, ctx, user_id: int):
        self.db.c.execute('DELETE FROM Users WHERE user_id = ?', (user_id,))
        self.db.c.execute('DELETE FROM Businesses WHERE user_id = ?', (user_id,))
        self.db.c.execute('DELETE FROM Transactions WHERE user_id = ?', (user_id,))
        self.db.c.execute('DELETE FROM Shop WHERE user_id = ?', (user_id,))
        self.db.conn.commit()
        await ctx.send(f'User {user_id} has been reset.')

def setup(bot):
    bot.add_cog(Admin(bot))