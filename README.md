# 🎨 BgRemoveXevolv Bot

A powerful Telegram bot that removes image backgrounds instantly — powered by AI.

![Logo](logo.png)

## ✨ Features

- 🖼️ **Instant Background Removal** — Send a photo, get transparent PNG
- ⚡ **Fast Processing** — Results in 5-10 seconds
- 🎯 **High Quality** — AI-powered edge detection
- 🆓 **Free to Use** — No signup, no API key
- 📱 **Mobile Friendly** — Works on any device
- 🔒 **Privacy First** — Images not stored

## 🚀 How to Use

1. Open the bot on Telegram: [@YourBotUsername](https://t.me/YourBotUsername)
2. Send `/start`
3. Send any photo
4. Receive transparent PNG instantly

## 🛠️ Tech Stack

- **Python 3.10+**
- **python-telegram-bot** — Telegram API wrapper
- **requests** — API calls
- **nobg API** — Background removal engine

## 📦 Installation

### Prerequisites

- Python 3.10+
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))

### Local Setup

```bash
# Clone repository
git clone https://github.com/saifix7/bg-remover-bot.git
cd bg-remover-bot

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "BOT_TOKEN=your_token_here" > .env

# Run bot
python bot.py
