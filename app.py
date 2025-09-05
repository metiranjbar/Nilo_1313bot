from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import logging

# ---------------- تنظیمات ----------------
TOKEN = 8437778241:AAGDCdKLvzv5bq_nOq8kJgiuG0bCyUZz1fs
CHANNEL_USERNAME = "@nilo_1313"   # آیدی کانال
YOUTUBE_LINK = "https://www.youtube.com/@drYouTube18"
VIDEO_FILE_ID = "BAACAgQAAxkBAAECuopouWVUJtfMpcsmetdNqNPVz9REhQAC5gsAAjv7cFGU6qYqULI0MjYE"

# ---------------- لاگینگ ----------------
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# ---------------- توابع ----------------
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")],
        [InlineKeyboardButton("🎥 سابسکرایب یوتیوب", url=YOUTUBE_LINK)],
        [InlineKeyboardButton("✅ تایید کردم", callback_data="check")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("سلام 👋\nبرای دریافت ویدیو باید عضو کانال و یوتیوب بشی:", reply_markup=reply_markup)

def check_membership(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    member = context.bot.get_chat_member(CHANNEL_USERNAME, user_id)

    if member.status in ["member", "administrator", "creator"]:
        context.bot.send_video(chat_id=user_id, video=VIDEO_FILE_ID, supports_streaming=True)
        query.answer("✅ عضویت تایید شد! ویدیو برات ارسال شد.")
    else:
        query.answer("❌ هنوز عضو کانال نشدی!", show_alert=True)

# ---------------- ران کردن ربات ----------------
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(check_membership, pattern="check"))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
