from aiogram import Bot, Dispatcher, types, executor
from gtts import gTTS
from config import *
from mem import *
import asyncio
from time import sleep

bot = Bot(TOKEN_API); dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help", "stiker_pak", "mem", "sport", "sticker", "links"])
async def commands(message: types.Message):
    if   message.text=="/start":     await bot.send_message(chat_id=message.from_user.id,text=hello,parse_mode="HTML",reply_markup=start_kb())
    elif message.text=="/sport":     await bot.send_video(message.from_user.id, video=open(r'D:/Visualis/Project/Sport.gif.mp4','rb'))        
    elif message.text=="/help":      await message.reply(text=HELP_COMAND, parse_mode="HTML")
    elif message.text=="/stiker_pak":await message.reply(text='\n'.join([str(i)for i in stickers]))
    elif message.text=="/mem":       await bot.send_photo(message.from_user.id, photo=random_mem())
    elif message.text=="/links":     await message.answer("Мої соц мережі", reply_markup=links_ikb())
    elif message.text=="/sticker":   await message.answer(message.sticker.emoji)

@dp.message_handler(commands=['durack'])
async def durak(message: types.Message):
    global run_game; run_game = True
    await asyncio.create_task(game(message))
    await asyncio.create_task(card(message))
    await asyncio.create_task(no_cards(message))
    await asyncio.create_task(podkid(message))

async def game(message):
    global card_request, car, move; card_request = True
    while not (player==[] or bot_c==[] and cards==[]):
        await message.answer(print_inf(player,bot_c,trum),reply_markup = card_kb(player))
        if move == "player":
            while True:
                if table == []: await message.answer(text="Виберіть чим бажаете походити: ")
                else: await message.answer(text="Виберіть що бажаете підкинути: ")
                while card_request:
                    sleep(1)
                    print(car)
                p = car; car = "0"
                if p in player:
                    if table == []: break
                    elif check(p): 
                        await message.answer(text="Вам нема що бідкидати"); break

            if hod_pleyer(): break
            if throw_up_player():
                await message.answer(text = "Ви можети підкинути карту",reply_markup = card_kb_P(player))
                while podkidat: pass
                if kb_podkid == True:
                    move = "bot"; podkidat = False; kb_podkid = False; break
            else:
                await message.answer(text = "Ви не можети підкинути карту")
                move = "bot"; break


@dp.message_handler(lambda message: message.text in player and card_request)
async def card(message):
    global card_request, podkidat, car
    card_request = False
    podkidat = False
    car = message.text
    print(car)

@dp.message_handler(lambda message: not message.text in player and card_request)
async def no_cards(message):
    if not message.text in player and card_request:
        await message.answer(text="Ви не вибрили карту а ввели з клавіатури!")

@dp.message_handler(lambda message: message.text == "Не підкидати" and podkidat)
async def podkid():
    global podkidat, kb_podkid; podkidat = False; kb_podkid = True

@dp.message_handler(lambda message: message.text in stickers)
async def my_sticker(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker=stickers[message.text])

@dp.message_handler()
async def audio(message: types.Message): 
    while '??' in message.text: message.text = message.text.replace("??","?")
    tts = gTTS(message.text, lang='uk'); tts.save("saund.ogg")
    audio = open(r'D:/Visualis/Project/saund.ogg','rb')
    await bot.send_audio(message.from_user.id, audio=audio)

if __name__ == "__main__": executor.start_polling(dp, skip_updates=True)