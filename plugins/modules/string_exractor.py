import os
import string_extract
import domain_extract
from pyrogram import Client, filters

@Bot.on_message(filters.command("extract"))
async def extract(bot, update):
    if " " not in update.text or not update.reply_to_message.text or not update.reply_to_message.caption:
        await update.reply_text("Please send command with type as reply to a string")
    else:
        type = update.text.split()[1]
        string = update.reply_to_message.text if update.reply_to_message.text else update.reply_to_message.caption
        if type not in types:
            await update.reply_text("`Invalid type!`")
        else:
            if type == "lines":
                text = string_extract.lines(string)
            elif type == "spaces":
                text = string_extract.spaces(string)
            elif type == "words":
                text = string_extract.words(string)
            elif type == "links":
                text = string_extract.links(string)
            elif type == "urls":
                text = "\n".join(string_extract.urls(string))
            elif type == "domains":
                text = "\n".join(domain_extract.string_domains(string))
            await update.reply_text(
                text=text,
                quote=True,
                disable_web_page_preview=True
            )
