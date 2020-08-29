"""Restart or Terminate the bot from any chat
Commands:
.restart
.shutdown"""
import asyncio
import os
import sys

from telethon import events
from userbot import bot, ALIVE_NAME
from userbot.system import dev_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================


@bot.on(dev_cmd("restart"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"`{DEFAULTUSER}:`**𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐫𝐢𝐚𝐯𝐯𝐢𝐚𝐭𝐨...**\n**𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐨𝐧𝐥𝐢𝐧𝐞 𝐭𝐫𝐚 2 𝐦𝐢𝐧𝐮𝐭𝐢[.𝐭𝐞𝐬𝐭 𝐩𝐞𝐫 𝐚𝐯𝐯𝐢𝐚𝐭𝐞]**")
    await bot.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@bot.on(dev_cmd("shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"`{DEFAULTUSER}:`**𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐨𝐟𝐟**\n**𝐚𝐯𝐯𝐢𝐚 𝐦𝐚𝐧𝐮𝐚𝐥𝐦𝐞𝐧𝐭𝐞 𝐝𝐚 𝐡𝐞𝐫𝐨𝐤𝐮**")
    await bot.disconnect()
