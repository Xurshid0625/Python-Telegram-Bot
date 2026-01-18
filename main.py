from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [
            InlineKeyboardButton("Toshkent", callback_data="region_1"),
            InlineKeyboardButton("Samarqand", callback_data="region_2"),
        ]
    ]

    user = update.message.from_user
    await update.message.reply_html(
        "Assalomu alaykum <b>{}!</b>\n \n<b>Ramazon oyi muborak bo'lsin</b>\n \nSizga qaysi minatqa bo'yicha ma'lumot berayin?".format(
            user.first_name
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
    )


async def region_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()

    if query.data == "region_1":
        await query.message.reply_text("📍 Siz Toshkentni tanladingiz")
    elif query.data == "region_2":
        await query.message.reply_text("📍 Siz Samarqandni tanladingiz")


def main():

    app = (
        ApplicationBuilder()
        .token("8522778567:AAF6h7icUvkw4rGv0uGkaSzwAWNXRLaWWyI")
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(region_callback))
    app.run_polling()


if __name__ == "__main__":
    main()
