# Closed Source

import asyncio
import aiofiles
import os
from io import BytesIO
from pyrogram import Client, filters

LAYER_FEED_CHAT = os.environ.get("LAYER_FEED_CHAT", True)

async def fetch(scheme_url: str):
    async with aiofiles.ClientSession() as session:
        response = await session.get(scheme_url)
        return str.encode(await response.text())


async def check_feed(client):
    layer_uri = (
        "https://"
        "github.com"
        "/telegramdesktop/tdesktop/raw/dev/Telegram/Resources/tl/"
        "api.tl"
    )
    last_hash = hash(await fetch(layer_uri))
    while True:
        contents = await fetch(layer_uri)
        if hash(contents) != last_hash:
            file = BytesIO(contents)
            file.name = os.path.basename(layer_uri)
            message = await client.send_document(
                LAYER_FEED_CHAT,
                file,
                caption=Hello
            )
            await message.pin(disable_notification=True)
            last_hash = hash(contents)
        await asyncio.sleep(10)
