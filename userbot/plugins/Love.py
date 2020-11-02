import asyncio

from userbot.system import register
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

@register(outgoing=True, pattern="^[.]love")
async def checkVoip(e):
  if e.is_reply:
    msg = await e.get_reply_message()
    try:
      user = await e.client(GetFullUserRequest(msg.sender_id))
      dc_id, location = get_input_location(user.profile_photo)
      if user.user.username != None:
        name = "@" + user.user.username
      else:
        name = user.user.first_name
      if dc_id == 4:
        await e.edit(f"╔══╗\
\n╚╗╔╝\
\n╔╝(¯v´¯)\
\n╚══.¸. {name} ")
      else:
        await e.edit(f"╔══╗\
\n╚╗╔╝\
\n╔╝(¯v´¯)\
\n╚══.¸. {name} ")
    except:
      await e.edit("╔══╗\
\n╚╗╔╝\
\n╔╝(¯v´¯)\
\n╚══.¸. {name}")
  else:
    get = e.text.split(" ", 1)[1]
    try:
      usr = await e.client.get_entity(get)
      user = await e.client(GetFullUserRequest(usr.id))
      dc_id, location = get_input_location(user.profile_photo)
      if user.user.username != None:
        name = "@" + user.user.username
      else:
        name = user.user.first_name
      if dc_id == 4:
        await e.edit(f"╔══╗\
\n╚╗╔╝\
\n╔╝(¯v´¯)\
\n╚══.¸. {name} ")
      else:
        await e.edit(f"╔══╗\
\n╚╗╔╝\
\n╔╝(¯v´¯)\
\n╚══.¸. {name} ")
    except:
      await e.edit("**❌ 𝗲𝗿𝗿𝗼𝗿𝗲 ❌**")
