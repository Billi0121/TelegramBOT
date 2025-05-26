from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Hello Brother'
    )

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def foto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo='https://i.pinimg.com/736x/ec/b9/2d/ecb92d18c7855c986a5571c1b6f7cad2.jpg',
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

app = Application.builder().token('8093611066:AAFVTE4h4xFaU0kW0nDJD-lgVKn-q2f1PpE').build()
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('foto', foto))
app.add_handler(CommandHandler('hello', hello))
app.add_handler(CommandHandler('help', help))
app.run_polling()