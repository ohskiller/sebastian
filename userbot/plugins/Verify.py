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

          
@register(outgoing=True, pattern="^[.]verify$")
async def Verify(e):
  global verify
  verify = e
  await e.client.send_message("@SpamBot", "/start")
 
@register(incoming=True)
async def checkVerify(e):
  global verify
  if verify != None:
    if e.chat_id == 178220800:
      if ":" in e.text:
        st = e.text.split(" ")
        for i in range(st.__len__()):
          if ":" in st[i]:
            fine = st[i - 3] + " " + st[i - 2] + " " + st[i - 1] + " Ore: " +st[i]
            break
        await verify.edit(f"**❌ Sei limitato fino al {fine} ❌**")
        verify = None
        await e.client(functions.messages.DeleteHistoryRequest(e.chat_id, 0, False, True))
      else:
        await verify.edit("**✅ Non sei limitato ✅**")
        verify = None
        await e.client(functions.messages.DeleteHistoryRequest(e.chat_id, 0, False, True))
