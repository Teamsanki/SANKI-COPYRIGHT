from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters
from pyrogram.types import Message
import time
import psutil
import platform
import logging
from config import OWNER_ID, BOT_USERNAME
from config import *
from SANKIRIGHT import SANKIRIGHT as app

import pyrogram
from pyrogram.errors import FloodWait


# ----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------


start_txt = """<b> 🤖 sᴀɴᴋɪxᴅ sᴇᴄᴜʀɪᴛʏ ʀᴏʙᴏᴛ 🛡️ </b>

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ #sᴀɴᴋɪxᴅ ɢʀᴏᴜᴘ sᴇᴄᴜʀɪᴛʏ ʀᴏʙᴏᴛ, ʏᴏᴜʀ ᴠɪɢɪʟᴀɴᴛ ɢᴜᴀʀᴇɪɴ ɪɴ ᴛʜɪs ᴛᴇʟᴇɢʀᴀᴍ sᴘᴀᴄᴇ! ᴏᴜʀ ᴍɪssɪᴏɴ ɪs ᴛᴏ ᴇɴsᴜʀᴇ ᴀ sᴇᴄᴜʀᴇ ᴀɴᴅ ᴘʟᴇᴀsᴀɴᴛ ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ ғᴏʀ ᴇᴠᴇʀʏᴏɴᴇ. ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ᴘʀᴏᴛᴇᴄᴛ𝂢ɪᴏɴ ᴛᴏ ᴍᴀɪɴᴛᴀɪɴɪɴɢ ᴅᴇᴄᴏʀᴜᴍ, ᴡᴇ'ᴠᴇ ɢᴏᴛ ɪᴛ ᴄᴏᴠᴇʀᴇᴅ.

ғᴇᴇʟ ғʀᴇᴇ ᴛᴏ ʀᴇᴘᴏʀᴛ ᴀɴʏ ᴄᴏɴᴄᴇʀɴs, ᴀɴᴅ ʟᴇᴛ's ᴡᴏʀᴋ ᴛᴏɢᴇᴛʜᴇʀ ᴛᴏ ᴍᴀᴋᴇ ᴛʜɪs ᴄᴏᴍᴍᴜɴɪᴛʏ ᴛʜʀɪᴠᴇ! 🤝🔐 """


@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴀɴᴅʟᴇʀ •", callback_data="sanki_back")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/72f0c77e4987f9caa46de-4fd6305ce614367c45.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


gd_buttons = [              
        [
            InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id=OWNER_ID),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/Teamsankinetworkk"),    
        ]
        ]


# ------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("sanki_back"))
async def sanki_back(_, query: CallbackQuery):
    await query.message.edit_caption(start_txt,
                                    reply_markup=InlineKeyboardMarkup(gd_buttons),)
        

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


start_time = time.time()

def time_formatter(milliseconds: float) -> str:
    seconds , milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"

@app.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"➪ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"➪ᴄᴘᴜ: {cpu}%\n"
        f"➪ꜱᴛᴏʀᴀɢᴇ: {size_formatter(storage.total)} [ᴛᴏᴛᴀʟ]\n"
        f"➪{size_formatter(storage.used)} [ᴜsᴇᴅ]\n"
        f"➪{size_formatter(storage.free)} [ғʀᴇᴇ]\n"
        f"➪ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: {python_version},"
    )

    await message.reply(reply_text, quote=True)

FORBIDDEN_KEYWORDS = [
    "porn", "xxx", "sex", "NCERT", "XII", "page", "Ans", "meiotic", 
    "divisions", "System.in", "Scanner", "void", "nextInt", 
    "madhrchod", "randi", "lund", "land", "lawda", "betichod", 
    "chutiya", "gand", "lula"
]

@app.on_message()
async def handle_message(client, message):
    try:
        # Check if the message has text
        if hasattr(message, 'text') and any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
            logging.info(f"Deleting message with ID {message.id}")
            await message.delete()
            await message.reply_text(f"@{message.from_user.username} ᴡʜʏ ʏᴏᴜ ᴜsɪɴɢ ʟɪᴋᴇ ᴛʜɪs ᴡᴏʀᴅ ᴅᴏɴ'ᴛ ᴅᴏ ɴᴇxᴛ ᴛɪᴍᴇ ᴏᴋʏ! ɪғ ʏᴏᴜ ᴅᴏ ᴀɢᴀɪɴ ᴀᴅᴍɪɴs ɢɪᴠᴇs ʏᴏᴜ ʙᴀɴ.")
        
        # Check if the message has a caption
        elif hasattr(message, 'caption') and any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
            logging.info(f"Deleting message with ID {message.id}")
            await message.delete()
            await message.reply_text(f"@{message.from_user.username} ᴡʜʏ ʏᴏᴜ ᴜsɪɴɢ ʟɪᴋᴇ ᴛʜɪs ᴡᴏʀᴅ ᴅᴏɴ'ᴛ ᴅᴏ ɴᴇxᴛ ᴛɪᴍᴇ ᴏᴋʏ! ɪғ ʏᴏᴜ ᴅᴏ ᴀɢᴀɪɴ ᴀᴅᴍɪɴs ɢɪᴠᴇs ʏᴏᴜ ʙᴀɴ.")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()

def delete_long_messages(_, m):
    return len(m.text.split()) > 10

@app.on_message(filters.group & filters.private & delete_long_messages)
async def delete_and_reply(_, msg):
    await msg.delete()
    user_mention = msg.from_user.mention
    await app.send_message(msg.chat.id, f"Hey {user_mention}, please keep your messages short!")

@app.on_message(filters.animation | filters.audio | filters.document | filters.photo | filters.sticker | filters.video)
async def keep_reaction_message (client, message: Message):
    pass 

async def delete_pdf_files(client, message):
    if message.document and message.document.mime_type == "application/pdf":
        warning_message = f"@{message.from_user.username} I ʜᴀᴠᴇ ᴅᴇʟᴇᴛᴇᴅ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ,\n ʙᴇᴄᴀᴜsᴇ ʏᴏᴜ ᴡᴇʀᴇ ᴀʙᴜsɪɴɢ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴀɴᴅ I ᴡɪʟʟ ɴᴏᴛ ʟᴇᴛ ᴛʜɪs ʜᴀᴘᴘᴇɴ\n\n ʙᴇᴄᴀᴜsᴇ ɪᴛ ᴄᴀɴ ᴀʟsᴏ ʙᴇ ᴄᴏᴘʏʀɪɢʜᴛᴇᴅ.\n\n Mᴀᴅᴇ Bʏ @TSGCODER 🥀"
        await message.reply_text(warning_message)
        await message.delete()
    else:  
        pass

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_pdf_files(client, message)
