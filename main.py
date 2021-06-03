from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

TOKEN = '1779872877:AAGKs54Jotb37C0E7TYe0qx1KMMMkqLEYwk'

def start(update: Update, context: CallbackContext):


    update.message.reply_text('Привет, я бот Информатишка. Я помогу тебе в сдаче ЕГЭ по информатике. \
Выбери номер задания, я выдам тебе задачу. Введи ответ и я проверю его правильность. \
Введите команду /practice, чтобы начать решать задания. \
Чтобы смотреть теорию, напишите /theory')
    print(update.message.text)
    print(update.message.text)

def info(update: Update, context: CallbackContext):
    update.message.reply_text('ООО NLP Bank')

def enter_card_number(update: Update, context: CallbackContext):
    update.message.reply_text("Введите номер своей карты:")
    print('enter 1')
    return 1

def enter_pin_code(update: Update, context: CallbackContext):
    print('enter 2')
    global card_num
    card_num = update.message.text
    update.message.reply_text("Введите пин код карты:")
    return 2

def block(update: Update, context: CallbackContext):
    print('enter 3')
    global card_num
    pin_code = update.message.text
    update.message.reply_text("Карта " + card_num + ' заблокирована')
    return 2

def read(update, context):


    if update.message.text == 'block':
        reply_keyboard = [['/block']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text('Если вы хотите заблокировать карту нажмите /block', reply_markup=markup)


# def block(update: Update, context: CallbackContext):

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("info", info))

    Dialog_block = ConversationHandler(
        entry_points=[CommandHandler('block', enter_card_number)],
        states={
            1: [MessageHandler(Filters.text, enter_pin_code)],
            2: [MessageHandler(Filters.text, block)],
        },
        fallbacks=[MessageHandler(Filters.text, start)]
    )
    #
    # Dialog_theory = ConversationHandler(
    #     entry_points=[CommandHandler('theory', conv_begin)],
    #     states={
    #         1: [MessageHandler(Filters.text, theory)],
    #     },
    #     fallbacks=[MessageHandler(Filters.text, start)]
    # )
    # # dispatcher.add_handler(CommandHandler("photo", send_photo))
    dispatcher.add_handler(Dialog_block)
    # dispatcher.add_handler(Dialog_theory)

    # dispatcher.add_handler(MessageHandler(Filters.text, help_command))


    # dispatcher.add_handler(MessageHandler(Filters.text, echo))
    text_handler = MessageHandler(Filters.text, read)

    # Регистрируем обработчик в диспетчере.
    dispatcher.add_handler(text_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()