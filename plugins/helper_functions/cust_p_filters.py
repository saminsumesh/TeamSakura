#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pyrogram import (
    filters
)

async def admin_filter_f(filt, client, message):
    return await admin_check(message)


admin_fliter = filters.create(
    func=admin_filter_f,
    name="AdminFilter"
)
