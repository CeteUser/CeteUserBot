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

# ================= CONSTANT =================

@register(outgoing=True, pattern="^.bira")

async def bira(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 101)
    animation_chars = [
            "🍺       🍺",
            "🍺     🍺",
            "🍺  🍺",
            "🍻"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@register(outgoing=True, pattern="^.civciv")
async def port_civciv(event):
	if event.fwd_from:
		return
	deq = deque(list("🐤🐣🐥🐓"))
	for _ in range(18):
		await asyncio.sleep(0.5)
		await event.edit("".join(deq))
		deq.rotate(1)


@register(outgoing=True, pattern="^.engelli")

async def port_engellli(event):

    if event.fwd_from:

        return

    animation_interval = 0.4

    animation_ttl = range(0, 12)

    await event.edit("Bu Gösteri Engelli Arkadaşımız İçin..")

    animation_chars = [

            "♿",
            "♿♿",
            "♿♿♿",
            "♿♿♿♿",
            "♿♿♿♿♿",
            "♿♿♿♿♿♿",
            "Toplanın Engelli Buldum.",
            "♿♿♿♿♿♿",
            "♿♿♿♿♿",
            "♿♿♿♿",
            "♿♿♿",
            "**♿Engellisin**"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])


@register(outgoing=True, pattern="^.cabbar")

async def abbasyanbasan21(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 12)

    await event.edit("hePiNiZE MERHaba ARKADAşlaR..")

    animation_chars = [

            "BEN AbBAs YaNBasan",
            "EVEt bAŞLıyORuz",
            "CabbaR 1",
            "CAbBar 2",
            "CAbbAr 3",
            "EvEt bAŞLıyORuz",
            "ÖhÖM SeSiM gEliYo ivEt",
            "Wara WaRA WARA",
            "len ANA sKrmM",
            "bAqIM",
            "CabBaR aNaN nAsIL? eğeğ",
            "**‼️Abbas yanbasan sunar.**"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])



@register(outgoing=True, pattern="^.kabe")

