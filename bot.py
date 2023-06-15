from aiogram import Bot, Dispatcher, types, executor
from gtts import gTTS
from config import *
from coloda import *
from mem import *
import asyncio

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

@dp.message_handler(lambda message: message.text in stickers)
async def my_sticker(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker=stickers[message.text])

@dp.message_handler(commands=['durack'])
async def durak(message: types.Message):
    global players
    players[message.from_user.id] = new()
    await asyncio.create_task(game(message))
    try:
        await asyncio.create_task(card(message))
        await asyncio.create_task(no_cards(message))
        await asyncio.create_task(podkid(message))
        await asyncio.create_task(bot_podkid(message))
    except: pass

async def game(message):
    global deck, players
    while not((players[message.from_user.id]["player"]==[] or players[message.from_user.id]["bot"]==[])and players[message.from_user.id]["cards"]==[]):
        players[message.from_user.id]["not_opt"] = True
        if players[message.from_user.id]["move"] == "player":
            if players[message.from_user.id]["table"] == []:
                await message.answer(print_inf(players[message.from_user.id]["table"],players[message.from_user.id]["trum"],players[message.from_user.id]["cards"]),
                                    reply_markup = card_kb(players[message.from_user.id]["player"]))
                if players[message.from_user.id]["text"]!="text":await message.answer(text=players[message.from_user.id]["text"]);players[message.from_user.id]["text"]="text"

                while players[message.from_user.id]["card_request"]: await asyncio.sleep(1)
                players[message.from_user.id]["p"] = players[message.from_user.id]["car"]
                players[message.from_user.id]["card_request"] = True
                players[message.from_user.id]["podkidat"] = True
                players[message.from_user.id]["bitca"] = True
                players[message.from_user.id]["car"] = "0"
                players[message.from_user.id]["player"].remove(players[message.from_user.id]["p"])
                players[message.from_user.id]["table"].append(players[message.from_user.id]["p"])
            elif players[message.from_user.id]["bot"]!=[]:
                await message.answer(print_inf(players[message.from_user.id]["table"],players[message.from_user.id]["trum"],players[message.from_user.id]["cards"]),
                                     reply_markup = card_kb_P(players[message.from_user.id]["player"]))
                while True:
                    while players[message.from_user.id]["podkidat"]: await asyncio.sleep(1)

                    players[message.from_user.id]["p"] = players[message.from_user.id]["car"]
                    players[message.from_user.id]["car"] = "0"
                    players[message.from_user.id]["bitca"] = True
                    players[message.from_user.id]["podkidat"] = True
                    players[message.from_user.id]["card_request"] = True

                    if players[message.from_user.id]["kb_podkid"]:
                        next_raund(players[message.from_user.id]["cards"],players[message.from_user.id]["bot"],players[message.from_user.id]["player"])
                        players[message.from_user.id]["move"] = "bot"
                        players[message.from_user.id]["table"]=[]
                        players[message.from_user.id]["kb_podkid"]=False
                        players[message.from_user.id]["not_opt"]=False
                        break
                    else:
                        if check(players[message.from_user.id]["p"], players[message.from_user.id]["table"]):
                            players[message.from_user.id]["player"].remove(players[message.from_user.id]["p"])
                            players[message.from_user.id]["table"].append(players[message.from_user.id]["p"])
                            break
                        else: 
                            await message.answer("Спробуйте иншу карту!")
            else:
                await message.answer(text="Пидкинути карту немождиво у противника нема карт!")
                next_raund(players[message.from_user.id]["cards"],players[message.from_user.id]["bot"],players[message.from_user.id]["player"])
                players[message.from_user.id]["move"] = "bot"
                players[message.from_user.id]["table"]=[]


            if players[message.from_user.id]["not_opt"]:
                players[message.from_user.id]["b"] = logick_bot(players[message.from_user.id]["p"], players[message.from_user.id]["bot"], players[message.from_user.id]["trum"])
                if players[message.from_user.id]["b"] == False:
                    await message.answer("Противник забираэ карти!")
                    players[message.from_user.id]["bot"] += players[message.from_user.id]["table"]
                    players[message.from_user.id]["table"]  = []
                    players[message.from_user.id]["not_opt"]= False
                    next_raund(players[message.from_user.id]["cards"],players[message.from_user.id]["bot"],players[message.from_user.id]["player"])
                else:
                    await message.answer(text="Противник бьє картою " + players[message.from_user.id]["b"])
                    players[message.from_user.id]["table"].append(players[message.from_user.id]["b"])
                    players[message.from_user.id]["bot"].remove(players[message.from_user.id]["b"])
    
        elif players[message.from_user.id]["move"] == "bot":
            if players[message.from_user.id]["text"]!="text": await message.answer(text=players[message.from_user.id]["text"]);players[message.from_user.id]["text"]="text"

            if players[message.from_user.id]["player"]!= []: 
                players[message.from_user.id]["a"],players[message.from_user.id]["b"] = \
                hod_bot(players[message.from_user.id]["table"],players[message.from_user.id]["bot"],players[message.from_user.id]["trum"])
            else: players[message.from_user.id]["a"] = False

            if players[message.from_user.id]["a"] != False:
                await message.answer(print_inf(players[message.from_user.id]["table"],players[message.from_user.id]["trum"],players[message.from_user.id]["cards"]),
                                     reply_markup = card_kb_Z(players[message.from_user.id]["player"]))

                players[message.from_user.id]["bot"].remove(players[message.from_user.id]["b"])
                players[message.from_user.id]["table"].append(players[message.from_user.id]["b"])
                while True:
                    await message.answer(text = players[message.from_user.id]["a"], reply_markup = card_kb_Z(players[message.from_user.id]["player"]))
                    while players[message.from_user.id]["bitca"]: await asyncio.sleep(1)

                    players[message.from_user.id]["p"] = players[message.from_user.id]["car"]
                    players[message.from_user.id]["card_request"] = True
                    players[message.from_user.id]["podkidat"] = True
                    players[message.from_user.id]["bitca"] = True
                    players[message.from_user.id]["car"] = "0"

                    if players[message.from_user.id]["zabrat"]:
                        players[message.from_user.id]["player"] += players[message.from_user.id]["table"]
                        next_raund(players[message.from_user.id]["cards"],players[message.from_user.id]["bot"],players[message.from_user.id]["player"])
                        players[message.from_user.id]["zabrat"] = False
                        players[message.from_user.id]["table"] = []
                        break

                    if players[message.from_user.id]["b"][0] == players[message.from_user.id]["p"][0] and ind(players[message.from_user.id]["p"]) > ind(players[message.from_user.id]["b"]): 
                        players[message.from_user.id]["table"].append(players[message.from_user.id]["p"])
                        players[message.from_user.id]["player"].remove(players[message.from_user.id]["p"])
                        break
                    elif players[message.from_user.id]["p"][0] == players[message.from_user.id]["trum"][0] and players[message.from_user.id]["b"][0] != players[message.from_user.id]["trum"][0]: 
                        players[message.from_user.id]["table"].append(players[message.from_user.id]["p"])
                        players[message.from_user.id]["player"].remove(players[message.from_user.id]["p"])
                        break
                    elif players[message.from_user.id]["p"][0]==players[message.from_user.id]["trum"][0] and players[message.from_user.id]["b"][0]==players[message.from_user.id]["trum"][0] and ind(players[message.from_user.id]["p"])>ind(players[message.from_user.id]["b"]): 
                        players[message.from_user.id]["table"].append(players[message.from_user.id]["p"])
                        players[message.from_user.id]["player"].remove(players[message.from_user.id]["p"])
                        break
                    else:
                        await message.answer("Спробуйте иншу карту!") 
            else:
                await message.answer("Противнику нема що підкидати!")
                next_raund(players[message.from_user.id]["cards"],players[message.from_user.id]["bot"],players[message.from_user.id]["player"])
                players[message.from_user.id]["move"] = "player"
                players[message.from_user.id]["table"] = []

    await message.answer(text = game_over(players[message.from_user.id]["player"],players[message.from_user.id]["bot"]), reply_markup=start_kb())
    del players[message.from_user.id]

