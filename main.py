from random import randint
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, \
    ConversationHandler

TOKEN = '1779872877:AAFM0z3EPu23T169XtMcD7DUEvfcRYSb2H4'


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Добро пожаловать! \n' +
                              'Я телеграм бот-помощник NLP-bank. Я могу показать инормацию '+
                                'о банке, посмотреть бадланс, перевести деньги, забокировать' +
                                'карту, написать в поддержку. \n' + 'Для начала работы введите'+
                                ' номер вашей карты')

    return 1


def info(update: Update, context: CallbackContext):
    update.message.reply_text('ООО NLP Bank')


def enter_card_number(update: Update, context: CallbackContext):
    update.message.reply_text("Введите номер своей карты:")
    return 1


def enter_pin_code(update: Update, context: CallbackContext):
    global card_num
    card_num = update.message.text
    update.message.reply_text("Введите пин код карты:")
    return 2

def enter_cvv_code(update: Update, context: CallbackContext):
    global pin_code
    pin_code = update.message.text
    update.message.reply_text("Введите cvv код карты:")
    return 3

def finish_login(update: Update, context: CallbackContext):
    global card_num
    cvv_code = update.message.text
    update.message.reply_text(f"Вы вошли в систему с картой {card_num}")
    return ConversationHandler.END

def start_blocking(update: Update, context: CallbackContext):
    global card_num
    update.message.reply_text(f"Вы уверены что хотите заблокировать карту {card_num}?")
    update.message.reply_text("Введите пин код карты для подтверждения")
    return 1

def finish_blocking(update: Update, context: CallbackContext):
    pin_code = update.message.text
    reply_keyboard = [['/start']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(f"Вы заблокировали карту {card_num}", reply_markup=markup)
    return ConversationHandler.END

def block(update: Update, context: CallbackContext):
    global card_num
    pin_code = update.message.text
    update.message.reply_text("Карта " + card_num + ' заблокирована')
    return ConversationHandler.END


def enter_addressee_name(update: Update, context: CallbackContext):
    global cvv_code
    cvv_code = update.message.text
    update.message.reply_text("Введите номер карты адресата")
    return 1


def enter_amount(update: Update, context: CallbackContext):
    global addressee_card
    addressee_card = update.message.text
    update.message.reply_text("Введите сумму перевода")
    return 2


def send_money(update: Update, context: CallbackContext):
    global addressee_card, cvv_code, card_num
    ammount = update.message.text
    update.message.reply_text(
        f"Совершен перевод с карты {card_num} на карту {addressee_card} в размере {ammount} рублей")
    return ConversationHandler.END


def get_balance(update: Update, context: CallbackContext):
    global card_num
    balance = randint(0, 100000)
    update.message.reply_text(f"Баланс карты {card_num} составляет {balance} рублей")
    return


def stream(update, context):
    if update.message.text == 'block':
        reply_keyboard = [['/block']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text('Если вы хотите заблокировать карту нажмите /block',
                                  reply_markup=markup)
    elif update.message.text == 'transfer':
        reply_keyboard = [['/transfer']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text('Если вы хотите совершить перевод карту нажмите /transfer',
                                  reply_markup=markup)
    elif update.message.text == 'balance':
        reply_keyboard = [['/balance']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text('Чтобы узнать баланс вашей карты нажмите /balance',
                                  reply_markup=markup)


# def block(update: Update, context: CallbackContext):

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("info", info))
    dispatcher.add_handler(CommandHandler("balance", get_balance))

    dialog_start = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(Filters.text, enter_pin_code)],
            2: [MessageHandler(Filters.text, enter_cvv_code)],
            3: [MessageHandler(Filters.text, finish_login)],
        },
        fallbacks=[MessageHandler(Filters.text, start)]
    )

    dialog_block = ConversationHandler(
        entry_points=[CommandHandler('block', start_blocking)],
        states={
            1: [MessageHandler(Filters.text, finish_blocking)],

        },
        fallbacks=[MessageHandler(Filters.text, start)]
    )

    dialog_transfer = ConversationHandler(
        entry_points=[CommandHandler('transfer', enter_addressee_name)],
        states={
            1: [MessageHandler(Filters.text, enter_amount)],
            2: [MessageHandler(Filters.text, send_money)],
        },
        fallbacks=[MessageHandler(Filters.text, start)]
    )



    dispatcher.add_handler(dialog_start)
    dispatcher.add_handler(dialog_block)
    dispatcher.add_handler(dialog_transfer)



    text_handler = MessageHandler(Filters.text, stream)

    # Регистрируем обработчик в диспетчере.
    dispatcher.add_handler(text_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