async def kabe(event):
    if event.fwd_from:
        return
    animation_interval = 1.2
    animation_ttl = range(0, 11)
    animation_chars = [
            "🚶‍♀🚶‍♂🚶‍♀🚶‍♂🚶‍♀\n🚶‍♂              🚶‍♂\n🚶‍♀    🕋     🚶‍♀\n🚶‍♂              🚶‍♂\n🚶‍♀🚶‍♂🚶‍♀🚶‍♂🚶‍♀",
            "🚶‍♂🚶‍♀🚶‍♂🚶‍♀🚶‍♂\n🚶‍♀              🚶‍♀\n🚶‍♂    🕋     🚶‍♂\n🚶‍♀              🚶‍♀\n🚶‍♂🚶‍♀🚶‍♂🚶‍♀🚶‍♂",
            "🚶‍♀🚶‍♂🚶‍♀🚶‍♂🚶‍♀\n🚶‍♂              🚶‍♂\n🚶‍♀    🕋     🚶‍♀\n🚶‍♂              🚶‍♂\n🚶‍♀🚶‍♂🚶‍♀🚶‍♂🚶‍♀",
            "🚶‍♂🚶‍♀🚶‍♂🚶‍♀🚶‍♂\n🚶‍♀              🚶‍♀\n🚶‍♂    🕋     🚶‍♂\n🚶‍♀              🚶‍♀\n🚶‍♂🚶‍♀🚶‍♂🚶‍♀🚶‍♂",
            "🚶‍♀🚶‍♂🚶‍♀🚶‍♂🚶‍♀\n🚶‍♂              🚶‍♂\n🚶‍♀    🕋     🚶‍♀\n🚶‍♂              🚶‍♂\n🚶‍♀🚶‍♂🚶‍♀🚶‍♂🚶‍♀",
            "🚶‍♂🚶‍♀🚶‍♂🚶‍♀🚶‍♂\n🚶‍♀              🚶‍♀\n🚶‍♂    🕋     🚶‍♂\n🚶‍♀              🚶‍♀\n🚶‍♂🚶‍♀🚶‍♂🚶‍♀🚶‍♂",
            "🚶‍♀🚶‍♂🚶‍♀🚶‍♂🚶‍♀\n🚶‍♂              🚶‍♂\n🚶‍♀    🕋     🚶‍♀\n🚶‍♂              🚶‍♂\n🚶‍♀🚶‍♂🚶‍♀🚶‍♂🚶‍♀",
            "🚶‍♂🚶‍♀🚶‍♂🚶‍♀🚶‍♂\n🚶‍♀              🚶‍♀\n🚶‍♂    🕋     🚶‍♂\n🚶‍♀              🚶‍♀\n🚶‍♂🚶‍♀🚶‍♂🚶‍♀🚶‍♂",
            "🚶‍♀🚶‍♂🚶‍♀🚶‍♂🚶‍♀\n🚶‍♂              🚶‍♂\n🚶‍♀    🕋     🚶‍♀\n🚶‍♂              🚶‍♂\n🚶‍♀🚶‍♂🚶‍♀🚶‍♂🚶‍♀",
            "🚶‍♂🚶‍♀🚶‍♂🚶‍♀🚶‍♂\n🚶‍♀              🚶‍♀\n🚶‍♂    🕋     🚶‍♂\n🚶‍♀              🚶‍♀\n🚶‍♂🚶‍♀🚶‍♂🚶‍♀🚶‍♂",
            "🚶‍♀🚶‍♂🚶‍♀🚶‍♂🚶‍♀\n🚶‍♂              🚶‍♂\n🚶‍♀    🕋     🚶‍♀\n🚶‍♂              🚶‍♂\n🚶‍♀🚶‍♂🚶‍♀🚶‍♂🚶‍♀",
            "🚶‍♂🚶‍♀🚶‍♂🚶‍♀🚶‍♂\n🚶‍♀              🚶‍♀\n🚶‍♂    🕋     🚶‍♂\n🚶‍♀              🚶‍♀\n🚶‍♂🚶‍♀🚶‍♂🚶‍♀🚶‍♂"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@register(outgoing=True, pattern="^.fb")

async def m_fb(event):

    if event.fwd_from:

        return

    animation_interval = 0.4

    animation_ttl = range(0, 11)

    #input_str = event.pattern_match.group(1)

    #if input_str == "fb":

    await event.edit("Fenerbahçe..")

    animation_chars = [

            "🔵🔵🔵*F*🟡🟡🟡\n🟡🟡🟡*B*🔵🔵🔵",
            "🟡🟡🟡*F*🔵🔵🔵\n🔵🔵🔵*B*🟡🟡🟡",
            "🔵🔵🔵*F*🟡🟡🟡\n🟡🟡🟡*B*🔵🔵🔵",
            "🟡🟡🟡*F*🔵🔵🔵\n🔵🔵🔵*B*🟡🟡🟡",
            "🔵🔵🔵*F*🟡🟡🟡\n🟡🟡🟡*B*🔵🔵🔵",
            "🟡🟡🟡*F*🔵🔵🔵\n🔵🔵🔵*B*🟡🟡🟡",
            "🔵🔵🔵*F*🟡🟡🟡\n🟡🟡🟡*B*🔵🔵🔵",
            "🟡🟡🟡*F*🔵🔵🔵\n🔵🔵🔵*B*🟡🟡🟡",
            "🔵🔵🔵*F*🟡🟡🟡\n🟡🟡🟡*B*🔵🔵🔵",
            "🟡🟡🟡*F*🔵🔵🔵\n🔵🔵🔵*B*🟡🟡🟡",
            "'♡💙Fenerbahçe💛♡'"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])


@register(outgoing=True, pattern="^.gs")

async def m_gs(event):

    if event.fwd_from:

        return

    animation_interval = 0.4

    animation_ttl = range(0, 11)

    #input_str = event.pattern_match.group(1)

    #if input_str == "gs":

    await event.edit("Galatasaray..")

    animation_chars = [

            "🔴🔴🔴*G*🟡🟡🟡\n🟡🟡🟡*S*🔴🔴🔴",
            "🟡🟡🟡*G*🔴🔴🔴\n🔴🔴🔴*S*🟡🟡🟡",
            "🔴🔴🔴*G*🟡🟡🟡\n🟡🟡🟡*S*🔴🔴🔴",
            "🟡🟡🟡*G*🔴🔴🔴\n🔴🔴🔴*S*🟡🟡🟡",
            "🔴🔴🔴*G*🟡🟡🟡\n🟡🟡🟡*S*🔴🔴🔴",
            "🟡🟡🟡*G*🔴🔴🔴\n🔴🔴🔴*S*🟡🟡🟡",
            "🔴🔴🔴*G*🟡🟡🟡\n🟡🟡🟡*S*🔴🔴🔴",
            "🟡🟡🟡*G*🔴🔴🔴\n🔴🔴🔴*S*🟡🟡🟡",
            "🔴🔴🔴*G*🟡🟡🟡\n🟡🟡🟡*S*🔴🔴🔴",
            "🟡🟡🟡*G*🔴🔴🔴\n🔴🔴🔴*S*🟡🟡🟡",
            "♡❤️Galatasaray💛♡"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])


