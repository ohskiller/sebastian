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

          
@register(outgoing=True, pattern="^.mex")
async def setMessage(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    global message
    message = str(e.text[5:])
    await e.edit("`𝐚𝐧𝐢𝐦𝐚𝐳𝐢𝐨𝐧𝐞 𝐭𝐞𝐬𝐭𝐨 𝐚𝐭𝐭𝐢𝐯𝐚𝐭𝐚 ✅`")





@register(outgoing=True, pattern="^.niceText$")
async def setNiceText(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    global autoNiceText
    if autoNiceText:
      autoNiceText = False
      await e.edit("`𝐚𝐧𝐢𝐦𝐚𝐳𝐢𝐨𝐧𝐞 𝐭𝐞𝐬𝐭𝐨 𝐝𝐢𝐬𝐚𝐭𝐭𝐢𝐯𝐚𝐭𝐚✅`")
    else:
      autoNiceText = True
      await e.edit("` 𝐚𝐧𝐢𝐦𝐚𝐳𝐢𝐨𝐧𝐞 𝐭𝐞𝐬𝐭𝐨 𝐚𝐭𝐭𝐢𝐯𝐚𝐭𝐚✅`")
      
@register(outgoing=True)
async def niceText(e):
  if e.text[0].isalpha() and not e.text == "Canali":
    global autoNiceText
    if autoNiceText:
      mex = ""
      for i in range(len(e.text)):
        if e.text[i] == " ":
          mex = mex + ' '
        else:
          mex = mex + e.text[i]
        await asyncio.wait([e.edit("`" + mex + " |`")])
        await asyncio.sleep(0.1)
        await asyncio.wait([e.edit("`" + mex + "  ‏‏‎ `")])
        await asyncio.sleep(0.1)
        if i == len(e.text) - 1:
          await asyncio.wait([e.edit("`" + e.text + "`")])
          
@register(incoming=True)
async def autoReply(e):
  if e.is_private and not (await e.get_sender()).bot:
    global mutedList
    if e.chat_id in mutedList:
      await e.delete()
    else:
      if type((await e.client.get_me()).status).__name__ ==  "UserStatusOffline":
        global exempt
        if not e.sender.id in exempt:
          exempt.append(e.sender.id)
          x = 0
          while True:
            if type((await e.client.get_me()).status).__name__ ==  "UserStatusOffline":
              await asyncio.sleep(1)
              x += 1
              if x >= 300:
                global message
                await e.respond(message)
                exempt.remove(e.sender.id)
                break
            else:
              exempt.remove(e.sender.id)
              break
