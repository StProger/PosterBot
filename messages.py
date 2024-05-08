from pyrogram import Client, enums

import config


async def send_message_zelenka(app: Client):
    try:
        async with app:

            await app.send_photo(
                chat_id=config.ZELENKA,
                caption=config.message_zelenka,
                photo=config.BANNER_ID,
                parse_mode=enums.ParseMode.HTML
            )
    except:
        pass


async def send_message_scrouge(app: Client):
    try:
        async with app:
            await app.send_photo(
                chat_id=config.SCROUGE,
                caption=config.message_scrouge,
                photo=config.BANNER_ID,
                parse_mode=enums.ParseMode.HTML
            )
    except:
        pass


async def send_message_kiwi(app: Client):

    try:
        async with app:
            await app.send_photo(
                chat_id=config.KIWI,
                caption=config.message_kiwi,
                photo=config.BANNER_ID,
                parse_mode=enums.ParseMode.HTML
            )
    except:
        pass


async def send_other(app: Client):
    try:
        async with app:
            await app.send_photo(
                chat_id=config.OTC,
                caption=config.other_message,
                photo=config.BANNER_ID,
                parse_mode=enums.ParseMode.HTML
            )

            await app.send_photo(
                chat_id=config.DARK_BOARD,
                caption=config.other_message,
                photo=config.BANNER_ID,
                parse_mode=enums.ParseMode.HTML
            )
    except:
        pass