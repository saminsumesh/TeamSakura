import os
import glitchart
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


PATH = os.environ.get("PATH", "./DOWNLOADS")


@Client.on_message(filters.private & filters.photo, filters.command("glitch"))
async def glitch_art(bot, update):
    download_path = PATH + "/"
    download_location = download_path + "image.jpg"
    message = await update.reply_text(
        text="`Processing...`",
        quote=True
    )
    try:
        await update.download(
            file_name=download_location
        )
    except Exception as error:
        await message.edit_text(
            text=f"**Error :** `{error}`\nContact @TheFayas."
        )
        return 
    await message.edit_text(
        text="`Converting to glitch...`"
    )
    try:
        glitch_art = glitchart.jpeg(download_location)
        await update.reply_photo(photo=glitch_art, quote=True)
        os.remove(download_location)
        os.remove(glitch_art)
    except Exception as error:
        await message.edit_text(
            text=f"**Error :** `{error}`\nContact @TheFayas."
        )
        return
    await message.delete()
