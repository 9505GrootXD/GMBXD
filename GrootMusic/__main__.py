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
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
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
    LOGGER("GrootMusic.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Groot.start()
    try:
        await Groot.stream_call("https://te.legra.ph/file/07c786fb2835ab46e0439.jpg")
    except NoActiveGroupCall:
        LOGGER("GrootMusic").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Groot.decorators()
    LOGGER("GrootMusic").info("Music Bot Started Successfully ❣️")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("GrootMusic").info("Stopping Music Bot, Bhakk Bhosdike (Gaand Maraa Tu)")
