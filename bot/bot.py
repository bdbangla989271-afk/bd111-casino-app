import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("8617853962:AAEMTP-DnsR_TBVVGt1csYbiCUvPMCSJUUI")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to BD111 Real Casino 🎰\nPlay Slot: https://bd111casino.com/slot.html"
    )

async def deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Deposit Request Received! ✅")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("deposit", deposit))

print("🤖 BD111 Real Casino Bot is running...")
app.run_polling()
