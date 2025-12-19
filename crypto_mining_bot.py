from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import random

# Dummy database (can be replaced with Redis/Firebase)
user_data = {}

# Command to start
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id not in user_data:
        user_data[user_id] = {'mined': 0}
    update.message.reply_text(
        "Welcome to Crypto Mining Bot! Use /mine to start mining. 🪙"
    )

# Mining command
def mine(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    reward = random.randint(1, 10)
    user_data[user_id]['mined'] += reward
    update.message.reply_text(f"You mined {reward} coins! Total: {user_data[user_id]['mined']} 🪙")

# Leaderboard command
def leaderboard(update: Update, context: CallbackContext) -> None:
    sorted_users = sorted(user_data.items(), key=lambda x: x[1]['mined'], reverse=True)
    message = "🏆 Leaderboard 🏆\n"
    for i, (user_id, data) in enumerate(sorted_users[:10]):
        message += f"{i+1}. User {user_id}: {data['mined']} coins\n"
    update.message.reply_text(message)

def main():
    TOKEN = "YOUR_BOT_API_TOKEN"  # Replace with your bot token from BotFather
    updater = Updater(TOKEN)
    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("mine", mine))
    dispatcher.add_handler(CommandHandler("leaderboard", leaderboard))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()