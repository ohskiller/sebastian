from telethon import functions
from userbot.system import dev_cmd


@bot.on(dev_cmd(pattern="invite ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await event.edit("`.invite` users to a chat, not to a Private Message")
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
            for user_id in to_add_users.split(" "):
                try:
                    await bot(functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id,
                        user_id=user_id,
                        fwd_limit=1000000
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("Invitato! ")
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split(" "):
                try:
                    await bot(functions.channels.InviteToChannelRequest(
                        channel=event.chat_id,
                        users=[user_id]
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("Invitato! ")
            
            

async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await event.edit("`.invite` In chat, non in privato!")
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
            for user_id in to_add_users.split(" "):
                try:
                    await bot(functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id,
                        user_id=user_id,
                        fwd_limit=1000000
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.reply("Invitato! ")
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split(" "):
                try:
                    await bot(functions.channels.InviteToChannelRequest(
                        channel=event.chat_id,
                        users=[user_id]
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.reply("Invitato! ")
