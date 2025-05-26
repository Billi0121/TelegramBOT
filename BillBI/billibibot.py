from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот.")

# /help с кнопкой
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔗 Подробнее", url="https://example.com")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Нажми на кнопку, чтобы узнать больше:",
        reply_markup=reply_markup
    )

# /photo — отправка фото
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://i.pinimg.com/736x/ec/b9/2d/ecb92d18c7855c986a5571c1b6f7cad2.jpg",
        caption="Вот тебе картинка, брат! 📸"
    )

# ❌ Все остальные сообщения (фото, текст, голос и т.д.)
async def block_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⛔ Только команды разрешены! Используй /start или /help.")

# Создание приложения
app = Application.builder().token("8093611066:AAHeyUy3WGGc00peTNgyUbuvH54vv_mLolQ").build()

# Обработчики команд
app.add_handler(CommandHandler("start", start)) 
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("photo", photo))

# Обработчик на ВСЕ остальные типы сообщений
app.add_handler(MessageHandler(filters.ALL & (~filters.COMMAND), block_all))

# Запуск
app.run_polling()