@register(outgoing=True, pattern="^.surf")

async def surf(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 101)
    animation_chars = [
            "ᅠ🏄🏻‍♂️ᅠᅠᅠᅠᅠᅠᅠ🏄🏻‍♀️\n🌊🌊🌊🌊🌊🌊🌊🌊",
            "ᅠᅠ🏄🏻‍♂️ᅠᅠᅠᅠᅠ🏄🏻‍♀️ᅠ\n🌊🌊🌊🌊🌊🌊🌊🌊",
            "ᅠᅠᅠ🏄🏻‍♂️ᅠᅠᅠ🏄🏻‍♀️ᅠᅠ\n🌊🌊🌊🌊🌊🌊🌊🌊",
            "ᅠᅠᅠᅠ🏄🏻‍♂️🏄🏻‍♀️ᅠᅠᅠᅠ\n🌊🌊🌊🌊🌊🌊🌊🌊",
			"ᅠᅠᅠ🏄🏻‍♂️ᅠᅠᅠ🏄🏻‍♀️ᅠᅠ\n🌊🌊🌊🌊🌊🌊🌊🌊",
			"ᅠᅠ🏄🏻‍♂️ᅠᅠᅠᅠᅠ🏄🏻‍♀️ᅠ\n🌊🌊🌊🌊🌊🌊🌊🌊",
			"ᅠ🏄🏻‍♂️ᅠᅠᅠᅠᅠᅠᅠ🏄🏻‍♀️\n🌊🌊🌊🌊🌊🌊🌊🌊",
			"ᅠᅠ🏄🏻‍♂️ᅠᅠᅠᅠᅠ🏄🏻‍♀️ᅠ\n🌊🌊🌊🌊🌊🌊🌊🌊",
			"ᅠᅠᅠ🏄🏻‍♂️ᅠᅠᅠ🏄🏻‍♀️ᅠᅠ\n🌊🌊🌊🌊🌊🌊🌊🌊",
			"ᅠᅠᅠᅠ🏄🏻‍♂️🏄🏻‍♀️ᅠᅠᅠᅠ\n🌊🌊🌊🌊🌊🌊🌊🌊",
			"ᅠᅠᅠ🏄🏻‍♂️ᅠᅠᅠ🏄🏻‍♀️ᅠᅠ\n🌊🌊🌊🌊🌊🌊🌊🌊",
			"ᅠᅠ🏄🏻‍♂️ᅠᅠᅠᅠᅠ🏄🏻‍♀️ᅠ\n🌊🌊🌊🌊🌊🌊🌊🌊",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@register(outgoing=True, pattern="^.pisicik")

async def pisicik(event):

    if event.fwd_from:

        return

    animation_interval = 0.7

    animation_ttl = range(0, 11)

    #input_str = event.pattern_match.group(1)

    #if input_str == "pisicik":


    animation_chars = [

            "`ᅠᅠᅠᅠᅠ🧶🏃🏼‍♂\n ᅠᅠ  ᅠ  ᅠ  -yakala pisicik\n           ᅠᅠ  \n     ᅠᅠᅠᅠ   \n  ᅠᅠᅠᅠᅠ  🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ 🧶ᅠ  \n           ᅠᅠ  \n     ᅠᅠᅠᅠ   \n  ᅠᅠᅠᅠᅠ  🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n           🧶ᅠ  \n     ᅠᅠᅠᅠ   \n  ᅠᅠᅠᅠᅠ  🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n             ᅠ  \n       🧶ᅠᅠᅠ   \n  ᅠᅠᅠᅠᅠ  🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n             ᅠ  \n         ᅠᅠᅠ   \n  🧶ᅠᅠᅠᅠ  🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n             ᅠ  \n         ᅠᅠᅠ   \n  🧶ᅠᅠᅠ 🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n             ᅠ  \n         ᅠᅠᅠ   \n  🧶ᅠᅠᅠ🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n             ᅠ  \n         ᅠᅠᅠ   \n  🧶ᅠᅠ🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n             ᅠ  \n         ᅠᅠᅠ   \n  🧶ᅠ🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n             ᅠ  \n        -miaw ᅠᅠᅠ   \n  🧶🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ -aferin kızıma\n             ᅠ  \n         ᅠᅠᅠ   \n  🧶🐈`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])


@register(outgoing=True, pattern="^Sa$")

async def merkurkedissa(event):

    if event.fwd_from:

        return

    animation_interval = 0.4

    animation_ttl = range(0, 12)

    await event.edit("Selamün Aleyküm..🐺")

    animation_chars = [

            "S",
            "SA",
            "SEA",
            "**Selam Almayanın Mq**",
            "🌀Sea",
            "🍃Selam",
            "🔅Sa",
            "🍁Selammm",
            "🍃Naber",
            "🔅Ben Geldim",
            "**Hoşgeldim**",
            "**❄️Sea**"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])


@register(outgoing=True, pattern="^.bjk")

async def m_bjk9(event):

    if event.fwd_from:

        return

    animation_interval = 0.4

    animation_ttl = range(0, 11)

    #input_str = event.pattern_match.group(1)

    #if input_str == "bjk":

    await event.edit("Beşiktaş..")

    animation_chars = [

            "⬛⬛⬛B⬜⬜⬜\n⬜⬜⬜J⬛⬛⬛\n⬛⬛⬛K⬜⬜⬜",
            "⬜⬜⬜B⬛⬛⬛\n⬛⬛⬛J⬜⬜⬜\n⬜⬜⬜K⬛⬛⬛",
            "⬛⬛⬛B⬜⬜⬜\n⬜⬜⬜J⬛⬛⬛\n⬛⬛⬛K⬜⬜⬜",
            "⬜⬜⬜B⬛⬛⬛\n⬛⬛⬛J⬜⬜⬜\n⬜⬜⬜K⬛⬛⬛",
            "⬛⬛⬛B⬜⬜⬜\n⬜⬜⬜J⬛⬛⬛\n⬛⬛⬛K⬜⬜⬜",
            "⬜⬜⬜B⬛⬛⬛\n⬛⬛⬛J⬜⬜⬜\n⬜⬜⬜K⬛⬛⬛",
            "⬛⬛⬛B⬜⬜⬜\n⬜⬜⬜J⬛⬛⬛\n⬛⬛⬛K⬜⬜⬜",
            "⬜⬜⬜B⬛⬛⬛\n⬛⬛⬛J⬜⬜⬜\n⬜⬜⬜K⬛⬛⬛",
            "⬛⬛⬛B⬜⬜⬜\n⬜⬜⬜J⬛⬛⬛\n⬛⬛⬛K⬜⬜⬜",
            "⬜⬜⬜B⬛⬛⬛\n⬛⬛⬛J⬜⬜⬜\n⬜⬜⬜K⬛⬛⬛",
            "`♡_⬛Beşiktaş⬜_♡'"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])


