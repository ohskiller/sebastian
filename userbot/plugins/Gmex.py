import asyncio
from telethon.sync import TelegramClient
from telethon import functions, types
from userbot.system import register

#message = "**PLUGIN DI @OHS_Kill3r05**"
exempt = []
mutedList = []
#autoNiceText = True
exempted = []
e = [] 

@register(outgoing=True, pattern="^[.]gmex ")
async def BroadCast(e):
  global exempted
  mex = e.text.split(" ", 1)[1]
  Uauzs = await e.client(functions.messages.GetAllChatsRequest([0]))
  chattezzs = []
  for i in Uauzs.chats:
    if not i.id in chattezzs:
      chattezzs.append(i.id)
  chats = []
  for i in chattezzs:
    if not str(i) in exempted:
      chats.append(i)
  await asyncio.wait([e.client.send_message(chat, mex) for chat in chats])
  await e.edit("Mex mandato in tutti i gruppi in cui sei presente!")
