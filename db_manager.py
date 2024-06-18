import sqlite3

class DBManager:
    def __init__(self, db_name='economy.db'):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

    def get_balance(self, user_id):
        self.c.execute('SELECT balance FROM Users WHERE user_id = ?', (user_id,))
        return self.c.fetchone()

    def update_balance(self, user_id, amount):
        self.c.execute('UPDATE Users SET balance = balance + ? WHERE user_id = ?', (amount, user_id))
        self.conn.commit()

    def register_user(self, user_id, username):
        self.c.execute('INSERT INTO Users (user_id, username, balance) VALUES (?, ?, ?)', (user_id, username, 0))
        self.conn.commit()

    def get_user_profile(self, user_id):
        self.c.execute('SELECT * FROM Users WHERE user_id = ?', (user_id,))
        return self.c.fetchone()

    def add_business(self, user_id, business_name, revenue_rate, perk):
        self.c.execute('INSERT INTO Businesses (user_id, business_name, level, revenue_rate, perk) VALUES (?, ?, ?, ?, ?)', (user_id, business_name, 1, revenue_rate, perk))
        self.conn.commit()

    def upgrade_business(self, business_id):
        self.c.execute('UPDATE Businesses SET level = level + 1, revenue_rate = revenue_rate + 10 WHERE business_id = ?', (business_id,))
        self.conn.commit()

    def get_business_revenue(self, user_id):
        self.c.execute('SELECT SUM(revenue_rate) FROM Businesses WHERE user_id = ?', (user_id,))
        return self.c.fetchone()

    def get_random_perk(self):
        perks = ['Increased Revenue', 'Reduced Upgrade Costs', 'Special Bonuses']
        return random.choice(perks)

    def add_business_to_shop(self, user_id, business_id, price):
        self.c.execute('INSERT INTO Shop (user_id, business_id, price) VALUES (?, ?, ?)', (user_id, business_id, price))
        self.conn.commit()

    def buy_business_from_shop(self, shop_id, buyer_id):
        self.c.execute('SELECT business_id, price FROM Shop WHERE shop_id = ?', (shop_id,))
        business_id, price = self.c.fetchone()
        self.c.execute('UPDATE Businesses SET user_id = ? WHERE business_id = ?', (buyer_id, business_id))
        self.c.execute('DELETE FROM Shop WHERE shop_id = ?', (shop_id,))
        self.c.execute('UPDATE Users SET balance = balance - ? WHERE user_id = ?', (price, buyer_id))
        self.conn.commit()