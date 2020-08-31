import asyncio

from userbot.system import register
from telethon import functions, types
 
list = []
tmp_storage_global = None
 
@register(outgoing=True, pattern="^[.]gmex")
async def BroadCast(e):
  global list
  mex = e.text.split(" ", 1)[1]
  await asyncio.wait([e.client.send_message(chat, mex) for chat in list])
  await e.edit("✅ Messaggio mandato a tutti i gruppi della lista ✅")
 
@register(outgoing=True, pattern="^[.]addgroup")
async def blackList(e):
  global list
  try:
    ent = e.text.split(" ", 1)[1]
    group = await e.client.get_entity(ent)
    if not group.id in list:
      list.append(group.id)
      await e.edit("✅ Gruppo Aggiunto Correttamente ✅")
    else:
      await e.edit("Questo gruppo è già aggiunto")
  except:
    await e.edit("❌ Gruppo Non Trovato ❌")
 
@register(outgoing=True, pattern="^[.]delgroup")
async def notBlackList(e):
  global list
  try:
    ent = e.text.split(" ", 1)[1]
    group = await e.client.get_entity(ent)
    if group.id in list:
      list.remove(group.id)
      await e.edit("✅ Gruppo Rimosso Correttamente ✅")
    else:
      await e.edit("❌ Questo gruppo non è nella lista ❌")
  except:
    await e.edit("❌ Gruppo Non Trovato ❌")
 
@register(outgoing=True, pattern="^[.]listgroup")
async def groupList(e):
  global list, tmp_storage_global
  wait = False
  mex = "📃 LISTA GRUPPI 📃\n"
  if tmp_storage_global == None:
    chats = await e.client(GetAllChatsRequest([]))
    tmp_storage_global = chats.chats
    wait = True
  for i in tmp_storage_global:
    if type(i).__name__ == "Channel":
      if i.megagroup and not i.left and i.id in list:
        mex += "\n__" + i.title + " -__ [`" + str(i.id) + "`]"
    elif type(i).__name__ == "Chat":
      if not i.left and not i.kicked and not i.deactivated and i.id in list:
        mex += "\n__" + i.title + " -__ [`" + str(i.id) + "`]"
  await e.edit(mex)
  if wait:
    await asyncio.sleep(1)
    tmp_storage_global = None
