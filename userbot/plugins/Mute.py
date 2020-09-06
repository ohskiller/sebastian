import asyncio
from userbot import bot
from userbot.system import register
from telethon.tl.functions.account import UpdateProfileRequest
from telethon import events
from telethon.events import StopPropagation
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon import functions, types
from telethon.tl.functions.messages import GetAllChatsRequest
from telethon.tl.functions.messages import GetAllChatsRequest

exempt = []
mutedList = []
autoNiceText = False

@register(outgoing=True, pattern="^.mute$")
async def setMute(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    if e.is_private and not (await e.get_sender()).bot:
      global mutedList
      if e.chat_id in mutedList:
        mutedList.remove(e.chat_id)
        await e.edit("`Sei stato smutato! Ora potrai scrivere!`")
      else:
        mutedList.append(e.chat_id)
        await e.edit("`Sei stato mutato! Qualsiasi messaggio verrà scritto sarà cancellato!`")
        
