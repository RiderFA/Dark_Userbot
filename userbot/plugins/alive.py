"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`𝔏𝔦𝔳𝔢 𝔞𝔰 𝔦𝔣 𝔶𝔬𝔲 𝔴𝔢𝔯𝔢 𝔱𝔬 𝔡𝔦𝔢 𝔱𝔬𝔪𝔬𝔯𝔯𝔬𝔴. 𝔏𝔢𝔞𝔯𝔫 𝔞𝔰 𝔦𝔣 𝔶𝔬𝔲 𝔴𝔢𝔯𝔢 𝔱𝔬 𝔩𝔦𝔳𝔢 𝔣𝔬𝔯𝔢𝔳𝔢𝔯.👍ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴍʏ ᴍᴀꜱᴛᴇʀ🎈🎈`**\n\n"
                     "**✅Telethon version:- 6.9.0**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**✅Python: 3.7.3**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n"
                     "**✅Bot Made By:- @from userbot import *
from userbot.utils import *
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Darkbot User"

ludosudo = Config.SUDO_USERS
if ludosudo:

    sudou = "True"

else:
    sudou = "False"
    
dark = bot.uid

PM_IMG = "https://telegra.ph/file/c2f484ff3ddd53d752dcd.mp4"

pm_caption = "__**🤘『 ÐΛR̷Ꮶ 』★BØT★ ɨz օռʟɨռɛ🤘**__\n\n"

pm_caption += (
    f"           𖤍M͜͡Y͜͡ B͜͡O͜͡S͜͡S͡𖤍\n**『🔥[{DEFAULTUSER}](tg://user?id={dark})🔥』**\n\n"
)



pm_caption += f"🔥**『 ÐΛR̷Ꮶ 』★BØT★🔥  : 1.0** \n\n"

pm_caption += f" ** ⚔️𝕋𝔼𝕃𝔼𝕋ℍ𝕆ℕ 𝕍𝔼ℝ𝕊𝕀𝕆ℕ ⚔️  : 6.9.0 ** \n\n"



pm_caption += "**⭐𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝕊𝕋𝔸𝕋𝕌𝕊⭐ :- 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝕎𝕆ℝ𝕂𝕀ℕ𝔾 ℕ𝕆ℝ𝕄𝔸𝕃𝕃𝕐 **✅\n\n◆"


pm_caption +=  "**⭕ℂℍ𝔸ℕℕ𝔼𝕃⭕    : [ᴊᴏɪɴ](https://t.me/Dark_bot_support)**\n\n" 



pm_caption += "**⭐ℂℝ𝔼𝔸𝕋𝕆ℝ ⭐: [ ʜᴀʀsʜ ʜᴇʀᴇ](https://t.me/harsh_78)**\n\n"

pm_caption +=  "[☠️ᴅᴀʀᴋ ʙᴏᴛ ʀᴇᴘᴏ ☠️ ](https://github.com/Harsh-78/Dark_Userbot)\n "    


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()
\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**"
                     "**✅Database Status: Databases functioning normally!**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n💞Always with you, my peru master!\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n"
                     "[Deploy this userbot Now](https://github.com/Harsh-78/Dark_Userbot)")
from userbot import *

from userbot.utils import *

from telethon.events import NewMessage

from telethon.tl.custom import Dialog

from telethon.tl.types import Channel, Chat, User





DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Darkbot User"



ludosudo = Config.SUDO_USERS

if ludosudo:



    sudou = "True"



else:

    sudou = "False"

    

dark = bot.uid



PM_IMG = "https://telegra.ph/file/c2f484ff3ddd53d752dcd.mp4"



pm_caption = "__**🤘『 ÐΛR̷Ꮶ 』★BØT★ ɨz օռʟɨռɛ🤘**__\n\n"



pm_caption += (

    f"           𖤍M͜͡Y͜͡ B͜͡O͜͡S͜͡S͡𖤍\n**『🔥[{DEFAULTUSER}](tg://user?id={dark})🔥』**\n\n"

)







pm_caption += f"🔥**『 ÐΛR̷Ꮶ 』★BØT★🔥  : 1.0** \n\n"



pm_caption += f" ** ⚔️𝕋𝔼𝕃𝔼𝕋ℍ𝕆ℕ 𝕍𝔼ℝ𝕊𝕀𝕆ℕ ⚔️  : 6.9.0 ** \n\n"







pm_caption += "**⭐𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝕊𝕋𝔸𝕋𝕌𝕊⭐ :- 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝕎𝕆ℝ𝕂𝕀ℕ𝔾 ℕ𝕆ℝ𝕄𝔸𝕃𝕃𝕐 **✅\n\n◆"





pm_caption +=  "**⭕ℂℍ𝔸ℕℕ𝔼𝕃⭕    : [ᴊᴏɪɴ](https://t.me/Dark_bot_support)**\n\n" 







pm_caption += "**⭐ℂℝ𝔼𝔸𝕋𝕆ℝ ⭐: [ ʜᴀʀsʜ ʜᴇʀᴇ](https://t.me/harsh_78)**\n\n"



pm_caption +=  "[☠️ᴅᴀʀᴋ ʙᴏᴛ ʀᴇᴘᴏ ☠️ ](https://github.com/Harsh-78/Dark_Userbot)\n "    





@bot.on(admin_cmd(outgoing=True, pattern="alive$"))

async def amireallyalive(alive):

    await alive.get_chat()

    await alive.delete()

    """ For .alive command, check if the bot is running.  """

    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)

    await alive.delete()