@register(outgoing=True, pattern="^.türküm")

async def turkum(event):

    if event.fwd_from:

        return

    animation_interval = 0.8

    animation_ttl = range(0, 11)

    #input_str = event.pattern_match.group(1)

    #if input_str == "türküm":

    await event.edit("o7")

    animation_chars = [

            "`NE MUTLU TÜRKÜM DİYENE`",
            "'⠀⠀⢠⡤⢺⣿⣿⣿⣿⣿⣶⣄\n     ⠉⠀⠘⠛⠉⣽⣿⣿⣿⣿⡇\n⠀⠀⠀⠀⠀⠀⠀⢉⣿⣿⣿⣿⡗\n⠀⢀⣀⡀⢀⣀⣤⣤⣽⣿⣼⣿⢇⡄\n⠀⠀⠙⠗⢸⣿⠁⠈⠋⢨⣏⡉⣳\n⠀⠀⠀⠀⢸⣿⡄⢠⣴⣿⣿⣿\n⠀⠀⠀⠀⠉⣻⣿⣿⣿⣿⣿⡟⡀\n ⠀⠀⠀⠀⠐⠘⣿⣶⡿⠟⠁⣴⣿⣄\n⠀⠀⠀⠀⠀⠘⠛⠉⣠⣴⣾⣿⣿⣿⡦\n⠀⠀⢀⣴⣠⣄⠸⠿⣻⣿⣿⣿⣿⠏\n⠀⣠⣿⣿⠟⠁'",
            "`NE MUTLU TÜRKÜM DİYENE`",
            "'🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥🟥🟥◻️◻️◻️◻️🟥🟥🟥🟥🟥\n🟥🟥🟥◻️◻️🟥🟥🟥◻️🟥🟥🟥🟥\n🟥🟥◻️◻️🟥🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥◻️◻️🟥🟥🟥🟥🟥◻️🟥🟥🟥\n🟥🟥◻️◻️🟥🟥🟥🟥◻️◻️◻️🟥🟥\n🟥🟥◻️◻️🟥🟥🟥🟥🟥◻️🟥🟥🟥\n🟥🟥◻️◻️🟥🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥🟥◻️◻️🟥🟥🟥◻️🟥🟥🟥🟥\n🟥🟥🟥🟥◻️◻️◻️◻️🟥🟥🟥🟥🟥\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥'",
            "`NE MUTLU TÜRKÜM DİYENE`",
            "'⠀⠀⢠⡤⢺⣿⣿⣿⣿⣿⣶⣄\n     ⠉⠀⠘⠛⠉⣽⣿⣿⣿⣿⡇\n⠀⠀⠀⠀⠀⠀⠀⢉⣿⣿⣿⣿⡗\n⠀⢀⣀⡀⢀⣀⣤⣤⣽⣿⣼⣿⢇⡄\n⠀⠀⠙⠗⢸⣿⠁⠈⠋⢨⣏⡉⣳\n⠀⠀⠀⠀⢸⣿⡄⢠⣴⣿⣿⣿\n⠀⠀⠀⠀⠉⣻⣿⣿⣿⣿⣿⡟⡀\n ⠀⠀⠀⠀⠐⠘⣿⣶⡿⠟⠁⣴⣿⣄\n⠀⠀⠀⠀⠀⠘⠛⠉⣠⣴⣾⣿⣿⣿⡦\n⠀⠀⢀⣴⣠⣄⠸⠿⣻⣿⣿⣿⣿⠏\n⠀⣠⣿⣿⠟⠁'",
            "`NE MUTLU TÜRKÜM DİYENE`",
            "'🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥🟥🟥◻️◻️◻️◻️🟥🟥🟥🟥🟥\n🟥🟥🟥◻️◻️🟥🟥🟥◻️🟥🟥🟥🟥\n🟥🟥◻️◻️🟥🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥◻️◻️🟥🟥🟥🟥🟥◻️🟥🟥🟥\n🟥🟥◻️◻️🟥🟥🟥🟥◻️◻️◻️🟥🟥\n🟥🟥◻️◻️🟥🟥🟥🟥🟥◻️🟥🟥🟥\n🟥🟥◻️◻️🟥🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥🟥◻️◻️🟥🟥🟥◻️🟥🟥🟥🟥\n🟥🟥🟥🟥◻️◻️◻️◻️🟥🟥🟥🟥🟥\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥'",
            "`NE MUTLU TÜRKÜM DİYENE`",
            "'⠀⠀⢠⡤⢺⣿⣿⣿⣿⣿⣶⣄\n     ⠉⠀⠘⠛⠉⣽⣿⣿⣿⣿⡇\n⠀⠀⠀⠀⠀⠀⠀⢉⣿⣿⣿⣿⡗\n⠀⢀⣀⡀⢀⣀⣤⣤⣽⣿⣼⣿⢇⡄\n⠀⠀⠙⠗⢸⣿⠁⠈⠋⢨⣏⡉⣳\n⠀⠀⠀⠀⢸⣿⡄⢠⣴⣿⣿⣿\n⠀⠀⠀⠀⠉⣻⣿⣿⣿⣿⣿⡟⡀\n ⠀⠀⠀⠀⠐⠘⣿⣶⡿⠟⠁⣴⣿⣄\n⠀⠀⠀⠀⠀⠘⠛⠉⣠⣴⣾⣿⣿⣿⡦\n⠀⠀⢀⣴⣠⣄⠸⠿⣻⣿⣿⣿⣿⠏\n⠀⣠⣿⣿⠟⠁'",
            "`🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥🟥🟥◻️◻️◻️◻️🟥🟥🟥🟥🟥\n🟥🟥🟥◻️◻️🟥🟥🟥◻️🟥🟥🟥🟥\n🟥🟥◻️◻️🟥🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥◻️◻️🟥🟥🟥🟥🟥◻️🟥🟥🟥\n🟥🟥◻️◻️🟥🟥🟥🟥◻️◻️◻️🟥🟥\n🟥🟥◻️◻️🟥🟥🟥🟥🟥◻️🟥🟥🟥\n🟥🟥◻️◻️🟥🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥🟥◻️◻️🟥🟥🟥◻️🟥🟥🟥🟥\n🟥🟥🟥🟥◻️◻️◻️◻️🟥🟥🟥🟥🟥\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])



@register(outgoing=True, pattern="^.bg")

async def battalgazi(event):

    if event.fwd_from:

        return

    animation_interval = 1.9
    animation_ttl = range(0, 4)
    await event.edit("BATTAL GAZİ")

    animation_chars = ['Ben senin kancık kelleni ödlek bedeninden ayırmaya geldim.', 'Çıkın gidin buradan döverim seni! HEPİNİZİ DÖVERİM ÜLEEAAAAN!', 'Benim adım kerim hepinizi sikerim!', 'Zulme boyun eğmezsek Türk oluruz! Kefereye kılıç çalarsak Türk oluruz! Mazluma umut olursak Türk oluruz!', 'Hele davran bizans kargası', 'Kırk Bakireye bakmaya bal yanaktan tatamaya geldim']


    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i])

