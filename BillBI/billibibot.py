from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот.")

# /help с кнопкой
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔗 Подробнее", url="https://billibi.pythonanywhere.com/auth/login/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Нажми на кнопку, чтобы узнать больше:",
        reply_markup=reply_markup
    )

# Запуск
app = Application.builder().token("8093611066:AAHeyUy3WGGc00peTNgyUbuvH54vv_mLolQ").build()
app.add_handler(CommandHandler("start", start)) 
app.add_handler(CommandHandler("help", help)) 
app.run_polling()
