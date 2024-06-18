# Economy Discord Bot

## Overview
This is a fully functional Economy Discord bot built using `discord.py` and an SQLite database. The bot is designed to be an engaging "Idle CEO Game" experience, with early game, mid game, and end game content and balancing.

## Setup and Initialization
- `bot.py`: Initializes the bot, loads cogs, and connects to the SQLite database. Defines event listeners such as `on_ready` and `on_message`.

## Database
- SQLite database with tables for Users, Businesses, Transactions, and Shop.

## Database Schema
- **Users**: Contains columns for `user_id`, `username`, `balance`, and `created_at` to track user information.
- **Businesses**: Contains columns for `business_id`, `user_id`, `business_name`, `level`, `revenue_rate`, `perk`, and `created_at` to track user-owned businesses and their details.
- **Transactions**: Contains columns for `transaction_id`, `user_id`, `amount`, `transaction_type`, and `timestamp` to log all financial transactions.
- **Shop**: Contains columns for `shop_id`, `user_id`, `business_id`, `price`, and `timestamp` to manage the user shop for selling businesses.

## Cogs and Commands
- **Economy Cog**:
  - Commands related to the economy, including checking balances, earning money, and spending money.
  - Examples: `!balance`, `!earn <amount>`, `!spend <amount>`.

- **Users Cog**:
  - Commands related to user management, such as registering new users and viewing user profiles.
  - Examples: `!register`, `!profile`.

- **Business Cog**:
  - Commands related to business management, including starting a business, upgrading businesses, and generating revenue.
  - Examples: `!start_business <business_name>`, `!upgrade_business <business_id>`.

- **Admin Cog**:
  - Admin commands for managing the game, such as adding money to users or resetting user data.
  - Examples: `!add_money <user_id> <amount>`, `!reset_user <user_id>`.

- **Shop Cog**:
  - Commands related to the user shop, where users can buy and sell businesses.
  - Examples: `!list_business <business_id> <price>`, `!buy_business <shop_id>`.

## Gameplay Phases
1. **Early Game**:
   - Users can register and start owning their first business.
   - Commands: `!register`, `!start_business <business_name>`, `!earn <amount>`, `!balance`.

2. **Mid Game**:
   - Users can manage and upgrade multiple businesses, explore the user shop for new opportunities.
   - Commands: `!start_business <business_name>`, `!upgrade_business <business_id>`, `!list_business <business_id> <price>`, `!buy_business <shop_id>`.

3. **End Game**:
   - Users aim to own 10+ businesses, including a few legendary businesses with special perks.
   - Commands: `!balance`, `!profile`, `!admin commands`.

## Additional Gameplay Features
- **Investments**:
  - Users can invest in other businesses or virtual stocks, adding more strategic depth.
  - Commands: `!invest <amount>`, `!withdraw_investment`.

- **Achievements**:
  - Reward users for reaching milestones, such as earning a certain amount of money or owning a number of businesses.
  - Commands: `!achievements`, `!claim_achievement`.

## Business Perks
- Each business has randomly assigned perks when acquired, which can influence revenue rates or other business attributes.

## User Shop
- Users can list their businesses for sale in a user shop, setting their own prices.
- Other users can browse the shop and purchase listed businesses.

## Acquiring Businesses
- Users acquire businesses through a `!start_business` command, which costs money to start, assigns a randomly generated name and perk.
- Businesses can also be acquired from other users via the shop.

## Idle System
- Businesses generate revenue automatically based on time intervals.
- Implement a background task that periodically updates user balances based on their business revenue.

## Testing
- Unit tests are written for each command and system to ensure functionality and reliability.
- Tests cover all edge cases and validate that the commands interact correctly with the database.

## Documentation
- All commands are documented in this README for ease of use and understanding.

## Placeholders
- Placeholders for graphics, emojis, and embed images are created for future customization.

## Running the Bot
1. Set the `DISCORD_TOKEN` environment variable with your bot's token.
2. Run `bot.py` to start the bot.

```sh
python bot.py
```