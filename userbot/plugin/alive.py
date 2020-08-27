# Copyright © 2020 di 100101110 Github, <https://github.com/100101110>.
#
# Questo file fa parte del progetto <https://github.com/100101110/userbot-100101110>,
# e viene rilasciato in base alla "Licenza GNU Affero General Public v3.0".
# Si prega di consultare <https://github.com/100101110/userbot-100101110/blob/master/LICENSE>
#
# Tutti i diritti riservati.
# 
# Crediti: @100101110
#

import asyncio
from telethon import events, version
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME, bot, versions
from userbot.system import dev_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================

@bot.on(dev_cmd(pattern=f"alive", outgoing=True))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running. """
    await alive.edit("**🔰𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐛𝐲 OHS_kill3r05🔰**\n\n"
                     f"**> 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧:** {version.__version__}\n"
                     f"**> 𝐏𝐲𝐭𝐡𝐨𝐧:** {versions.__python_version__}\n"
                     f"**> 𝐅𝐢𝐫𝐦𝐰𝐚𝐫𝐞:** {versions.__version__}\n"
                     f"**> 👤𝐔𝐬𝐞𝐫**: {DEFAULTUSER}\n\n"
                     "▬▬▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬▬▬")
