#By @OHS_Kill3r05 on TG, all rights deserved

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 117)

    input_str = event.pattern_match.group(1)

    if input_str == "antiscam":

        await event.edit(input_str)

        animation_chars = [
 "Informazioni sui gruppi di @STWAntiscambot",
          " Canale delle prove > @STWAntiscam_prove 📂",
"Canale principale > @STWAntiscam_channel👑",
"Assistenza > @STWAntiscam_assistenza_bot⚠️",

"Bot >  @STWAntiscambot 🤖",

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 117])
