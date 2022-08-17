# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali
# Harshit Sharma


import asyncio
import os
import shutil

from pyrogram.types import InlineKeyboardMarkup

from config import get_queue
from Alexa import BOT_USERNAME, db_mem
from Alexa.Core.PyTgCalls import Queues
from Alexa.Core.PyTgCalls.Alexa import join_stream
from Alexa.Database import (
    add_active_chat,
    add_active_video_chat,
    is_active_chat,
    music_off,
    music_on,
)
from Alexa.Inline import audio_markup, audio_markup2, primary_markup, secondary_markup
from Alexa.Utilities.timer import start_timer

loop = asyncio.get_event_loop()


async def start_stream(
    CallbackQuery,
    file,
    videoid,
    thumb,
    title,
    duration_min,
    duration_sec,
    mystic,
):
    global get_queue
    if CallbackQuery.message.chat.id not in db_mem:
        db_mem[CallbackQuery.message.chat.id] = {}
    wtfbro = db_mem[CallbackQuery.message.chat.id]
    wtfbro["live_check"] = False
    if await is_active_chat(CallbackQuery.message.chat.id):
        position = await Queues.put(CallbackQuery.message.chat.id, file=file)
        _path_ = (str(file)).replace("_", "", 1).replace("/", "", 1).replace(".", "", 1)
        buttons = secondary_markup(videoid, CallbackQuery.from_user.id)
        if file not in db_mem:
            db_mem[file] = {}
        cpl = f"cache/{_path_}final.png"
        shutil.copyfile(thumb, cpl)
        wtfbro = db_mem[file]
        wtfbro["title"] = title
        wtfbro["duration"] = duration_min
        wtfbro["username"] = CallbackQuery.from_user.mention
        wtfbro["videoid"] = videoid
        got_queue = get_queue.get(CallbackQuery.message.chat.id)
        title = title
        user = CallbackQuery.from_user.first_name
        duration = duration_min
        to_append = [title, user, duration]
        got_queue.append(to_append)
        final_output = await CallbackQuery.message.reply_photo(
            photo=thumb,
            caption=(
                f"🎬<b>sᴏɴɢ:</b>[{title[:20]}](https://www.youtube.com/watch?v={videoid}) \n⏳<b>ᴅᴜʀᴀᴛɪᴏɴ:</b> {duration_min} \n💡<b>ɪɴғᴏ:</b> [ɢɪᴠᴇ ᴍᴇ ʜᴇᴀʀᴛ](https://t.me/Give_Me_Heart)\n👤<b>ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:</b>{CallbackQuery.from_user.mention} \n⃣<b>ǫᴜᴇᴜᴇᴅ ᴀᴛ:</b> <b>#{position}</b>"
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        await mystic.delete()
        await CallbackQuery.message.delete()
        os.remove(thumb)
        return
    else:
        if not await join_stream(CallbackQuery.message.chat.id, file):
            return await mystic.edit("ᴇʀʀᴏʀ ᴊᴏɪɴɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ...")
        get_queue[CallbackQuery.message.chat.id] = []
        got_queue = get_queue.get(CallbackQuery.message.chat.id)
        title = title
        user = CallbackQuery.from_user.first_name
        duration = duration_min
        to_append = [title, user, duration]
        got_queue.append(to_append)
        await music_on(CallbackQuery.message.chat.id)
        await add_active_chat(CallbackQuery.message.chat.id)
        buttons = primary_markup(
            videoid, CallbackQuery.from_user.id, duration_min, duration_min
        )
        await mystic.delete()
        cap = f"🎥<b>ᴘʟᴀʏɪɴɢ:</b>[{title[:20]}](https://www.youtube.com/watch?v={videoid}) \n💡<b>ɪɴғᴏ:</b> [ɢɪᴠᴇ ᴍᴇ ʜᴇᴀʀᴛ](https://t.me/Give_Me_Heart)\n👤**ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {CallbackQuery.from_user.mention}"
        final_output = await CallbackQuery.message.reply_photo(
            photo=thumb,
            reply_markup=InlineKeyboardMarkup(buttons),
            caption=cap,
        )
        os.remove(thumb)
        await CallbackQuery.message.delete()
        await start_timer(
            videoid,
            duration_min,
            duration_sec,
            final_output,
            CallbackQuery.message.chat.id,
            CallbackQuery.from_user.id,
            0,
        )


async def start_stream_audio(
    message, file, videoid, title, duration_min, duration_sec, mystic
):
    global get_queue
    if message.chat.id not in db_mem:
        db_mem[message.chat.id] = {}
    wtfbro = db_mem[message.chat.id]
    wtfbro["live_check"] = False
    if message.chat.username:
        link = f"https://t.me/{message.chat.username}/{message.reply_to_message.message_id}"
    else:
        xf = str((message.chat.id))[4:]
        link = f"https://t.me/c/{xf}/{message.reply_to_message.message_id}"
    if await is_active_chat(message.chat.id):
        position = await Queues.put(message.chat.id, file=file)
        if file not in db_mem:
            db_mem[file] = {}
        db_mem[file]["title"] = title
        db_mem[file]["duration"] = duration_min
        db_mem[file]["username"] = message.from_user.mention
        db_mem[file]["videoid"] = videoid
        got_queue = get_queue.get(message.chat.id)
        title = title
        user = message.from_user.first_name
        duration = duration_min
        to_append = [title, user, duration]
        got_queue.append(to_append)
        final_output = await message.reply_photo(
            photo="Utils/Telegram.JPEG",
            caption=(
                f"🎬<b>ᴀᴜᴅɪᴏ:</b> [ɢɪᴠᴇɴ ᴀᴜᴅɪᴏ ᴠɪᴀ ᴛᴇʟᴇɢʀᴀᴍ]({link})\n⏳<b>ᴅᴜʀᴀᴛɪᴏɴ:</b> {duration_min} \n👤<b>ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:</b>{message.from_user.mention} \n⃣<b>ǫᴜᴇᴜᴇᴅ ᴀᴛ:</b> <b>#{position}!</b>"
            ),
            reply_markup=audio_markup2,
        )
        await mystic.delete()
        return
    else:
        if not await join_stream(message.chat.id, file):
            return await mystic.edit(
                "ᴇʀʀᴏʀ ᴊᴏɪɴɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.../nᴍᴀᴋᴇ sᴜʀᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɪs ᴇɴᴀʙʟᴇᴅ..."
            )
        get_queue[message.chat.id] = []
        got_queue = get_queue.get(message.chat.id)
        title = title
        user = message.from_user.first_name
        duration = duration_min
        to_append = [title, user, duration]
        got_queue.append(to_append)
        await music_on(message.chat.id)
        await add_active_chat(message.chat.id)
        buttons = audio_markup(
            videoid, message.from_user.id, duration_min, duration_min
        )
        await mystic.delete()
        cap = f"🎥<b>ᴘʟᴀʏɪɴɢ:</b>[ɢɪᴠᴇɴ ᴀᴜᴅɪᴏ ᴠɪᴀ ᴛᴇʟᴇɢʀᴀᴍ]({link})\n👤**ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {message.from_user.mention}"
        final_output = await message.reply_photo(
            photo="Utils/Telegram.JPEG",
            reply_markup=InlineKeyboardMarkup(buttons),
            caption=cap,
        )
        await start_timer(
            videoid,
            duration_min,
            duration_sec,
            final_output,
            message.chat.id,
            message.from_user.id,
            1,
        )
