from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ⚠️ আপনার BotFather থেকে পাওয়া টোকেন বসান
TOKEN = "8617853962:AAEMTP-DnsR_TBVVGt1csYbiCUvPMCSJUUI"

# /start কমান্ড হ্যান্ডলার
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to BD111 Real Casino 🎰\nPlay Slot: http://localhost:8000/slot.html"
    )

# /deposit কমান্ড হ্যান্ডলার
async def deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Deposit Request Received! ✅")

# Bot Application তৈরি
app = ApplicationBuilder().token(TOKEN).build()

# কমান্ড যুক্ত করা
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("deposit", deposit))

# Bot চালু করা
print("🤖 BD111 Real Casino Bot is running...")
app.run_polling()
