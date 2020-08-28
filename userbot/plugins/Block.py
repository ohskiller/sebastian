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


message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!**"
mexScuola = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
exempt = []
mutedList = []
autoNiceText = False

blockMessage = "**Ops, sei stato bloccato🔒**"

@register(outgoing=True, pattern="^[.]block$")
async def blockUser(e):
  if not (await e.get_sender()).bot:
    global blockMessage
    if e.is_reply:
      reply = await e.get_reply_message()
      await e.delete()
      await e.client.send_message(reply.chat_id, blockMessage, reply_to=reply)
      await e.client(BlockRequest(reply.sender.id))
    else:
      if e.is_private:
        await e.edit(blockMessage)
        await e.client(BlockRequest(e.chat_id))

unblockMessage = "**✅SEI STATO SBLOCCATO✅**"
 
@register(outgoing=True, pattern="^.unblock$")
async def unblockUser(e):
  if not e.text[0].isalpha():
    if not (await e.get_sender()).bot:
      global unblockMessage
      if e.is_reply:
        reply = await e.get_reply_message()
        await e.delete()
        await e.client.send_message(reply.chat_id, unblockMessage, reply_to=reply)
        await e.client(UnblockRequest(reply.sender.id))
      else:
        if e.is_private:
          await e.edit(unblockMessage)
          await e.client(UnblockRequest(e.chat_id))
