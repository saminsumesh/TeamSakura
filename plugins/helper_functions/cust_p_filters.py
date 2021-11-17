#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pyrogram import (
    filters
)

def onw_filter(filt, client, message):
    if USE_AS_BOT:
        return bool(
            True # message.from_user.id in SUDO_USERS
        )
    else:
        return bool(
            message.from_user and
            message.from_user.is_self
        )

async def admin_filter_f(filt, client, message):
    return await admin_check(message)


admin_fliter = filters.create(
    func=admin_filter_f,
    name="AdminFilter"
)
