from random import randint
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

TOKEN = '1779872877:AAGKs54Jotb37C0E7TYe0qx1KMMMkqLEYwk'

def start(update: Update, context: CallbackContext):


    update.message.reply_text('Добро пожаловать! \n' +
                              'Я телеграм бот-помощник NLP-bank. Я могу показать инормацию  о банке, посмотреть бадланс, перевести деньги, забокировать карту, написать в поддержку')


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

def start_transfer(update: Update, context: CallbackContext):
    update.message.reply_text("Введите номер вашей карты")
    print('enter 1')
    return 1

def enter_cvv_code(update: Update, context: CallbackContext):
    global card_num
    card_num = update.message.text
    update.message.reply_text("Введите cvv код карты:")
    return 2

def enter_addressee_name(update: Update, context: CallbackContext):
    global cvv_code
    cvv_code = update.message.text
    update.message.reply_text("Введите номер карты адресата")
    return 3
def enter_amount(update: Update, context: CallbackContext):
    global addressee_card
    addressee_card = update.message.text
    update.message.reply_text("Введите сумму перевода")
    return 4
def send_money(update: Update, context: CallbackContext):
    global addressee_card, cvv_code, card_num
    ammount = update.message.text
    update.message.reply_text(f"Совершен перевод с карты {card_num} на карту {addressee_card} в размере {ammount} рублей")
    return 5

def get_balance(update: Update, context: CallbackContext):
    balance = randint(0, 100000)
    update.message.reply_text("Ва")

def read(update, context):


    if update.message.text == 'block':
        reply_keyboard = [['/block']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text('Если вы хотите заблокировать карту нажмите /block', reply_markup=markup)
    elif update.message.text == 'transfer':
        reply_keyboard = [['/transfer']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text('Если вы хотите совершить перевод карту нажмите /transfer', reply_markup=markup)



# def block(update: Update, context: CallbackContext):

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("info", info))
    dispatcher.add_handler(CommandHandler("balance", get_balance))

    Dialog_block = ConversationHandler(
        entry_points=[CommandHandler('block', enter_card_number)],
        states={
            1: [MessageHandler(Filters.text, enter_pin_code)],
            2: [MessageHandler(Filters.text, block)],
        },
        fallbacks=[MessageHandler(Filters.text, start)]
    )

    Dialog_transfer = ConversationHandler(
        entry_points=[CommandHandler('start_transfer', enter_card_number)],
        states={
            1: [MessageHandler(Filters.text, enter_cvv_code)],
            2: [MessageHandler(Filters.text, enter_addressee_name)],
            3: [MessageHandler(Filters.text, enter_amount)],
            4: [MessageHandler(Filters.text, send_money)],
        },
        fallbacks=[MessageHandler(Filters.text, start)]
    )

    Dialog_balance = ConversationHandler(
        entry_points=[CommandHandler('balance', enter_card_number)],
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
    dispatcher.add_handler(Dialog_transfer)
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