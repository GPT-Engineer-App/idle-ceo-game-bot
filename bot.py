import discord
from discord.ext import commands
import sqlite3
import os

# Initialize bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Database connection
conn = sqlite3.connect('economy.db')
c = conn.cursor()

# Create tables if they don't exist
c.execute('''CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    balance INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)''')

c.execute('''CREATE TABLE IF NOT EXISTS Businesses (
    business_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    business_name TEXT,
    level INTEGER,
    revenue_rate INTEGER,
    perk TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id)
)''')

c.execute('''CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount INTEGER,
    transaction_type TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id)
)''')

c.execute('''CREATE TABLE IF NOT EXISTS Shop (
    shop_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    business_id INTEGER,
    price INTEGER,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES Users(user_id),
    FOREIGN KEY(business_id) REFERENCES Businesses(business_id)
)''')

conn.commit()

# Load cogs
initial_extensions = ['cogs.economy', 'cogs.users', 'cogs.business', 'cogs.admin', 'cogs.shop']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

# Run the bot
bot.run(os.getenv('DISCORD_TOKEN'))