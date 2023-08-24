import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from TxcMusic import LOGGER, app, userbot
from TxcMusic.core.call import Txc
from TxcMusic.plugins import ALL_MODULES
from TxcMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("TxcMusic").error("Add Pyrogram string session and then try...")
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
        importlib.import_module("TxcMusic.plugins" + all_module)
    LOGGER("TxcMusic.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Txc.start()
    try:
        await Txc.stream_call("https://telegra.ph/file/a1c776f377ac1200e4221.mp4")
    except NoActiveGroupCall:
        LOGGER("TxcMusic").error(
            "[ERROR] - \n\nTurn on group voice chat and don't put it off otherwise I'll stop working thanks."
        )
        sys.exit()
    except:
        pass
    awaitAlexa.decorators()
    LOGGER("AlexaMusic").info("Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("AlexaMusic").info("Stopping Music Bot")
