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

@register(outgoing=True, pattern="^.on$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "Nicky [onlaiz]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sei Online`")
		
@register(outgoing=True, pattern="^.off$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "Nicky [offlunz]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sei Offline`")
		
@register(outgoing=True, pattern="^.goretime$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "Nicky [sto su goretube ]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sei su gore.tube`")

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

@register(outgoing=True, pattern="^.on$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "Nicky [onlaiz]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sei Online`")
		
@register(outgoing=True, pattern="^.off$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "Nicky [offlunz]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sei Offline`")
		
@register(outgoing=True, pattern="^.goretime$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "Nicky [sto su goretube ]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sei su gore.tube`")

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

@register(outgoing=True, pattern="^.on$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "𖣘︎̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼༒✞๏ђร_𝕜𝕚𝕝𝕝3𝕣05✞𖣔ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ༒卍 [ᵒⁿˡⁱⁿᵉ]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sei Online`")
		
@register(outgoing=True, pattern="^.off$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "𖣘︎̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼༒✞๏ђร_𝕜𝕚𝕝𝕝3𝕣05✞𖣔ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ༒卍 [ᵒᶠᶠˡⁱⁿᵉ]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sei Offline`")
		
@register(outgoing=True, pattern="^.porntime$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "𖣘︎̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼༒✞๏ђร_𝕜𝕚𝕝𝕝3𝕣05✞𖣔ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ༒卍 [sto su pornhub 🌚 ]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sei su pornhub o su qualche sito pedo 🌚`")
		
@register(outgoing=True, pattern="^.salvailmondotime$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "𖣘︎̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼༒✞๏ђร_𝕜𝕚𝕝𝕝3𝕣05✞𖣔ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ༒卍⚡️¹³¹⚡ [sto su Salva il mondo ]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sono su fortnite per precisione salva il mondo`")
