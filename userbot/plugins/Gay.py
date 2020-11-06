import asyncio

from userbot.system import register
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

@register(outgoing=True, pattern="^[.]gay")
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
        await e.edit(f"🏳‍🌈𝐆𝐀𝐘__𝐂𝐇𝐄𝐂𝐊𝐄𝐑🔍\
\n⛔️ ᴇᴄᴄᴏ ɪʟ ɢᴀʏ ᴘʀᴇsᴇɴᴛᴇ\
\n⛔️ ɪɴ ǫᴜᴇsᴛᴏ ɢʀᴜᴘᴘᴏ --->  {name} \
\n sɢᴀᴍᴀᴛᴏ (^。^)ノ")
      else:
        await e.edit(f"🏳‍🌈𝐆𝐀𝐘__𝐂𝐇𝐄𝐂𝐊𝐄𝐑🔍\
\n⛔️ ᴇᴄᴄᴏ ɪʟ ɢᴀʏ ᴘʀᴇsᴇɴᴛᴇ\
\n⛔️ ɪɴ ǫᴜᴇsᴛᴏ ɢʀᴜᴘᴘᴏ --->  {name} \
\n sɢᴀᴍᴀᴛᴏ (^。^)ノ")
    except:
      await e.edit("🏳‍🌈𝐆𝐀𝐘__𝐂𝐇𝐄𝐂𝐊𝐄𝐑🔍\
\n⛔️ ᴇᴄᴄᴏ ɪʟ ɢᴀʏ ᴘʀᴇsᴇɴᴛᴇ\
\n⛔️ ɪɴ ǫᴜᴇsᴛᴏ ɢʀᴜᴘᴘᴏ --->  {name} \
\n sɢᴀᴍᴀᴛᴏ (^。^)ノ")
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
        await e.edit(f"🏳‍🌈𝐆𝐀𝐘__𝐂𝐇𝐄𝐂𝐊𝐄𝐑🔍\
\n⛔️ ᴇᴄᴄᴏ ɪʟ ɢᴀʏ ᴘʀᴇsᴇɴᴛᴇ\
\n⛔️ ɪɴ ǫᴜᴇsᴛᴏ ɢʀᴜᴘᴘᴏ --->  {name} \
\n sɢᴀᴍᴀᴛᴏ (^。^)ノ")
      else:
        await e.edit(f"🏳‍🌈𝐆𝐀𝐘__𝐂𝐇𝐄𝐂𝐊𝐄𝐑🔍\
\n⛔️ ᴇᴄᴄᴏ ɪʟ ɢᴀʏ ᴘʀᴇsᴇɴᴛᴇ\
\n⛔️ ɪɴ ǫᴜᴇsᴛᴏ ɢʀᴜᴘᴘᴏ --->  {name} \
\n sɢᴀᴍᴀᴛᴏ (^。^)ノ")
    except:
      await e.edit("**❌ 𝗲𝗿𝗿𝗼𝗿𝗲 ❌**")
