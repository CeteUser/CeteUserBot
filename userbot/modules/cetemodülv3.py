# Copyright (C) 2020 BristolMyers z2sofwares.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Cete UserBot - BristolMyers z2sofwares

""" İnsanlarla eğlenmek için yapılmış olan UserBot modülü. """

from asyncio import sleep
from random import choice, getrandbits, randint
from re import sub
import time
from collections import deque
import requests
from userbot import CMD_HELP
from userbot.events import register
from userbot.modules.admin import get_user_from_event
from telethon import events
import asyncio
import os
import sys
import random
from telethon import events, functions, types
import asyncio
from telethon.tl.types import ChannelParticipantsAdmins

@register(outgoing=True, pattern="^.ask (.*)")
async def ask (event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.edit("️╔══╗╔╗ ♡ ♡ ♡\n╚╗╔╝║║╔═╦╦╦╔╗\n╔╝╚╗║╚╣║║║║╔╣\n╚══╝╚═╩═╩═╩═╝\n♡" + input_str +"♡\n𝓢𝓔𝓝𝓘 𝓢𝓔𝓥𝓘𝓨𝓞𝓡𝓤𝓜")

@register(outgoing=True, pattern="^.bye")

async def bye(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 11)

    await event.edit("Ben Gidiyorum ❤️")

    animation_chars = [
            "❤️=🙋‍♂️====❤️",
            "❤️==🙋‍♂️===❤️",
            "❤️===🙋‍♂️==❤️",
            "❤️====🙋‍♂️=❤️",
            "❤️=====🙋‍♂️❤️",
            "❤️====🙋‍♂️=❤️",
            "❤️===🙋‍♂️==❤️",
            "❤️==🙋‍♂️===❤️",
            "❤️=🙋‍♂️====❤️",
            "❤️🙋‍♂️=====❤️",
            "Bye Bye ❤️",
			]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])

@register(outgoing=True, pattern="^bruh$")

async def oof(e):
    t = "bruh"
    for j in range(16):
        t = t[:-1] + "uh"
        await e.edit(t)

PENIS_TEMPLATE = """
╔╦╦
╠╬╬╬╣
╠╬╬╬╣ I ♥
╠╬╬╬╣ Chocolate
╚╩╩╩╝ CeteUserBot
"""

@register(outgoing=True, pattern=r"^\.(?:cho)\s?(.)?")
async def emoji_nah(e):
    emoji = e.pattern_match.group(1)

    await e.edit("Cete...")
    message = PENIS_TEMPLATE
    if emoji:
        message = message.replace('🍆', emoji)

    await e.edit(message)

@register(outgoing=True, pattern="^.cetepol")

async def port_police(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 12)

    await event.edit("ÇETE")

    animation_chars = [

            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "**🔥Çete Is Here🔥**"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])

PENIS_TEMPLATE = """
♪ღ♪*•.¸¸.•*¨¨*•.♪ღ♪*•.¸¸.•*¨¨*•.♪ღ♪
░H░A░P░P░Y░♪░B░I░R░T░H░D░A░Y░
♪ღ♪*•.¸¸.•*¨¨*•.♪ღ♪*•.¸¸.•*¨¨*•.♪ღ♪
"""

@register(outgoing=True, pattern=r"^\.(?:happy)\s?(.)?")
async def emoji_nah(e):
    emoji = e.pattern_match.group(1)

    await e.edit("Happy...")
    message = PENIS_TEMPLATE
    if emoji:
        message = message.replace('🍆', emoji)

    await e.edit(message)

PENIS_TEMPLATE = """
╭━┳━╭━╭━╮╮
┃┈┈┈┣▅╋▅┫┃
┃┈┃┈╰━╰━━━━━━╮
╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣
╲┃┈┈┈┈┈┈┈┈┈▉▉▉
╲┃┈┈┈┈┈┈┈┈┈◥▉◤
╲┃┈┈┈┈╭━┳━━━━╯
╲┣━━━━━━┫﻿
"""

