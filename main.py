import discord
import os
from keep_alive import keep_alive
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("ディスコードのトークンが設定されていません。.envファイルに DISCORD_TOKEN を設定してください。")

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('ゆあちゃんが起動したよ～')

@client.event
async def on_message(message):
    emoji ="👍"
    await message.add_reaction(emoji)

# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)
