import telebot
from telebot import types

import config
import database as db
import markups as mkup

bot = telebot.TeleBot(config.token)

# Get user status from database
def user_status(chatid):
    status = db.get_data("users", "status", "chatid={}".format(str(chatid)))
    if len(status) == 0:
        return None
    else:
        return status[0][0]


# Register a new user
def user_registration(message, first_time=False):
    bot.send_message(message.chat.id, mkup.start_phrase if first_time else mkup.repeat_start_phrase,
                     reply_markup=mkup.start_keyboard, parse_mode="markdown")

@bot.message_handler(func=lambda message: (message.content_type == 'text'))
def all_messages(message):
    status = user_status(message.chat.id)

    if status is None:
        if message.text == "/start":
            user_registration(message, first_time=True)
        else:
            user_registration(message)

    elif status == "student":
        pass
    elif status == "teacher":
        pass
    elif status == "admin":
        pass


@bot.callback_query_handler(func=lambda c: True)
def all_inlines(c):
    if c.data == ("reg_student"):
        if user_status(c.message.chat.id) is not None:
            bot.send_message(c.message.chat.id, "Вы уже зарегистрировались!")
            return 0
        try:
            bot.edit_message_text(text=mkup.student_class_selection, chat_id=c.message.chat.id,
                                  message_id=c.message.message_id, reply_markup=mkup.student_preclasses_keyboard)
        except:
            bot.send_message(c.message.chat.id, mkup.student_class_selection,
                             reply_markup=mkup.student_preclasses_keyboard)

    elif c.data.startswith("preclass_"):
        class_num = c.data.split("preclass_")[1]
        kb = types.InlineKeyboardMarkup(row_width=2)
        mkup.dict_to_kb(kb, mkup.student_classes_buttons[class_num])
        if user_status(c.message.chat.id) is not None:
            bot.send_message(c.message.chat.id, "Вы уже зарегистрировались!")
            return 0
        try:
            bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id, reply_markup=kb)
        except:
            bot.send_message(c.message.chat.id, "Выбери свой класс!",
                             reply_markup=kb)

    elif c.data.startswith("class_"):
        class_full = c.data.split("class_")[1]
        db.insert_data("users", [c.message.chat.id, "student", class_full])
        try:
            bot.edit_message_text(text=mkup.welcome_message, chat_id=c.message.chat.id,
                                  message_id=c.message.message_id, reply_markup=None)
            bot.send_message(c.message.chat.id, mkup.welcome_help, reply_markup=mkup.student_menu,
                             parse_mode="markdown")
        except:
            bot.send_message(c.message.chat.id, mkup.welcome_message, reply_markup=mkup.student_menu)
            bot.send_message(c.message.chat.id, mkup.welcome_help, parse_mode="markdown")


# Constant polling

if __name__ == '__main__':
    bot.polling(none_stop=True)