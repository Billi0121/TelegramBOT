from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand, Bot
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Hello Brother'
    )

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def foto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo='http://i.pinimg.com/736x/ec/b9/2d/ecb92d18c7855c986a5571c1b6f7cad2.jpg',
        caption='Here is you Foto',
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Option 1", url='https://billibi.pythonanywhere.com/'),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)

app = Application.builder().token('8093611066:AAEseXIWMBkInLQT56EVvwd-L5P6PsGPxsc').build()
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('foto', foto))
app.add_handler(CommandHandler('hello', hello))
app.add_handler(CommandHandler('help', help))
async def setup_commands(application):
    await application.bot.set_my_commands([
        BotCommand("start", "Начать"),
        BotCommand("help", "Помощь"),
        BotCommand("photo", "Отправить фото"),
    ])
app.post_init = setup_commands  # установить команды при запуске

app.run_polling()