PENIS_TEMPLATE = """
{\__/}
( • . •) Beyin İstermisin?
/ >🧠
{\__/}
( • - •) sen kullanamazsın boşver
🧠< /
"""

@register(outgoing=True, pattern=r"^\.(?:beyin)\s?(.)?")
async def emoji_beyin(e):
    emoji = e.pattern_match.group(1)

    await e.edit("Al lazım olur...")
    message = PENIS_TEMPLATE
    if emoji:
        message = message.replace('🍆', emoji)

    await e.edit(message)



CMD_HELP.update({
    "modül":
    "**.surf**\
\n**Kullanım:** `Sruf yapar.`\
\n\n**.bira**\
\n**Kullanım:** `Bira tokuşturur`\
\n\n**.gs**\
\n**Kullanım:** `Galatasaraylı oldugunu belli eder.`\
\n\n**.fb**\
\n**Kullanım:** `Fenerbahçeli oldugunu belli eder`\
\n\n**.bjk**\
\n**Kullanım:** `Beşiktaşlı oldugunu belli eder.`\
\n\n**.cabbar**\
\n**Kullanım:** `Abbas Yanbasan hayranları veya izleyenleri için diyelim yapılmış bir plugin. TaMaMEn eĞLenME aMaÇLı!`\
\n\n**.türküm**\
\n**Kullanım:** `Atatürk ve Bayrak!`\
\n\n**.civciv**\
\n**Kullanım:** `Civcivleri izleyin.`\
\n\n**.engelli**\
\n**Kullanım:** `Engelli arkadaşlarınıza atabilirsiniz!`\
\n\n**.kabe**\
\n**Kullanım:** `Kabe modülü!`\
\n\n**.pisicik**\
\n**Kullanım:** `Pisicik modülü iyi eğlenceler.`\
\n\n**Sa**\
\n**Kullanım:** `Sa yazarak eğlenceli bir şekilde selam verebilirsiniz`\
\n\n**.bg**\
\n**Kullanım:** `Battal gazi gelir.`\
\n\n**.beyin**\
\n**Kullanımı:** `Beyin hediye eder.`\
\n\n**.klp**\
\n**Kullanımı:** `.klp (isim) yazarsanız kalp üstünde isim yazar`\
\n\n**.aşk**\
\n**Kullanımı:** `.aşk (isim) yazarsanız I Love isim yazar`\
\n\n**.tata**\
\n**Kullanımı:** `.tata (isim) yazarsanız silah ucunda isim yazar`\
\n\n**.sevgi**\
\n**Kullanımı:** `Kalp yaratır`\
\n\n**.merhaba**\
\n**Kullanımı:** `Yazarak haWli bir şekilde selam verirsiniz`\
\n\n\n **Uyarlamalar icin teşekkürler @BristolMyers @CeteUserBot ❤**"
})
