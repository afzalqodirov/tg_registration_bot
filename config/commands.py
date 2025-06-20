from aiogram.types import BotCommand, KeyboardButton, ReplyKeyboardMarkup

custom_commands = [
    BotCommand(command='start', description='(re)start the bot'),
    BotCommand(command='register', description='register to add category/product to the store'),
    BotCommand(command='add_category', description='add new category'),
    BotCommand(command='list_categories', description='returns a list of categories'),
    BotCommand(command='list_products', description='returns a list of a product'),
    BotCommand(command='add_product', description='add a new product'),
    BotCommand(command='search_category', description='search a category'),
]
phone_markup = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Send phone number',request_contact=True)]],
    resize_keyboard=True,
    one_time_keyboard=True,
    )