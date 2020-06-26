# Copyright (C) 2020 BristolMyers z2sofwares.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Cete UserBot - BristolMyers z2sofwares

""" UserBot yardım komutu """

from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.cete(?: |$)(.*)")
async def cete(event):
    """ .çete komutu için """
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("Lütfen bir Cete modülü adı belirtin.")
    else:
        await event.edit("Lütfen hangi Cete modülü için yardım istediğinizi belirtin !!\
            \nKullanım: .cete <modül adı>")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\n"
        await event.reply(string)
