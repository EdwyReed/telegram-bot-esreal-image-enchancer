import base64
from datetime import datetime

import aiohttp
import replicate

from pyrogram import Client, filters
from pyrogram.types import Message

from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
USERS_WHITELIST = set(int(id) for id in os.getenv('ALLOWED_USER_IDS').split(','))

app = Client("esreal_image_enhancer_bot", api_id=TELEGRAM_API_ID, api_hash=TELEGRAM_API_HASH,
             bot_token=TELEGRAM_BOT_TOKEN)


def process_image(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = base64.b64encode(file.read()).decode('utf-8')
            image = f"data:application/octet-stream;base64,{data}"

        image_input = {
            "image": image,
            "scale": 2,
            "face_enhance": False
        }

        output = replicate.run(
            "nightmareai/real-esrgan:350d32041630ffbe63c8352783a26d94126809164e54085352f8326e53999085",
            input=image_input
        )
        return output
    finally:
        os.remove(file_path)


@app.on_message(filters.command("start"))
async def start(client, message: Message):
    start_message = (
        "Привіт! \nЯ бот, який буде покращувати якість твоїх зображень за допомогою nightmareai/real-esrgan AI от Replicate. "
        "\nПросто відправ мені зображення, дай трохи часу і я відправлю тобі зображення з покращенною якістю та 2х резолюцією."
    )
    await message.reply_text(start_message)


@app.on_message(filters.photo)
async def photo_handler(client, message: Message):
    user_id = message.from_user.id
    if user_id not in USERS_WHITELIST:
        await message.reply_text(
            "Вибачте, але я працюю лише зі своїми Хозяїнами! Але ви можете звернутися до них задля оплати доступу до мене🥰💰")
        await message.reply_text("Ось їхні контакти: @honey_cupid 🥰")
        return
    await message.reply_text("Потрібно трохи часу, покращую якість зображення...")
    file_path = await client.download_media(message.photo)
    output_url = process_image(file_path)
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"enchanced_{current_time}.jpg"
    async with aiohttp.ClientSession() as session:
        async with session.get(output_url) as resp:
            if resp.status == 200:
                with open(file_name, 'wb') as f:
                    f.write(await resp.read())
                await client.send_document(message.chat.id, file_name, caption="Ось готове зображення!")
                os.remove(file_name)


if __name__ == "__main__":
    app.run()
