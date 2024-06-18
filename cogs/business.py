from discord.ext import commands, tasks
from db_manager import DBManager
import random

class Business(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DBManager()
        self.generate_revenue.start()

    @commands.command()
    async def start_business(self, ctx, business_name: str):
        user_id = ctx.author.id
        revenue_rate = random.randint(1, 10)
        perk = self.db.get_random_perk()
        self.db.add_business(user_id, business_name, revenue_rate, perk)
        await ctx.send(f'Business {business_name} started with perk: {perk}')

    @commands.command()
    async def upgrade_business(self, ctx, business_id: int):
        self.db.upgrade_business(business_id)
        await ctx.send(f'Business {business_id} upgraded!')

    @tasks.loop(minutes=1)
    async def generate_revenue(self):
        users = self.db.c.execute('SELECT user_id FROM Users').fetchall()
        for user in users:
            user_id = user[0]
            revenue = self.db.get_business_revenue(user_id)[0]
            if revenue:
                self.db.update_balance(user_id, revenue)
                user_obj = await self.bot.fetch_user(user_id)
                await user_obj.send(f'You earned {revenue} coins from your businesses!')

def setup(bot):
    bot.add_cog(Business(bot))