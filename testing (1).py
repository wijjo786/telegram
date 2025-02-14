
# from telegram import Update
# from telegram.ext import Application, CommandHandler, CallbackContext

# # Replace with your bot's token
# # TOKEN = "7916200857:AAGx_l-XY7a_h6ei0p1rwqbKg4cXLH7MvOo"

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # First message
    await update.message.reply_text("Hello Dear 🥰! Welcome to Phantom AI Trading with Coach Rachel. I'm excited to help you achieve your financial dreams💸🤑😊")

    # Wait 6 seconds
    await asyncio.sleep(6)

    # Second message with community button
    community_keyboard = [[InlineKeyboardButton("Join Free Community", url="https://t.me/financialfreedom_OfurePhantomAI")]]
    await update.message.reply_text(
        "Here's a link to join my free community. Once you join, come back here and I will send you a free video that gives you all the tantalizing information you need to start making passive income with Phantom AI.",
        reply_markup=InlineKeyboardMarkup(community_keyboard)
    )

    # Wait 15 seconds
    await asyncio.sleep(15)

    # Third message with video button
    video_keyboard = [[InlineKeyboardButton("Watch Video Guide", url="https://tinyurl.com/Trading-Bot-Video")]]
    await update.message.reply_text(
        "Here's a link to the video guide as promised🤝. Be sure to watch it to the end as there's a giveaway at the end. Don't miss it 😉\n\nType \"ready to install\" after you finish watching. I'll be waiting here for you 🫵",
        reply_markup=InlineKeyboardMarkup(video_keyboard)
    )

async def handle_ready(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    video_coach = [[InlineKeyboardButton("Chat With Rachel", url="https://t.me/PhantomAITrader")]]
    await update.message.reply_text("🎉 Chat with Coach Rachel",
    reply_markup =InlineKeyboardMarkup(video_coach)
    )


def main() -> None:
    # Replace with your bot token
    app = Application.builder().token("7916200857:AAGx_l-XY7a_h6ei0p1rwqbKg4cXLH7MvOo").build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Regex(r'\b(ready|install)\b', flags=re.IGNORECASE), handle_ready))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# import asyncio

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     # Send the first message
#     await update.message.reply_text(f"Hello {update.effective_user.first_name}! 👋")

#     # Add a delay (e.g., 3 seconds)
#     await asyncio.sleep(5)

#     # Send the second message with a button
#     keyboard = [[InlineKeyboardButton("Visit Our Website", url="https://www.example.com")]]
#     await update.message.reply_text(
#         text="Here's a button for you:",
#         reply_markup=InlineKeyboardMarkup(keyboard)
#     )

# app = ApplicationBuilder().token("7916200857:AAGx_l-XY7a_h6ei0p1rwqbKg4cXLH7MvOo").build()
# app.add_handler(CommandHandler("start", start))
# app.run_polling()
