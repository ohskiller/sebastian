from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio
from userbot.system import command


@command(outgoing=True, pattern=r"^.mute ?(\d+)?")
async def startmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("**𝘀𝗶 𝗲 𝘃𝗲𝗿𝗶𝗳𝗶𝗰𝗮𝘁𝗼 𝘂𝗻 𝗲𝗿𝗿𝗼𝗿𝗲! 𝗥𝗶𝗽𝗿𝗼𝘃𝗮𝗿𝗲⚠️**")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/mute", "!mute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit("**𝗿𝗶𝘀𝗽𝗼𝗻𝗱𝗶 𝗮𝗱 𝘂𝗻 𝘂𝘀𝗲𝗿 𝗼 𝗶𝗻𝘀𝗲𝗿𝗶𝘀𝗰𝗶 𝗶𝗹 𝘀𝘂𝗼 𝗶𝗱.**")
        chat_id = event.chat_id
        chat = await event.get_chat()
        if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None: 
            if chat.admin_rights.delete_messages is True:
                pass
            else:
                return await event.edit("**Non puoi mutare se non hai i permessi necessari!⚠️**")
        elif "creator" in vars(chat):
            pass
        elif private == True:
            pass
        else:
            return await event.edit("**𝗻𝗼𝗻 𝘀𝗼𝗻𝗼 𝗮𝗱𝗺𝗶𝗻:(**")
        if is_muted(userid, chat_id):
            return await event.edit("**𝗨𝘁𝗲𝗻𝘁𝗲 𝗴𝗶𝗮 𝗺𝘂𝘁𝗮𝘁𝗼**")
        try:
            mute(userid, chat_id)
        except Exception as e:
            await event.edit("Error occured!\nError is " + str(e))
        else:
            await event.edit("**𝗦𝗲𝗶 𝘀𝘁𝗮𝘁𝗼 𝗺𝘂𝘁𝗮𝘁𝗼! 𝗧𝘂𝘁𝘁𝗼 𝗰𝗶𝗼 𝗰𝗵𝗲 𝘀𝗰𝗿𝗶𝘃𝗶 𝘃𝗲𝗿𝗿𝗮 𝗲𝗹𝗶𝗺𝗶𝗻𝗮𝘁𝗼**")


@command(outgoing=True, pattern=r"^.unmute ?(\d+)?")
async def endmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("**𝘀𝗶 𝗲 𝘃𝗲𝗿𝗶𝗳𝗶𝗰𝗮𝘁𝗼 𝘂𝗻 𝗲𝗿𝗿𝗼𝗿𝗲! 𝗥𝗶𝗽𝗿𝗼𝘃𝗮𝗿𝗲⚠️**")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/unmute", "!unmute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit("**𝗿𝗶𝘀𝗽𝗼𝗻𝗱𝗶 𝗮𝗱 𝘂𝗻 𝘂𝘀𝗲𝗿 𝗼 𝗶𝗻𝘀𝗲𝗿𝗶𝘀𝗰𝗶 𝗶𝗹 𝘀𝘂𝗼 𝗶𝗱.**")
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await event.edit("**𝗨𝘁𝗲𝗻𝘁𝗲 𝗻𝗼𝗻 𝗺𝘂𝘁𝗮𝘁𝗼!**")
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await event.edit("Error occured!\nError is " + str(e))
        else:
            await event.edit("**𝗦𝗲𝗶 𝘀𝘁𝗮𝘁𝗼 𝘀𝗺𝘂𝘁𝗮𝘁𝗼! 𝗢𝗿𝗮 𝗽𝗼𝘁𝗿𝗮𝗶 𝘀𝗰𝗿𝗶𝘃𝗲𝗿𝗲**")
@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        await event.delete()
