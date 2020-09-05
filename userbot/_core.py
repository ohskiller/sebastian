from userbot import bot
from telethon import events
from userbot.system import command, remove_plugin, load_module
from var import Var
import importlib
from pathlib import Path
from userbot import LOAD_PLUG, ALIVE_NAME
import sys
import asyncio
import traceback
import os
import userbot.system
from datetime import datetime

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
DELETE_TIMEOUT = 5
# ============================================


@command(pattern="^.install", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(  # pylint:disable=E0602
                await event.get_reply_message(),
                "userbot/plugins/"  # pylint:disable=E0602
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.edit("✅𝒑𝒍𝒖𝒈𝒊𝒏 𝒊𝒏𝒔𝒕𝒂𝒍𝒍𝒂𝒕𝒐! `{}`".format(os.path.basename(downloaded_file_name)))
            else:
                os.remove(downloaded_file_name)
                await event.edit(f"`{DEFAULTUSER}`:**❌𝒆𝒓𝒓𝒐𝒓𝒆!𝒒𝒖𝒆𝒔𝒕𝒐 𝒑𝒍𝒖𝒈𝒊𝒏 𝒆 𝒈𝒊𝒂 𝒊𝒏𝒔𝒕𝒂𝒍𝒍𝒂𝒕𝒐.**")
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()

@command(pattern="^.send (?P<shortname>\w+)$", outgoing=True)
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match["shortname"]
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    start = datetime.now()
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        force_document=True,
        allow_cache=False,
        reply_to=message_id
    )
    end = datetime.now()
    time_taken_in_ms = (end - start).seconds
    await event.edit("**Caricato {} in {} sec**".format(input_str, time_taken_in_ms))
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()

@command(pattern="^.unload (?P<shortname>\w+)$", outgoing=True)
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"**✅𝒖𝒏𝒍𝒐𝒂𝒅** {shortname} **𝒆𝒔𝒆𝒈𝒖𝒊𝒕𝒐 𝒄𝒐𝒏 𝒔𝒖𝒄𝒆𝒔𝒔𝒐✅**")
    except Exception as e:
        await event.edit("**Unload** {shortname} **eseguito**\n{}".format(shortname, str(e)))
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()

@command(pattern="^.load (?P<shortname>\w+)$", outgoing=True)
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except:
            pass
        load_module(shortname)
        await event.edit(f"**✅𝒄𝒂𝒓𝒊𝒄𝒂𝒕𝒐 𝒄𝒐𝒏 𝒔𝒖𝒄𝒆𝒔𝒔𝒐** {shortname}")
    except Exception as e:
        await event.edit(f"**❌𝒊𝒎𝒑𝒐𝒔𝒔𝒊𝒃𝒊𝒍𝒆 𝒄𝒂𝒓𝒊𝒄𝒂𝒓𝒆 {shortname} causa error.\n{str(e)}**")
