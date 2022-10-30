# GROOT MUSIC NETWORK
# G-Network Music Projects
# Copyright (C) 2022 By @Groot_Network
# Copy Rights @RJbr0 , @MyNameIsGROOT
# Don't Any Value In This Repo If You Edit Your Github Will Get Banned 😌

from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from GrootMusic import app
from GrootMusic.core.call import Groot
from GrootMusic.utils import bot_sys_stats
from GrootMusic.utils.decorators.language import language

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND) & filters.group & ~filters.edited & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Groot.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping)
    )
