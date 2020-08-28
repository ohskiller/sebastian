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

@register(outgoing=True, pattern="^.id")
async def getId(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    if e.is_reply:
      try:
        reply = await e.get_reply_message()
        if reply.sender.username != None:
          await e.edit(f"**🆔 @{reply.sender.username}:** `{reply.sender.id}`")
        else:
          await e.edit(f"🆔 [{reply.sender.first_name}](tg://user?id={reply.sender.id})**:** `{reply.sender.id}`")
      except:
        await e.edit("**Entità non trovata. Riprova senza usare la @**")
    else:
      try:
        text = e.text.split(" ", 1)
        entity = await e.client.get_entity(text[1])
        if hasattr(entity, 'title'):
          await e.edit(f"**🆔 {entity.title}:** `{entity.id}`")
        else:
          if entity.username != None:
            await e.edit(f"**🆔 @{entity.username}:** `{entity.id}`")
          else:
            await e.edit(f"🆔 [{entity.firstname}](tg://user?id={entity.id})**:** `{entity.id}`")
      except:
        await e.edit("**Entità non trovata. Riprova senza usare la @**")
 
