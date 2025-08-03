import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler, CallbackQueryHandler, ContextTypes
from poster_api import get_sales_data
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот для анализа продаж из Poster POS. Отправь голос или текст.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text or "[Голосовое сообщение]"
    response_text = f"Вы хотите получить топ-5 продаж за 7 дней?\n\nВаш запрос: \"{user_input}\""
    keyboard = [
        [InlineKeyboardButton("✅ Да", callback_data="confirm"),
         InlineKeyboardButton("❌ Нет", callback_data="cancel")]
    ]
    await update.message.reply_text(response_text, reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "confirm":
        result = get_sales_data()
        await query.edit_message_text(f"Вот данные:\n{result}")
    else:
        await query.edit_message_text("Окей. Попробуй переформулировать запрос.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
