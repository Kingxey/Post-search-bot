# commands.py

from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from fonction import (
    connect_channel_to_group,
    list_connected_channels,
    disconnect_channel,
    register_user,
    get_stats,
    get_all_users
)

# /connect - Associe un canal à un groupe
@Client.on_message(filters.command("connect") & filters.group)
async def connect_command(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Utilisation : /connect <@username_or_id>")
    
    channel_id = message.command[1]
    group_id = message.chat.id
    result = connect_channel_to_group(channel_id, group_id)
    await message.reply(result)

# /connections - Liste des connexions canal -> groupe
@Client.on_message(filters.command("connections"))
async def connections_command(client, message: Message):
    result = list_connected_channels()
    await message.reply(result)

# /disconnect - Supprimer une connexion
@Client.on_message(filters.command("disconnect"))
async def disconnect_command(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Utilisation : /disconnect <@username_or_channel_id>")
    
    channel_id = message.command[1]
    result = disconnect_channel(channel_id)
    await message.reply(result)

# /broadcast - To send mesage  ( Only OWNER )
@Client.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_command(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Utilisation : /broadcast <votre message>")
    
    text = message.text.split(" ", 1)[1]
    count = 0
    for user_id in get_all_users():
        try:
            await client.send_message(user_id, text)
            count += 1
        except:
            continue
    await message.reply(f"📢 message send to {count} user(s).")

# /stats - To view stats
@Client.on_message(filters.command("stats"))
async def stats_command(client, message: Message):
    result = get_stats()
    await message.reply(result)

@Client.on_message(filters.command("start") & filters.private)
async def register_user_command(client, message: Message):
    register_user(message.from_user.id)
