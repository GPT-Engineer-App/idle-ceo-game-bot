# idle-ceo-game-bot

Create an Economy Discord bot in Python with `discord.py` and an SQLite database. The bot needs to be fully functioning in every aspect. When creating systems for this bot, make them as customizable and user-friendly as possible. Store commands in cogs, with each cog in its own Python file. Write tests for everything, and don’t continue working until the tests are passed. Make sure that there is a `bot.py` that will start the bot up, includes linking with cogs, and connects to the database. The bot is supposed to be played like a game, with a theme of an "Idle CEO Game". Ensure there is early game, mid game, and end game content and balancing. Don't worry about graphics, emojis, embed images, etc.; just make placeholders for me to add them later.

### Project Requirements

#### Setup and Initialization
- **bot.py**:
  - Initialize the bot, load cogs, and connect to the SQLite database.
  - Define event listeners such as `on_ready` to confirm the bot is online and `on_message` for custom message handling if needed.

#### Database
- **SQLite Database**:
  - Serve as the backbone of the bot, storing all relevant data.
  - Use a defined schema to ensure data integrity and consistency.

#### Database Schema
- **Tables**:
  - **Users**: Contains columns for `user_id`, `username`, `balance`, and `created_at` to track user information.
  - **Businesses**: Contains columns for `business_id`, `user_id`, `business_name`, `level`, `revenue_rate`, `perk`, and `created_at` to track user-owned businesses and their details.
  - **Transactions**: Contains columns for `transaction_id`, `user_id`, `amount`, `transaction_type`, and `timestamp` to log all financial transactions.
  - **Shop**: Contains columns for `shop_id`, `user_id`, `business_id`, `price`, and `timestamp` to manage the user shop for selling businesses.

#### db_manager.py
- Centralize all database interactions in this file.
- Example functions: `get_balance`, `update_balance`, `register_user`, `get_user_profile`, `add_business`, `upgrade_business`, `get_business_revenue`, `get_random_perk`, `add_business_to_shop`, `buy_business_from_shop`.

#### Cogs and Commands
- **Economy Cog**:
  - Commands related to the economy, including checking balances, earning money, and spending money.
  - Interactions with the database to fetch user balances, update balances after earnings or spendings.
  - Examples: `balance` (to check current balance), `earn` (to add a fixed amount to the balance), `spend` (to deduct an amount from the balance).

- **Users Cog**:
  - Commands related to user management, such as registering new users and viewing user profiles.
  - Interactions with the database to add new users and retrieve user profile information.
  - Examples: `register` (to create a new user in the database), `profile` (to display the user's profile information).

- **Business Cog**:
  - Commands related to business management, including starting a business, upgrading businesses, and generating revenue.
  - Implement an idle system where businesses generate revenue automatically over time.
  - Background tasks that periodically update user balances based on business revenue.
  - Examples: `start_business` (to add a new business for the user at a cost), `upgrade_business` (to level up a business and increase its revenue rate), `generate_revenue` (automated task to add revenue to users based on their businesses).

- **Admin Cog**:
  - Admin commands for managing the game, such as adding money to users or resetting user data.
  - Requires special permissions to execute these commands.
  - Examples: `add_money` (to add a specified amount to a user's balance), `reset_user` (to reset a user's data).

- **Shop Cog**:
  - Commands related to the user shop, where users can buy and sell businesses.
  - Managing the shop inventory and transactions.
  - Examples: `list_business` (to list a business for sale), `buy_business` (to buy a listed business).

#### Gameplay Phases
1. **Early Game**:
   - Users can register and start owning their first business.
   - Focus on initial growth and accumulating basic resources.
   - Commands: `register`, `start_business`, `earn`, `balance`.

2. **Mid Game**:
   - Users can manage and upgrade multiple businesses, explore the user shop for new opportunities.
   - Introduce more complex mechanics like business upgrades, perks, and strategic investments.
   - Commands: `start_business`, `upgrade_business`, `generate_revenue`, `list_business`, `buy_business`.

3. **End Game**:
   - Users aim to own 10+ businesses, including a few legendary businesses with special perks.
   - Incorporate advanced business strategies, high-level upgrades, and competitive elements.
   - Commands: `balance`, `profile`, `admin commands`.

#### Additional Gameplay Features
- **Investments**:
  - Users can invest in other businesses or virtual stocks, adding more strategic depth.
  - Commands: `invest` (to invest a specified amount in a business or stock), `withdraw_investment` (to withdraw investment and realize gains or losses).

- **Achievements**:
  - Reward users for reaching milestones, such as earning a certain amount of money or owning a number of businesses.
  - Commands: `achievements` (to display a list of achievements), `claim_achievement` (to claim rewards for achievements).

#### Business Perks
- Each business has randomly assigned perks when acquired, which can influence revenue rates or other business attributes.
- Examples of perks: increased revenue rate, reduced upgrade costs, special bonuses during events.

#### User Shop
- Users can list their businesses for sale in a user shop, setting their own prices.
- Other users can browse the shop and purchase listed businesses.
- Shop transactions are logged and managed in the database.

#### Acquiring Businesses
- Users acquire businesses through a `start_business` command, which costs money to start, assigns a randomly generated name and perk.
- Businesses can also be acquired from other users via the shop.
- Starting a new business should deduct the cost from the user's balance.

#### Idle System
- Businesses generate revenue automatically based on time intervals.
- Implement a background task that periodically updates user balances based on their business revenue.
- Ensure the system is efficient and scalable to handle multiple users and businesses.

#### Testing
- Write unit tests for each command and system to ensure functionality and reliability.
- Cover all edge cases and validate that the commands interact correctly with the database.
- Ensure all tests pass before proceeding with further development.

### Additional Considerations
- Ensure all commands are documented in the README for ease of use and understanding.
- Create placeholders for graphics, emojis, and embed images for future customization.
- Maintain clean, modular, and scalable code to accommodate future expansions and updates.

This structure and outline will help create a fully functional and customizable Economy Discord bot with `discord.py`, designed to be an engaging "Idle CEO Game" experience.


## Collaborate with GPT Engineer

This is a [gptengineer.app](https://gptengineer.app)-synced repository 🌟🤖

Changes made via gptengineer.app will be committed to this repo.

If you clone this repo and push changes, you will have them reflected in the GPT Engineer UI.

## Tech stack

This project is built with React and Chakra UI.

- Vite
- React
- Chakra UI

## Setup

```sh
git clone https://github.com/GPT-Engineer-App/idle-ceo-game-bot.git
cd idle-ceo-game-bot
npm i
```

```sh
npm run dev
```

This will run a dev server with auto reloading and an instant preview.

## Requirements

- Node.js & npm - [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating)
