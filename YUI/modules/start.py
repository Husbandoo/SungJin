from pyrogram.types import Message
from pyrogram import filters
from YUI import pgram

START_VID = "https://telegra.ph/file/2ddc15125fe6d1cd1b6fc.mp4"
PM_START_TEXT = """
*Kᴏɴɪᴄʜɪᴡᴀ {},*
*I'ᴍ Yᴜɪɢᴀʜᴀᴍᴀ Yᴜɪ, A Aɴɪᴍᴇ Tʜᴇᴍᴇᴅ Gʀᴏᴜᴘ Mᴀɴᴀɢᴇᴍᴇɴᴛ Bᴏᴛ.*
➖➖➖➖➖➖➖➖➖➖➖➖➖
❍ *Uᴘᴛɪᴍᴇ:* {}
❍ *Oᴡɴᴇʀ:* {OWNER_USERNAME}
➖➖➖➖➖➖➖➖➖➖➖➖➖
*Hɪᴛ Tʜᴇ /help Tᴏ Gᴇᴛ Lɪsᴛ Oғ Mʏ Cᴏᴍᴍᴀɴᴅs.××*
"""

@pgram.on_message(filters.command("start") && filters.private)
async def start(_, message):
   await message.reply_video(START_VID , PM_START_TEXT)
