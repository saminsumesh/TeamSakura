"""download from 1134 websites
/ytdl"""

import os
from pyrogram import (
    Client,
    filters
)
from info import (
    COMMAND_HAND_LER
)
from plugins.helper_functions.cust_p_filters import sudo_filter
from plugins.helper_functions.you_tube_dl_extractor import (
    extract_youtube_dl_formats
)
from plugins.helper_functions.extract_link import extract_link

TMP_DOWNLOAD_DIRECTORY = "./DOWNLOADS/"

@Client.on_message(filters.command("ytdl", COMMAND_HAND_LER)
async def down_load_media(client, message):
    status_message = await message.reply_text("...", quote=True)

    current_user_id = message.from_user.id
    # create an unique directory
    user_working_dir = os.path.join(
        TMP_DOWNLOAD_DIRECTORY,
        str(current_user_id)
    )
    # create download directory, if not exist
    if not os.path.isdir(user_working_dir):
        os.makedirs(user_working_dir)

    assumed_url, _, _, _ = extract_link(message.reply_to_message)

    # list the formats, and display in button markup formats
    thumb_image, text_message, reply_markup = await extract_youtube_dl_formats(
        assumed_url,
        user_working_dir
    )
    if thumb_image is not None:
        await message.reply_photo(
            photo=thumb_image,
            quote=True,
            caption=text_message,
            reply_markup=reply_markup
        )
        await status_message.delete()

    else:
        await status_message.edit_text(
            text=text_message,
            reply_markup=reply_markup
        )
