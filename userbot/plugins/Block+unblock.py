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

blockMessage = "✅𝒔𝒆𝒊 𝒔𝒕𝒂𝒕𝒐 𝒃𝒍𝒐𝒄𝒄𝒂𝒕𝒐✅"

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

unblockMessage = "**✅𝒔𝒆𝒊 𝒔𝒕𝒂𝒕𝒐 𝒔𝒃𝒍𝒐𝒄𝒄𝒂𝒕𝒐✅**"
 
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
