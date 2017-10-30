from telebot import types


def dict_to_kb(keyboard, buttons, row_size=2):
    """
    Adds buttons to inline keyboard

    :param keyboard: inline keyboard
    :type keyboard: types.InlineKeyboardMarkup object

    :param buttons: buttons to be added
    :type buttons: dict

    :param row_size: size of buttons row
    :type row_size: int
    """

    tmp=[]

    for item in buttons.items():
        tmp.append(types.InlineKeyboardButton(text=item[0], callback_data=item[1]))
        if len(tmp) == row_size:
            keyboard.row(*tmp)
            tmp = []
    keyboard.row(*tmp)


# First log-in
start_phrase = "Вас приветствует *Помощник Гимназиста* {}\nДавайте знакомиться!".format(
    chr(0x1F916))
start_keyboard = types.InlineKeyboardMarkup()
start_buttons = {"Я ученик {}".format(chr(0x1F609)): "reg_student",
                 "Я учитель {}".format(chr(0x1F60F)): "reg_teacher"
                 }
dict_to_kb(start_keyboard, start_buttons)
repeat_start_phrase = "Чтобы помочь вам, мне нужно узнать, кто вы {}\nВыберите одну из кнопок!".format(chr(0x1F636))


# Student registration
student_class_selection = "Супер {}\nТеперь выбери свой класс!".format(chr(0x1F60B))
student_preclasses_buttons = {"5" : "preclass_5", "6" : "preclass_6", "7" : "preclass_7", "8":"preclass_8",
                           "9" : "preclass_9", "10" : "preclass_10", "11" : "preclass_11"
                           }
student_preclasses_keyboard = types.InlineKeyboardMarkup(row_width=2)
dict_to_kb(student_preclasses_keyboard, student_preclasses_buttons)

student_classes_buttons = {
    "5" : {"5а" : "class_5a", "5б" : "class_5b", "5в" : "class_5c", "5г" : "class_5d"},
    "6" : {"6а" : "class_6a", "6б" : "class_6b", "6в" : "class_6c", "6г" : "class_6d"},
    "7" : {"7а" : "class_7a", "7б" : "class_7b", "7в" : "class_7c", "7г" : "class_7d"},
    "8" : {"8а" : "class_8a", "8б" : "class_8b", "8в" : "class_8c", "8г" : "class_8d"},
    "9" : {"9а" : "class_9a", "9б" : "class_9b", "9в" : "class_9c", "9г" : "class_9d"},
    "10" : {"10.1" : "class_101", "10.2" : "class_102", "10.3" : "class_103", "10.4" : "class_104",
            "10.5": "class_105", "10.6" : "class_106"},
    "11" : {"11.1" : "class_111", "11.2" : "class_112", "11.3" : "class_113", "11.4" : "class_114"}
}

welcome_message = "Добро пожаловать {}".format(chr(0x1F389))
welcome_help = "*Расписание* {} - здесь можно посмотреть актуальное расписание уроков на день и на неделю\n\n" \
               "*Новости* {} - новости Школы Глория\n\n" \
               "*Дневник* {} - авторизовавшись в Электронном Дневнике, здесь можно смотреть свои оценки и домашние задания\n\n" \
               "*Контакты* {} - здесь можно связаться с создателем Помощника Гимназиста" \
               "".format(chr(0x1F554), chr(0x1F4F0), chr(0x1F4DD), chr(0x1F4DE))

student_menu = types.ReplyKeyboardMarkup()
student_menu_buttons = ["Расписание {}".format(chr(0x1F554)), "Новости {}".format(chr(0x1F4F0)),
                        "Дневник {}".format(chr(0x1F4DD)), "Контакты {}".format(chr(0x1F4DE))]
student_menu.row(student_menu_buttons[0], student_menu_buttons[1])
student_menu.row(student_menu_buttons[2], student_menu_buttons[3])

contacts = "Спасибо, что пользуетесь *Помощником Гимназиста!*\n" \
           "Связаться со мной можно:\n\n" \
           "*Telegram:* @LifetimeAlone\n" \
           "*Vk:* https://vk.com/pois0n\n\n" \
           "{}".format(chr(0x1F31A))