@register(outgoing=True, pattern=r"^\.(?:hav)\s?(.)?")
async def emoji_nah(e):
    emoji = e.pattern_match.group(1)

    await e.edit("Hav...")
    message = PENIS_TEMPLATE
    if emoji:
        message = message.replace('🍆', emoji)

    await e.edit(message)

PENIS_TEMPLATE = """
/\︵-︵/\
|(◉)(◉)|
\ ︶V︶ /
/↺↺↺↺\
↺↺↺↺↺|
\↺↺↺↺/
¯¯/\¯/\¯
"""

@register(outgoing=True, pattern=r"^\.(?:huu|dick)\s?(.)?")
async def emoji_nah(e):
    emoji = e.pattern_match.group(1)

    await e.edit("Huu...")
    message = PENIS_TEMPLATE
    if emoji:
        message = message.replace('🍆', emoji)

    await e.edit(message)

PENIS_TEMPLATE = """
──────▄▀▄─────▄▀▄
─────▄█░░▀▀▀▀▀░░█▄
─▄▄──█░░░░░░░░░░░█──▄▄
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
"""

@register(outgoing=True, pattern=r"^\.(?:kedi)\s?(.)?")
async def emoji_nah(e):
    emoji = e.pattern_match.group(1)

    await e.edit("Kedi...")
    message = PENIS_TEMPLATE
    if emoji:
        message = message.replace('🍆', emoji)

    await e.edit(message)

@register(outgoing=True, pattern="^.klp (.*)")
async def klp (event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.edit("️❤ ●▬▬▬▬๑۩"+ input_str +"۩๑▬▬▬▬▬● ❤\n                   ❤️ ❤️         ❤️ ❤️\n                 ❤️      ❤️   ❤️      ❤️\n                ❤️           ❤️           ❤️\n                 ❤️                         ❤️\n                   ❤️                     ❤️\n                      ❤️               ❤️\n                         ❤️         ❤️\n                            ❤️   ❤️\n                                ❤️\n𝓢𝓔𝓝𝓘 𝓢𝓔𝓥𝓘𝓨𝓞𝓡𝓤𝓜")

LOL_TEMPLATE = """
😂
😂
😂
😂
😂😂😂😂

     😂😂😂
 😂            😂
😂              😂
 😂            😂
     😂😂😂

😂
😂
😂
😂
😂😂😂😂
"""

@register(outgoing=True, pattern=r"^\.(?:lol)\s?(.)?")
async def emoji_lol(e):
    emoji = e.pattern_match.group(1)
    await e.edit("Lolling :)")
    message = LOL_TEMPLATE
    if emoji:
        message = message.replace('😂', emoji)
    await e.edit(message)

PENIS_TEMPLATE = """
╔══╗╔╗ ♡ ♡ ♡
╚╗╔╝║║╔═╦╦╦╔╗
╔╝╚╗║╚╣║║║║╔╣
╚══╝╚═╩═╩═╩═╝
ஜ۞ஜ ÇETE ஜ۞ஜ
"""

@register(outgoing=True, pattern=r"^\.(?:love)\s?(.)?")
async def emoji_nah(e):
    emoji = e.pattern_match.group(1)

    await e.edit("Love...")
    message = PENIS_TEMPLATE
    if emoji:
        message = message.replace('🍆', emoji)

    await e.edit(message)

@register(outgoing=True, pattern="^.merhaba")

async def bye(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 11)

    await event.edit("Merhaba Ben Geldim ❤️")

    animation_chars = [
            "❤️=🙋‍♂️====❤️",
            "❤️==🙋‍♂️===❤️",
            "❤️===🙋‍♂️==❤️",
            "❤️====🙋‍♂️=❤️",
            "❤️=====🙋‍♂️❤️",
            "❤️====🙋‍♂️=❤️",
            "❤️===🙋‍♂️==❤️",
            "❤️==🙋‍♂️===❤️",
            "❤️=🙋‍♂️====❤️",
            "❤️🙋‍♂️=====❤️",
            "Merhaba ❤️",
			]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])

