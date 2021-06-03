from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

TOKEN = '1779872877:AAGKs54Jotb37C0E7TYe0qx1KMMMkqLEYwk'

def start(update: Update, context: CallbackContext):
    reply_keyboard = [['/practice', '/theory'], ['/reg', '/stats']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text('Привет, я бот Информатишка. Я помогу тебе в сдаче ЕГЭ по информатике. \
Выбери номер задания, я выдам тебе задачу. Введи ответ и я проверю его правильность. \
Введите команду /practice, чтобы начать решать задания. \
Чтобы смотреть теорию, напишите /theory', reply_markup=markup)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher


    dispatcher.add_handler(CommandHandler("start", start))
    # Dialog = ConversationHandler(
    #     entry_points=[CommandHandler('practice', conv_begin)],
    #     states={
    #         1: [MessageHandler(Filters.text, practice)],
    #         2: [MessageHandler(Filters.text, check)],
    #     },
    #     fallbacks=[MessageHandler(Filters.text, start)]
    # )
    #
    # Dialog_theory = ConversationHandler(
    #     entry_points=[CommandHandler('theory', conv_begin)],
    #     states={
    #         1: [MessageHandler(Filters.text, theory)],
    #     },
    #     fallbacks=[MessageHandler(Filters.text, start)]
    # )
    # # dispatcher.add_handler(CommandHandler("photo", send_photo))
    # dispatcher.add_handler(Dialog)
    # dispatcher.add_handler(Dialog_theory)
    # dispatcher.add_handler(MessageHandler(Filters.text, help_command))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()