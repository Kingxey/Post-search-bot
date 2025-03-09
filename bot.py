
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import API_ID, API_HASH, BOT_TOKEN
from database import init_db, add_user
from commands import *

# Initialisation du bot
bot = Client("ashi_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# To start Data-Base
init_db()

@bot.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message: Message):
    # Enregistrer l'utilisateur en base de données
    add_user(message.from_user.id)

    await message.reply_photo(
        photo="https://envs.sh/0lA.jpg",
        caption=(
            "👋 Bonjour ! Je suis **Ashi Bot**, un bot qui vous aide à retrouver vos posts "
            "publiés depuis un canal auquel je suis connecté, puis vous envoie les liens "
            "sous forme de **boutons** pour les retrouver facilement."
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📘 help", callback_data="help")],
                [InlineKeyboardButton("ℹ️ infos", callback_data="info")]
            ]
        )
    )

@bot.on_callback_query(filters.regex("help"))
async def help_callback(client, callback_query):
    await callback_query.message.edit_text("🙃 Je crois que vous êtes heureux.")

@bot.on_callback_query(filters.regex("info"))
async def info_callback(client, callback_query):
    await callback_query.message.edit_text("👋 Hi, How are you ?")

# Lancer le bot
if __name__ == "__main__":
    print("🤖 Ashi Bot is running...")
    bot.run()