PENIS_TEMPLATE = """
░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░
░░░░░░░░░░░░░░█░░█░░░░░░░░░░
░░░░░░░░░░░░░░█░░█░░░░░░░░░░
░░░░░░░░░░░░░░█░░█░░░░░░░░░░
░░░░░░░░░░░░░░█░░█░░░░░░░░░░
██████▄███▄████░░███▄░░░░░░░
▓▓▓▓▓▓█░░░█░░░█░░█░░░███░░░░
▓▓▓▓▓▓█░░░█░░░█░░█░░░█░░█░░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░█░░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█░░░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░██░░░░░
▓▓▓▓▓▓█████░░░░░░░░░██░░░░░░
"""

@register(outgoing=True, pattern=r"^\.(?:nah)\s?(.)?")
async def emoji_nah(e):
    emoji = e.pattern_match.group(1)

    await e.edit("Nah...")
    message = PENIS_TEMPLATE
    if emoji:
        message = message.replace('🍆', emoji)

    await e.edit(message)

@register(outgoing=True, pattern="^.hack")

async def port_hack(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 11)

    #input_str = event.pattern_match.group(1)

    #if input_str == "hack":

    await event.edit("Hacking..")

    animation_chars = [

            "`Connecting To Hacked Private Server...`",
            "`Target Selected.`",
            "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 84%\n█████████████████████▒▒▒▒ `",
            "`Hacking... 100%\n█████████HACKED███████████ `",
            "`Targeted Account Hacked...\n\nPay 69$ To Remove this hack..`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])

@register(outgoing=True, pattern="^.plane")
async def port_plane(event):
    if event.fwd_from:
        return


    await event.edit("✈-------------")
    await asyncio.sleep(1)
    await event.edit("-✈------------")
    await asyncio.sleep(1)
    await event.edit("--✈-----------")
    await asyncio.sleep(1)
    await event.edit("---✈----------")
    await asyncio.sleep(1)
    await event.edit("----✈---------")
    await asyncio.sleep(1)
    await event.edit("-----✈--------")
    await asyncio.sleep(1)
    await event.edit("------✈-------")
    await asyncio.sleep(1)
    await event.edit("-------✈------")
    await asyncio.sleep(1)
    await event.edit("--------✈-----")
    await asyncio.sleep(1)
    await event.edit("---------✈----")
    await asyncio.sleep(1)
    await event.edit("----------✈---")
    await asyncio.sleep(1)
    await event.edit("-----------✈--")
    await asyncio.sleep(1)
    await event.edit("------------✈-")
    await asyncio.sleep(1)
    await event.edit("-------------✈")
    await asyncio.sleep(5)
    await event.delete()

@register(outgoing=True, pattern="^.police")

async def port_police(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 12)

    await event.edit("Police")

    animation_chars = [

            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "**🔥Police Is Here🔥**"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])

@register(outgoing=True, pattern="^.snake")

