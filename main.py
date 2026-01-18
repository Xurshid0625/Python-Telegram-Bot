from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [
            
        ]
    ]
    
    user = update.message.from_user
    await update.message.reply_html(
        "Assalomu alaykum <b>{}!</b>\n \n<b>Ramazon oyi muborak bo'lsin</b>\n \nSizga qaysi minatqa bo;yicha ma'lumot berayin?".format(
            user.first_name
        ),
    )


def main():

    app = (
        ApplicationBuilder()
        .token("8522778567:AAF6h7icUvkw4rGv0uGkaSzwAWNXRLaWWyI")
        .build()
    )
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()
