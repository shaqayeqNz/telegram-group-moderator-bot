# Telegram Group Moderator Bot 🤖

A Python Telegram bot for automatic group moderation.

The bot detects predefined bad words, tracks user warnings, and automatically bans users after repeated violations.

## Features

* 🔍 Detects predefined bad words
* ⚠️ Tracks warnings for users
* 🚫 Automatically bans users after 3 violations
* 💬 Sends warning messages to users
* 🔐 Uses environment variables to keep the bot token private
* 🐍 Built with Python and `pyTelegramBotAPI`

## How It Works

When a user sends a message containing a prohibited word:

1. The bot detects the bad word.
2. The user's warning count is increased.
3. The bot sends a warning message.
4. After 3 violations, the user is automatically banned from the group.

## Project Structure

```text
telegram-group-moderator-bot/
│
├── bot.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/shaqayeqNz/telegram-group-moderator-bot.git
cd telegram-group-moderator-bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the bot token

Create a `.env` file in the project root:

```env
API_TOKEN=your_telegram_bot_token_here
```

You can get a bot token from Telegram's BotFather.

### 5. Run the bot

```bash
python bot.py
```

## Telegram Permissions

For the bot to moderate a group, it needs to be added as an administrator.

Make sure the bot has permission to:

* Delete messages (if message deletion is added later)
* Ban users

## Configuration

You can modify the list of prohibited words in `bot.py`:

```python
bad_words = ["bad_word1", "bad_word2"]
```

You can also change the warning limit:

```python
if warnings[user_id] >= 3:
```

## Important Note

Warning data is currently stored in memory.

This means warning counts will be reset whenever the bot restarts.

A database such as SQLite can be added in the future to make warning data persistent.


## License

This project is licensed under the MIT License.
