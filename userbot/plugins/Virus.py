#By @OHS_Kill3r05 on TG, all rights deserved

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.8

    animation_ttl = range(0, 117)

    input_str = event.pattern_match.group(1)

    if input_str == "virus":

        await event.edit(input_str)

        animation_chars = [
            "By @OHS_Kill3r05",
            "caricamento...",
            "caricamento..",
            "caricamento.",
            "sto entrando nel database",
            "caricamento databese completato",            "Virus... 8%n/██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
            "Virus... 20%/█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
            "Virus... 36%/█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
             "Virus... 52%/█████████████▒▒▒▒▒▒▒▒▒▒▒▒",
              "Virus... 84%/█████████████████████▒▒▒▒",
              "virus... 100%/█████████VIRUS███████████",
           "download completato",
           "inserisco i file",
           "caricamento...",
           "caricamento..",
           "file installati",
           "virus installato con sucesso",
           "il tuo userbot e stato disattivato da @OHS_Kill3r05"
           
            

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 117])
