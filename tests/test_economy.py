import unittest
from db_manager import DBManager

class TestEconomy(unittest.TestCase):
    def setUp(self):
        self.db = DBManager(':memory:')
        self.db.c.execute('''CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            balance INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        self.db.c.execute('''CREATE TABLE IF NOT EXISTS Businesses (
            business_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            business_name TEXT,
            level INTEGER,
            revenue_rate INTEGER,
            perk TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES Users(user_id)
        )''')
        self.db.c.execute('''CREATE TABLE IF NOT EXISTS Transactions (
            transaction_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            amount INTEGER,
            transaction_type TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES Users(user_id)
        )''')
        self.db.c.execute('''CREATE TABLE IF NOT EXISTS Shop (
            shop_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            business_id INTEGER,
            price INTEGER,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES Users(user_id),
            FOREIGN KEY(business_id) REFERENCES Businesses(business_id)
        )''')
        self.db.conn.commit()

    def test_register_user(self):
        self.db.register_user(1, 'testuser')
        user = self.db.get_user_profile(1)
        self.assertEqual(user[1], 'testuser')

    def test_update_balance(self):
        self.db.register_user(1, 'testuser')
        self.db.update_balance(1, 100)
        balance = self.db.get_balance(1)
        self.assertEqual(balance[0], 100)

    def test_add_business(self):
        self.db.register_user(1, 'testuser')
        self.db.add_business(1, 'testbusiness', 10, 'Increased Revenue')
        business = self.db.c.execute('SELECT * FROM Businesses WHERE user_id = 1').fetchone()
        self.assertEqual(business[2], 'testbusiness')

    def test_upgrade_business(self):
        self.db.register_user(1, 'testuser')
        self.db.add_business(1, 'testbusiness', 10, 'Increased Revenue')
        self.db.upgrade_business(1)
        business = self.db.c.execute('SELECT level FROM Businesses WHERE business_id = 1').fetchone()
        self.assertEqual(business[0], 2)

if __name__ == '__main__':
    unittest.main()