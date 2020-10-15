import asyncio
from telethon import events, version
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME, bot, versions
from userbot.system import dev_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "OHS_kill3r05"
# ============================================

@bot.on(dev_cmd(pattern=f"status", outgoing=True))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running. """
    await alive.edit("**🔰 𝖼𝗋𝖾𝖺𝗍𝗈𝗋𝖾 [OHS_kill3r05](https://t.me/OHS_kill3r05)🔰**\n\n"
                     f"**📎> 𝗏𝖾𝗋𝗌𝗂𝗈𝗇𝖾 𝗍𝖾𝗅𝖾𝗍𝗁𝗈𝗇:** {version.__version__}\n"
                     f"**📎> 𝗏𝖾𝗋𝗌𝗂𝗈𝗇𝖾 𝗉𝗒𝗍𝗁𝗈𝗇:** {versions.__python_version__}\n"
       
                     "✅》𝗎𝗌𝖾𝗋𝖻𝗈𝗍 𝗈𝗇《✅")
