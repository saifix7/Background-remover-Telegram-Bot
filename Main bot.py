"""
BG Remover Bot — Fresh Version
Background Remove + Private Channel Logging
"""

import logging
import requests
from io import BytesIO
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, MessageHandler, filters, ContextTypes
)

# =========================================================
# CONFIG
# =========================================================
BOT_TOKEN = "ENTER_YOUR_BOT_TOKEN"
API_URL = "https://api.nobg.akshit.io/api/v1/remove-background"
LOG_CHANNEL = ENTER_YOUR_LOG # Apna private channel ID

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# =========================================================
# COMMANDS
# =========================================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎨 *BG Remover Bot*\n\n"
        "Image bhejo, background remove kar dunga!\n\n"
        "⚡ Powered by EvolvX",
        parse_mode="Markdown"
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 *Help*\n\n"
        "1. Image bhejo\n"
        "2. Bot background remove karega\n"
        "3. Transparent PNG milega",
        parse_mode="Markdown"
    )


async def about_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *BG Remover Bot*\n\n"
        "Developer: SAIFIX\n"
        "Brand: EvolvX\n"
        "Version: 1.0",
        parse_mode="Markdown"
    )


# =========================================================
# PHOTO HANDLER
# =========================================================
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    photo = update.message.photo[-1]
    
    # 1. Private channel mein log karo
    try:
        await context.bot.send_photo(
            chat_id=LOG_CHANNEL,
            photo=photo.file_id,
            caption=(
                f"📥 *New Image*\n\n"
                f"👤 Name: {user.first_name}\n"
                f"🆔 ID: `{user.id}`\n"
                f"🔗 Username: @{user.username or 'N/A'}"
            ),
            parse_mode="Markdown"
        )
        logger.info(f"Logged image from {user.first_name}")
    except Exception as e:
        logger.error(f"Log error: {e}")
    
    # 2. User ko processing message
    msg = await update.message.reply_text("⏳ Processing...")
    
    try:
        # 3. Image download
        file = await context.bot.get_file(photo.file_id)
        image_bytes = bytes(await file.download_as_bytearray())
        
        # 4. API call — background remove
        files = {"image": ("photo.jpg", image_bytes, "image/jpeg")}
        response = requests.post(API_URL, files=files, timeout=60)
        
        if response.status_code != 200:
            await msg.edit_text(f"❌ Error: {response.status_code}")
            return
        
        # 5. Send back
        output = BytesIO(response.content)
        output.name = "no_bg.png"
        
        await update.message.reply_document(
            document=output,
            filename="no_bg.png",
            caption="✅ Background removed!\n\n⚡ EvolvX"
        )
        
        # 6. Delete processing message
        await msg.delete()
        
        logger.info(f"Processed for {user.first_name}")
        
    except Exception as e:
        logger.error(f"Process error: {e}")
        await msg.edit_text(f"❌ Error: {str(e)[:100]}")


# =========================================================
# ERROR HANDLER
# =========================================================
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Error: {context.error}")


# =========================================================
# MAIN
# =========================================================
def main():
    if "YOUR_BOT_TOKEN" in BOT_TOKEN:
        print("❌ BOT_TOKEN set karo!")
        return
    
    if -1001234567890 == LOG_CHANNEL:
        print("⚠️ LOG_CHANNEL set karo!")
        return
    
    print("🎨 BG Remover Bot chal raha hai...")
    print(f"📢 Log Channel: {LOG_CHANNEL}")
    
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("about", about_cmd))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    app.add_error_handler(error_handler)
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
