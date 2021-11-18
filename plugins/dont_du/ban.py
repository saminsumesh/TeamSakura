from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.admin_check import admin_check
from plugins.helper_functions.extract_user import extract_user
from plugins.helper_functions.string_handling import extract_time


@Client.on_message(filters.command("ban", COMMAND_HAND_LER))
async def ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.kick_member(
            user_id=user_id
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Who Are You...Lamo"
                f"{user_first_name}"
                "You're Banned"
            )
        else:
            await message.reply_text(
                "Who Are You...Lamo "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a>"
                " You're Banned."
            )


@Client.on_message(filters.command("tban", COMMAND_HAND_LER))
async def temp_ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    if not len(message.command) > 1:
        return

    user_id, user_first_name = extract_user(message)

    until_date_val = extract_time(message.command[1])
    if until_date_val is None:
        await message.reply_text(
            (
                "Invalid time type specified. "
                "Excepted m, h, or d, Got: {}"
            ).format(
                message.command[1][-1]
            )
        )
        return

    try:
        await message.chat.kick_member(
            user_id=user_id,
            until_date=until_date_val
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Congratulations You Are Banned 🚫 Lamo..! "
                f"{user_first_name}"
                f" banned for {message.command[1]}!"
            )
        else:
            await message.reply_text(
                "Congratulations Lamo! "
                f"<a href='tg://user?id={user_id}'>"
                "You Are Banned"
                "</a>"
                f" banned for {message.command[1]}!"
            )
