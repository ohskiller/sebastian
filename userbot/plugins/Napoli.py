#By @progettarsi on Telegram

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.47
    animation_ttl = range(0,117)
    input_str = event.pattern_match.group(1)
    if input_str == "napoli":
        await event.edit(input_str)
        animation_chars = [
        "by @OHS_Kill3r05",
            "NAPOLI SIMULATOR🛵",
            "NAPOLI SIMULATOR🛵.",
            "NAPOLI SIMULATO🛵..",
            "NAPOLI SIMULAT🛵...",
            "NAPOLI SIMULA🛵....",
            "NAPOLI SIMUL🛵.....",
            "NAPOLI SIMU🛵......",
            "NAPOLI SIM🛵.......",
            "NAPOLI SI🛵........",
            "NAPOLI S🛵.........",
            "NAPOLI 🛵..........",
            "NAPOLI🛵CURRI GENNA'",
            "NAPOL🛵CURRI GENNA'",
            "NAPO🛵CURRI GENNA'",
            "NAP🛵CURRI GENNA'",
            "NA🛵CURRI GENNA'",
            "N🛵CURRI GENNA'",
            "🛵CURRI GENNA'",
            "Sei stato shippato col motorino🛵"

            ]

        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 117])
