from JayXSpamBot import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from JayXSpamBot import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/0a90b9ca23989258de472.jpg"

DOLL_Help = "🔥 𝙅𝘼𝙔 ✘ 𝙎𝙥𝙖𝙢 𝘽𝙤𝙩 🔥\n\n"

DOLL_Help = "**𝐘𝐨𝐮𝐫 𝐃𝐚𝐝 𝐈𝐬 𝐂𝐨𝐦𝐢𝐧𝐠 𝐅𝐮𝐜𝐤 𝐘𝐨𝐮 𝐇𝐚𝐭𝐞𝐫𝐬 😈🚨**\n"
 
DOLL_Help += f"__ᴄᴍɴᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ 𝙅𝘼𝙔 ✘ sᴘᴀᴍ ʙᴏᴛ__\n\n"

DOLL_Help += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

DOLL_Help += f" `!ping` - to check ping\n `!alive` , `!doll` - to check bot alive/version (only main userbot will reply)\n\n !`restart` - to restart all spam bots \n\n `!addecho` - to addecho \n\n `!rmecho` - To remove Echo \n\n `!addsudo` - To add sudo user using spam bot \n\n"
 
DOLL_Help += f" ↧ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳 ↧\n\n"

DOLL_Help += f" `!leave` - to leave public/private channel/groups\n\n"
 
DOLL_Help += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

DOLL_Help += f" `!raid` - to raid\n `!replyraid` - to active reply raid\n\n `!dreplyraid` - to de-active reply raid\n\n `!spam` - this cmd use for Normal spam\n `!bigspam` - this cmd use for big spam\n\n `!uspam` - this cmd use for unlimited Spam until You restart the bots!!\n\n `!delayspam` - this cmd use for delay spam\n\n"

DOLL_Help += f" `!pornspam` - ɪ ᴡɪʟʟ ꜱᴜɢɢᴇꜱᴛ ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ😂 ↧\n\n"

DOLL_Help += f" `!hang` - 😂 ↧\n\n"

DOLL_Help += f" `!bspam` - 𝗕𝗜𝗥𝗧𝗛𝗗𝗔𝗬 𝗦𝗣𝗔𝗠🥵 ↧\n\n"

DOLL_Help += f"© @OFFICIALJAY79\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=JAY_Help,
                                  buttons=[
        [
        Button.url("☺️ᴄʜᴀɴɴᴇʟ☺️", "https://t.me/Officialjay_store")
        ] 
        ]
        )
