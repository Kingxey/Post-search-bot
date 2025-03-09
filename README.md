# 🤖 Ashi Bot - Telegram Message Search Assistant

Ashi Bot helps users find their previously published posts from connected Telegram channels and delivers them in button format.  
Built with [Pyrogram](https://docs.pyrogram.org) and ready to deploy in 1-click on [Koyeb](https://www.koyeb.com).

---

## 📦 Features

- `/start` - Introduces the bot with a welcome image and buttons.
- `/connect` - Connects a Telegram channel to a group.
- `/connections` - Lists all connected channels.
- `/disconnect` - Disconnects a channel.
- `/broadcast` - Sends a message to all users.
- `/stats` - Shows statistics (users and channels).
- Inline buttons: 📘 Help / ℹ️ Info

---

## 🚀 Deploy to Koyeb

You can deploy the bot to Koyeb in a few clicks.

👉 **[Deploy to Koyeb Now](https://www.koyeb.com)**

### Steps:
1. Push your code to a GitHub repository.
2. Go to [https://www.koyeb.com](https://www.koyeb.com) and sign in.
3. Click "Create Service" > "GitHub Repository".
4. Choose your repo.
5. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Run Command**: `python3 bot.py`
6. Add your environment variables:
   - `API_ID`
   - `API_HASH`
   - `BOT_TOKEN`
   - `OWNER_ID`
7. Click **Deploy** and you're done!

---

## 🐳 Run Locally with Docker

```bash
git clone https://github.com/your-username/ashi-bot
cd ashi-bot
docker build -t ashi-bot .
docker run -d --env-file .env ashi-bot
