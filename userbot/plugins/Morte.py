#By @OHS_Kill3r05 on TG, all rights deserved

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1.0

    animation_ttl = range(0, 117)

    input_str = event.pattern_match.group(1)

    if input_str == "muori":

        await event.edit(input_str)

        animation_chars = [
            "By @OHS_Kill3r05",
            "hai 15 secondi dopo morirai ",
            "15|",
			 "14|",
			 "13|",
			 "12|",
			 "11|",
			 "10|",
			 "9|",
			 "8|",
			 "7|",
			 "6|",
			 "5|",
			 "4|",
			 "3|",
			 "2|",
			 "1|",
			 "0",
			 "✞︎SEI MORTO✞︎"
			
			

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 117])
