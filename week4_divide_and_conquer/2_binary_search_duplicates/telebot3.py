from datetime import datetime
from logging import error
from telegram.constants import UPDATE_MESSAGE
from telegram.ext import *
from telegram.ext import updater
from telegram.ext import filters
from telegram.update import Update

print("بزن بریم")


def simple_response(input_message):
    user_message=str(input_message).lower()
    if user_message in ("سلام","چطوری","چه خبر"):
        return "سلام چطوری؟"
    if user_message in ("فردا بریم بیرون؟","کجایی"):
        return "حله"
    if user_message in ("ساعت چنده؟","چه زمانی؟"):
        now=datetime.now()
        date_time=now.strftime("%d/%m/%y,%H:%M:%S")
        return str(date_time)


def start_command(update,context):
    update.message.reply_text("چی میگی چیکار داری از خواب بیدارم کردی")

def help_command(update,context):
    update.meesage.reply_text("اگه کاری از دستم برمیاد بگو")

def handle_message(update,context):
    text=str(update.message.text).lower()
    R=simple_response(text)
    update.message.reply_text(R)
def erorr(update,context):
    print(f"دستور {update} منجر به خطای {context} شد")

def main():
    upd=Updater("2113880404:AAHpCyJmar7KS0O1AILmp6j6lmZqmPkYRwI",use_context=True)
    dp=upd.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_error_handler(error)
    upd.start_polling()
    upd.idle()
main()
