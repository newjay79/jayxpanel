import os
import asyncio
import sys
import git
import heroku3
# Changed root to JAYXPANEL
from JayXSpamBot import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9
from JayXSpamBot import OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, deadlyversion
from JayXSpamBot import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
# alive Pic By Default It's Will Show Our
from JayXSpamBot import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

DOLL_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/0a90b9ca23989258de472.jpg"


DOLL = "✯ 𝙅𝘼𝙔 ✘ 𝙎𝙥𝙖𝙢 𝙃𝙀𝙍𝙀 ✯\n\n"
DOLL += f"**𝐘𝐨𝐮𝐫 𝐃𝐚𝐝 𝐈𝐬 𝐂𝐨𝐦𝐢𝐧𝐠 𝐅𝐮𝐜𝐤 𝐘𝐨𝐮 𝐇𝐚𝐭𝐞𝐫𝐬 😈🚨**\n"
DOLL += f"━───────╯•╰───────━\n"
DOLL += f"• **𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽** : `3.10.1`\n"
DOLL += f"• **𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽** : `{version.__version__}`\n"
DOLL += f"• **𝙅𝘼𝙔 𝙓 𝙎𝘼𝙋𝙈 𝙃𝙀𝙍𝙀 𝚅𝙴𝚁𝚂𝙸𝙾𝙽**  : `{deadlyversion}`\n"
DOLL += f"• **ᴄʜᴀɴɴᴇʟ** : [Join.](https://t.me/Officialjay_store)\n"
DOLL += f"• **Source Code** : [•Repo•](https://t.me/Officialjay_store)\n"
DOLL += f"━───────╮•╭───────━\n\n"   
                                  
@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sdoll(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await BOT0.send_file(event.chat_id,
                                  DOLL_PIC,
                                  caption=DOLL,
                                  buttons=[
        [
        Button.url("☺️ᴄʜᴀɴɴᴇʟ☺️", "https://t.me/Officialjay_store"),
        Button.url("🇮🇳sᴜᴘᴘᴏʀᴛ🇮🇳", "https://t.me/Officialjay_store")
        ],
        [
        Button.url("• 🙂ʀᴇᴘᴏ🙂 •", "https://t.me/Officialjay_store")
        ]
        ]
        )
