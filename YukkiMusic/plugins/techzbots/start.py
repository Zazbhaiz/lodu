from config import START_IMG_URL as THUMBNAIL
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from pyrogram import filters
from YukkiMusic.plugins.techzbots.strings import *
from strings.helpers import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def start_menu_private(message):
    mention = "[" + message.from_user.first_name + "](tg://user?id=" + str(message.from_user.id) + ")"
    text = START_TEXT.replace("MENTION",mention)
    if "help" in message.text:
        await message.reply_photo(photo=THUMBNAIL,caption="**Choose Basic Command to get Basic Bot Commands\nAnd Advanved Command to get Advanved Bot Commands.**",reply_markup=COMMAND_MENU_BUTTON,parse_mode="markdown")
    else:
        await message.reply_photo(photo=THUMBNAIL,caption=text,reply_markup=START_BUTTON_PRIVATE,parse_mode="markdown")

async def start_menu_group(message):
    mention = "[" + message.from_user.first_name + "](tg://user?id=" + str(message.from_user.id) + ")"
    text = START_TEXT.replace("MENTION",mention)
    if "help" in message.text:
        await message.reply_photo(photo=THUMBNAIL,caption="**Choose A Help Menu From Given Below**",reply_markup=COMMAND_MENU_BUTTON,parse_mode="markdown")
    else:
        await message.reply_photo(photo=THUMBNAIL,caption=text,reply_markup=START_BUTTON_GROUP,parse_mode="markdown")

@app.on_callback_query(filters.regex("advanced_cmd"))
async def commands_menu(_, query):
    await query.answer()
    mention = "[" + query.from_user.first_name + "](tg://user?id=" + str(query.from_user.id) + ")"
    text = COMMANDS_TEXT.replace("MENTION",mention)
    if (query.from_user.id in SUDOERS):
        buttons = COMMANDS_BUTTON_SUDO
    else:
        buttons = COMMANDS_BUTTON_USER
    await query.message.edit(text=text,reply_markup=buttons)

@app.on_callback_query(filters.regex("admin_cmd"))
async def admin_menu(_, query):
    await query.answer()    
    await query.message.edit(text=ADMIN_TEXT,reply_markup=BACK_BUTTON,parse_mode="markdown")

@app.on_callback_query(filters.regex("auth_cmds"))
async def auth_cmds(_, query):
    await query.answer()    
    await query.message.edit(text=AUTH_TEXT,reply_markup=AUTH_BACK_BUTTON,parse_mode="markdown")

@app.on_callback_query(filters.regex("play_cmd"))
async def play_menu(_, query):
    await query.answer()    
    await query.message.edit(text=PLAY_TEXT,reply_markup=BACK_BUTTON,parse_mode="markdown")

@app.on_callback_query(filters.regex("bot_cmd"))
async def bot_menu(_, query):
    await query.answer()    
    await query.message.edit(text=BOT_TEXT,reply_markup=BACK_BUTTON,parse_mode="markdown")
    
    
    
@app.on_callback_query(filters.regex("admin"))
async def admin(_, query):
    await query.answer()    
    await query.message.edit(text=ADMIN,reply_markup=ZAZ,parse_mode="markdown")

@app.on_callback_query(filters.regex("misc"))
async def misc(_, query):
    await query.answer()    
    await query.message.edit(text=MISC,reply_markup=ZAZ,parse_mode="markdown")

@app.on_callback_query(filters.regex("animal"))
async def animal(_, query):
    await query.answer()    
    await query.message.edit(text=ANIMAL,reply_markup=ZAZ,parse_mode="markdown")

@app.on_callback_query(filters.regex("anime"))
async def anime(_, query):
    await query.answer()    
    await query.message.edit(text=ANIME,reply_markup=ZAZ,parse_mode="markdown")

@app.on_callback_query(filters.regex("picks"))
async def picks(_, query):
    await query.answer()    
    await query.message.edit(text=PICKS,reply_markup=ZAZ,parse_mode="markdown")

@app.on_callback_query(filters.regex("anti"))
async def anti(_, query):
    await query.answer()    
    await query.message.edit(text=ANTI,reply_markup=ZAZ,parse_mode="markdown")

@app.on_callback_query(filters.regex("crick"))
async def crick(_, query):
    await query.answer()    
    await query.message.edit(text=CRICK,reply_markup=ZAZ,parse_mode="markdown")

@app.on_callback_query(filters.regex("couple"))
async def couple(_, query):
    await query.answer()    
    await query.message.edit(text=COUPLE,reply_markup=ZAZ,parse_mode="markdown")