@dp.message_handler(lambda message: message.from_user.id in players and message.text in players[message.from_user.id]["player"] and players[message.from_user.id]["card_request"])
async def card(message):
    global players
    players[message.from_user.id]["car"] = message.text
    players[message.from_user.id]["card_request"] = False
    players[message.from_user.id]["podkidat"] = False
    players[message.from_user.id]["bitca"] = False

@dp.message_handler(lambda message: message.from_user.id in players and message.text == "Не підкидати" and players[message.from_user.id]["podkidat"])
async def podkid(message):
    global players
    players[message.from_user.id]["podkidat"] = False
    players[message.from_user.id]["kb_podkid"]= True


@dp.message_handler(lambda message: message.from_user.id in players and message.text == "Забрати" and players[message.from_user.id]["bitca"])
async def bot_podkid(message):
    global players
    players[message.from_user.id]["bitca"] = False
    players[message.from_user.id]["zabrat"]= True

@dp.message_handler(lambda message: message.from_user.id in players and not message.text in players[message.from_user.id]["player"] and players[message.from_user.id]["card_request"])
async def no_cards(message):
    if not message.text in players[message.from_user.id]["player"] and players[message.from_user.id]["card_request"]:
        await message.answer(text="У вас нема токої карти!")

@dp.message_handler()
async def audio(message: types.Message): 
    while '??' in message.text: message.text = message.text.replace("??","?")
    tts = gTTS(message.text, lang='uk'); tts.save("saund.ogg")
    audio = open(r'D:/Visualis/Project/saund.ogg','rb')
    await bot.send_audio(message.from_user.id, audio=audio)

if __name__ == "__main__": 
    executor.start_polling(dp, skip_updates=True)