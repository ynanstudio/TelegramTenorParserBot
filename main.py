import nest_asyncio
import logging
import asyncio
from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
import requests,json
import os
from dotenv import load_dotenv
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TENOR_TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()
allows = [УКАЗАТЬ ТУТ АЙДИ АККАУНТA/ОВ?\,МОЖНО НЕСКОЛЬКО ЧЕРЕЗ ЗАПЯТУЮ]#Защита от постороннего доступа (укажите в этот массив айди аккаунтов ,которые смогу управлять ботом)
active_users = {}
lmt = 150

@dp.message(Command("send"))
async def send_command(message: types.Message):
        if len(message.text.split()) > 1:
            search_term = ' '.join(message.text.split()[1:])
            if message.from_user.id in allows:
                if message.from_user.id in active_users:
                    await message.reply("Сырно")
                else:
                    active_users[message.from_user.id] = True
                    # get the top 8 GIFs for the search term
                    r = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&limit=%s" % (search_term, TENOR_TOKEN, lmt))
                    gif_links = set()
                    if r.status_code == 200:
                        # load the GIFs using the urls for the smaller GIF sizes
                        data = r.json()
                        for result in data['results']:
                            for key, value in result['media_formats'].items():
                                if 'gif' in key:
                                    gif_links.add(value['url'])
                        for link in gif_links:
                            if message.from_user.id in active_users:
                                try:
                                    if link.endswith('.gif'):
                                        await bot.send_animation(message.chat.id,link)
                                    elif link.endswith('.mp4') or link.endswith('.wav'):
                                        await bot.send_video(message.chat.id,link)
                                except:
                                    continue
                            else:
                                await message.reply("парсинг остановлен")
                                break
        else:
            await message.reply("Введи что нужно парсить.")
@dp.message(Command("stop"))
async def stop(message: types.Message):
    if message.from_user.id in active_users:
        del active_users[message.from_user.id]
    else:
        await message.reply("Парсинг не активен")
nest_asyncio.apply()
logging.basicConfig(level=logging.INFO)
async def main():
    await dp.start_polling(bot, skip_updates=True)
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    nest_asyncio.apply(loop.create_task(main()))
    loop.run_forever()
