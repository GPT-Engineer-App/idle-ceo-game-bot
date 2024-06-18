from discord.ext import commands
from db_manager import DBManager

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DBManager()

    @commands.command()
    async def list_business(self, ctx, business_id: int, price: int):
        user_id = ctx.author.id
        self.db.add_business_to_shop(user_id, business_id, price)
        await ctx.send(f'Business {business_id} listed for {price} coins.')

    @commands.command()
    async def buy_business(self, ctx, shop_id: int):
        buyer_id = ctx.author.id
        self.db.buy_business_from_shop(shop_id, buyer_id)
        await ctx.send(f'Business purchased from shop {shop_id}.')

def setup(bot):
    bot.add_cog(Shop(bot))