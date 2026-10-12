# 🎨 BG Remover Bot

Telegram bot that removes image backgrounds instantly and logs every image to a private channel. Built for quality control and admin monitoring.

![Logo](logo.png)

---

## 📖 What This Bot Does

- **Removes background** from any image user sends
- **Logs every image** to a private Telegram channel (admin review)
- **Sends back** transparent PNG to the user
- **Admin can monitor** all images in real-time
- **Captures user info** (name, ID, username) for every request

---

## ⚙️ How It Works


---

## ✨ Features

| # | Feature | Detail |
|---|---|---|
| 1 | Background Remove | AI-powered removal via nobg API |
| 2 | Private Channel Log | Every image logged with user info |
| 3 | User Info Capture | Name, ID, username saved |
| 4 | Fast Processing | 5-10 seconds per image |
| 5 | Free to Use | No API key needed |
| 6 | Transparent PNG | High-quality output |
| 7 | Error Handling | Graceful failures, no crash |
| 8 | Logging | Console + file logs |

---

## 🛠️ Tech Stack

| Component | What It Does |
|---|---|
| Python 3.10+ | Main language |
| python-telegram-bot | Telegram Bot API wrapper |
| requests | HTTP calls to background-removal API |
| nobg API | Background removal service (free) |

---

## 📦 Installation

### Prerequisites

- Python 3.10+
- Telegram Bot Token (from @BotFather)
- Private Telegram Channel (for logging)

### Step 1: Clone Repository

```bash
git clone https://github.com/saifix7/Background-remover-Telegram-Bot.git

pip install -r requirements.txt

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
LOG_CHANNEL = YOUR_CHANNEL_LOD_ID  # Your private channel ID
python bg_bot.py
🎨 BG Remover Bot chal raha hai...
📢 Log Channel: -1001234567890
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/saifix7/Background-remover-Telegram-Bot.git
pip install python-telegram-bot requests
python bg_bot.py