async def port_snake(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 27)

    await event.edit("Snake")

    animation_chars = [

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◻️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◻️◻️◻️️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◻️◻️◻️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "‎◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️",

            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️",

            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◻️◻️",

            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◻️◻️◻️",

            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◻️◻️◻️◻️",

            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

            "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

            "◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

            "◻️◻️◻️◻️◻️\n◻️◻️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

            "◻️◻️◻️◻️◻️\n◻️◻️◻️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️",

            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◻️◻️◻️\n◻️◻️◻️◻️◻️",

            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",

            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",

            "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",

            "◻️◻️◻️◻️◻️\n◻️◼️◻️◼️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 27])

@register(outgoing=True, pattern="^Selam$")

async def oof(e):
    t = "Selam"
    for j in range(16):
        t = t[:-1] + "am"
        await e.edit(t)

PENIS_TEMPLATE = """
♥════♫══════♥
░░▄▀▀▄▄▄▀▀▄░░
░█░░░░░░░░░█░
░▀▄░░░░░░░▄▀░
░░░▀▄░░░▄▀░░░
░░░░░▀▄▀░░░░░
♥════♫══════♥.
"""
@register(outgoing=True, pattern="^.sevgi (.*)")
async def emoji_sevgi(e):
    emoji = e.pattern_match.group(1)

    await e.edit("Seni Seviyorum...")
    message = PENIS_TEMPLATE
    if emoji:
        message = message.replace('🍆', emoji)

    await e.edit(message)

@register(outgoing=True, pattern="^Siktir$")

async def oof(e):
    t = "siktir"
    for j in range(16):
        t = t[:-1] + "ir"
        await e.edit(t)

@register(outgoing=True, pattern="^.tata (.*)")
async def tata(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.edit("️_/﹋\_\n(҂`_´)\n<,︻╦╤─ ҉ - - " + input_str +"\n_/﹋\_")

PENIS_TEMPLATE = """
😎😎
😎😎😎
  😎😎😎
    😎😎😎
     😎😎😎
       😎😎😎
        😎😎😎
         😎😎😎
          😎😎😎
          😎😎😎
      😎😎😎😎
 😎😎😎😎😎😎
 😎😎😎  😎😎😎
    😎😎       😎😎
"""

@register(outgoing=True, pattern=r"^\.(?:yrk|dick)\s?(.)?")
async def emoji_yrk(e):
    emoji = e.pattern_match.group(1)

    await e.edit("Al Bakalım...")
    message = PENIS_TEMPLATE
    if emoji:
        message = message.replace('😎', emoji)

    await e.edit(message)

CMD_HELP.update({
    "modülv3":
    "**.ask**\
\n**Kullanım:** `.ask (isim) olarak kullanabilirsiniz sevginizi belli eder.`\
\n\n**.bye**\
\n**Kullanım:** `Animasyonlu bir şekilde bye mesajı atar`\
\n\n**.bruh**\
\n**Kullanım:** `bruuuuuh`\
\n\n**.cho**\
\n**Kullanım:** `Çikolota çıkar`\
\n\n**.cetepol**\
\n**Kullanım:** `Cete İs Here.`\
\n\n**.happy**\
\n**Kullanım:** `Happy birthday mesajı`\
\n\n**.hav**\
\n**Kullanım:** `Köpek çıkar :)`\
\n\n**.hu**\
\n**Kullanım:** `Baykuş çıkar`\
\n\n**.kedi**\
\n**Kullanım:** `Kedi çıkar`\
\n\n**.lol**\
\n**Kullanım**: `LOL Yazdırır emojilerle`\
\n\n**.love**\
\n**Kullanım:** `I Love Çete`\
\n\n**.merhaba**\
\n**Kullanım:** `Animasyonlu bir şekilde merhaba yazdırır.`\
\n\n**.nah**\
\n**Kullanım:** `Nah çeker.`\
\n\n**.hack**\
\n**Kullanımı:** `Hack işlemini başlatır.`\
\n\n**.plane**\
\n**Kullanımı:** `Uçak animasyonu.`\
\n\n**.police**\
\n**Kullanımı:** `Polis animasyon.`\
\n\n**.snake**\
\n**Kullanımı:** `Yılan Animasyonu.`\
\n\n**Selam**\
\n**Kullanımı:** `Uzatarak selam yazdırır.`\
\n\n**.sevgi**\
\n**Kullanımı:** `Kalp oluşturur.`\
\n\n**siktir**\
\n**Kullanım:** `Uzatarak siktir yazdırır`\
\n\n**.tata**\
\n**Kullanım:** `.tata (@isim) şeklinde yazınız silah uçunda isim çıkar`\
\n\n**.yrk**\
\n**Kullanım:** `Emojili yrk çıkar.`\
\n\n\n **Uyarlamalar icin teşekkürler @BristolMyers ❤** "
})
