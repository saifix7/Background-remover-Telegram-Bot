"""
BG Remover Bot — Simple version (no .env needed)
"""

import requests
from io import BytesIO
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ⚠️ YAHAN APNA TOKEN DAALO
BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN"

API_URL = "https://api.nobg.akshit.io/api/v1/remove-background"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎨 BG Remover Bot\n\n"
        "Photo bhejo, background remove kar dunga!\n\n"
        "Made by SAIFIX"
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 Help\n\n"
        "1. Photo bhejo\n"
        "2. Bot background remove karega\n"
        "3. Transparent PNG milega\n\n"
        "Limit: 20 images/day"
    )


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text("⏳ Processing...")

        photo = update.message.photo[-1]
        file = await context.bot.get_file(photo.file_id)
        image_bytes = await file.download_as_bytearray()

        files = {"image": ("photo.jpg", bytes(image_bytes), "image/jpeg")}
        response = requests.post(API_URL, files=files, timeout=60)

        if response.status_code != 200:
            await update.message.reply_text(f"❌ Error: {response.status_code}")
            return

        output = BytesIO(response.content)
        output.name = "no_bg.png"

        await update.message.reply_document(
            document=output,
            filename="no_bg.png",
            caption="✅ Background removed!"
        )

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)[:100]}")


def main():
    print("🤖 Bot chal raha hai...")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.run_polling()


if __name__ == "__main__":
    main()
