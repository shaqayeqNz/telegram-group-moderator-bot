import telebot
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

bad_words = ["bad_word1", "bad_word2", "bad_word3"]
warnings = {}


def has_bad_words(text):
    for word in bad_words:
        if word in text.lower():
            return True
    return False


@bot.message_handler(func=lambda message: True)
def message_handler(message):

    if has_bad_words(message.text):

        user_id = str(message.from_user.id)

        if user_id in warnings:
            warnings[user_id] += 1
        else:
            warnings[user_id] = 1

        if warnings[user_id] >= 3:

            bot.ban_chat_member(
                message.chat.id,
                message.from_user.id
            )

            username = message.from_user.username or message.from_user.first_name

            bot.send_message(
                message.chat.id,
                f"user {username} has been kicked out because of breaking rules."
            )

        else:

            bot.reply_to(
                message,
                f"Please don't use bad words!\n"
                f"You received warning {warnings[user_id]}.\n"
                f"If your warnings exceed 3, you will be kicked out of the group!"
            )


bot.infinity_polling()