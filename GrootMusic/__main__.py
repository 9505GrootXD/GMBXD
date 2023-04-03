# GROOT MUSIC NETWORK
# G-Network Music Projects
# Copyright (C) 2022 By @Groot_Network
# Copy Rights @RJbr0 , @MyNameIsGROOT
# Don't Any Value In This Repo If You Edit Your Github Will Get Banned 😌

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from GrootMusic import LOGGER, app, userbot
from GrootMusic.core.call import Groot
from GrootMusic.plugins import ALL_MODULES
from GrootMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("GrootMusic").error(
            "ᴡʜᴀᴛ ᴘɪʀᴏ.! ᴀᴛʟᴇᴀsᴛ ᴀᴅᴅ ᴀ ᴘʏʀᴏɢʀᴀᴍ sᴛʀɪɴɢ, ʜᴏᴡ ᴄʜᴇᴀᴘ.. 😒"
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("GrootMusic.plugins" + all_module)
    LOGGER("GrootMusic.plugins").info("ɴᴇᴄᴇssᴀʀʏ ᴍᴏᴅᴜʟᴇs ɪᴍᴘᴏʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ. 😌")
    await userbot.start()
    await Groot.start()
    try:
        await Groot.stream_call("https://te.legra.ph/file/07c786fb2835ab46e0439.jpg")
    except NoActiveGroupCall:
        LOGGER("GrootMusic").error(
            "[ERROR] - \n\n😎 ʜᴇʏ ᴍᴏᴏᴅᴇʟ, ғɪʀsᴛʟʏ ᴏᴘᴇɴ ᴛᴇʟᴇɢʀᴀᴍ ᴀɴᴅ ᴛᴜʀɴ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ,ɪғ ʏᴏᴜ ᴇᴠᴇʀ ᴇɴᴅᴇᴅ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪ ᴡɪʟʟ sᴛᴏᴘ ᴡᴏʀᴋɪɴɢ ᴀɴᴅ ᴍᴇᴍʙᴇʀs ᴡɪʟʟ ᴘᴜᴍᴋ ʏᴏᴜ ᴜᴘ.😂"
        )
        sys.exit()
    except:
        pass
    await Groot.decorators()
    LOGGER("GrootMusic").info("🌱 ɢʀᴏᴏᴛ ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ 🤨")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("GrootMusic").info("😏 sᴛᴏᴘᴘɪɴɢ ɢʀᴏᴏᴛ ᴍᴜsɪᴄ ʙᴏᴛ 😒")