@app.on_callback_query(filters.regex("chat"))
async def chat(_, query):
    await query.answer()    
    await query.message.edit(text=CHAT,reply_markup=ZAZ,parse_mode="markdown")

@app.on_callback_query(filters.regex("cats"))
async def cats(_, query):
    await query.answer()    
    await query.message.edit(text=CATS,reply_markup=ZAZ,parse_mode="markdown")

@app.on_callback_query(filters.regex("black"))
async def black(_, query):
    await query.answer()    
    await query.message.edit(text=BLACK,reply_markup=ZAZ,parse_mode="markdown")\

@app.on_callback_query(filters.regex("blackc"))
async def blackc(_, query):
    await query.answer()    
    await query.message.edit(text=BLACKC,reply_markup=ZAZ,parse_mode="markdown")

@app.on_callback_query(filters.regex("next1"))
async def next1(_, query):
    await query.answer()    
    await query.message.edit(text=BASIC_TEXT,reply_markup=NEXT1,parse_mode="markdown")

@app.on_callback_query(filters.regex("crypto"))
async def crypto(_, query):
    await query.answer()    
    await query.message.edit(text=CRYPTO,reply_markup=ZAZ1,parse_mode="markdown")
    
@app.on_callback_query(filters.regex("misc1"))
async def misc1(_, query):
    await query.answer()    
    await query.message.edit(text=MISC1,reply_markup=ZAZ1,parse_mode="markdown")

@app.on_callback_query(filters.regex("dice"))
async def dice(_, query):
    await query.answer()    
    await query.message.edit(text=DICE,reply_markup=ZAZ1,parse_mode="markdown")

@app.on_callback_query(filters.regex("filter"))
async def filter(_, query):
    await query.answer()    
    await query.message.edit(text=FILTER,reply_markup=ZAZ1,parse_mode="markdown")

@app.on_callback_query(filters.regex("flood"))
async def flood(_, query):
    await query.answer()    
    await query.message.edit(text=FLOOD,reply_markup=ZAZ1,parse_mode="markdown")

@app.on_callback_query(filters.regex("greet"))
async def greet(_, query):
    await query.answer()    
    await query.message.edit(text=GREET,reply_markup=ZAZ1,parse_mode="markdown")

@app.on_callback_query(filters.regex("info"))
async def info(_, query):
    await query.answer()    
    await query.message.edit(text=INFO,reply_markup=ZAZ1,parse_mode="markdown")

@app.on_callback_query(filters.regex("karma"))
async def karma(_, query):
    await query.answer()    
    await query.message.edit(text=KARMA,reply_markup=ZAZ1,parse_mode="markdown")

@app.on_callback_query(filters.regex("lock"))
async def lock(_, query):
    await query.answer()    
    await query.message.edit(text=LOCK,reply_markup=ZAZ1,parse_mode="markdown")

@app.on_callback_query(filters.regex("notes"))
async def notes(_, query):
    await query.answer()    
    await query.message.edit(text=NOTES,reply_markup=ZAZ1,parse_mode="markdown")

@app.on_callback_query(filters.regex("music"))
async def music(_, query):
    await query.answer()    
    await query.message.edit(text=MUSIC,reply_markup=ZAZ1,parse_mode="markdown")


@app.on_callback_query(filters.regex("close_btn"))
async def closer_menu(_, query):
    await query.answer()    
    await query.message.delete()

@app.on_callback_query(filters.regex("open_start_menu"))
async def open_start_menu(_, query):
    await query.answer()
    if query.message.chat.type == "group":
        button = START_BUTTON_GROUP
    elif query.message.chat.type == "supergroup":
        button = START_BUTTON_GROUP
    elif query.message.chat.type == "private":
        button = START_BUTTON_PRIVATE

    mention = "[" + query.from_user.first_name + "](tg://user?id=" + str(query.from_user.id) + ")"
    text = START_TEXT.replace("MENTION",mention)
    await query.message.edit(text=text,reply_markup=button,parse_mode="markdown")
    
    
@app.on_callback_query(filters.regex("basic_cmd"))
async def basic_cmd(_, query): 
    await query.answer()   
    await query.message.edit(text=BASIC_TEXT,reply_markup=BASIC_BACK_BUTTON,parse_mode="markdown")    
    
    
    
@app.on_callback_query(filters.regex("command_menu"))
async def command_menu(_, query):
    await query.answer()   
    await query.message.edit(text="**Choose One To Get Help For.**",reply_markup=COMMAND_MENU_BUTTON,parse_mode="markdown")  

