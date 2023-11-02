import asyncio
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
from telethon.sync import TelegramClient
from telethon import events, functions, types
import datetime

api_id = 28442396
api_hash = '355a93942f840b99262e842391aa96c7'
print('Hisoka')

client = TelegramClient('Hisoka', api_id, api_hash)

mob_status = True
event_status = True
name = 'Hisoka'
mob_lvl_min = 25
mob_lvl_max = 35
i = 0

@client.on(events.NewMessage('chtwrsbot'))
async def main(event):
    if 'Stamina restored. You are ready for more adventures' in event.raw_text:
        await quest()
        await asyncio.sleep(1800)
        await arena()
    elif 'You were strolling around' in event.raw_text:
        await intervene(event)

@client.on(events.NewMessage('me'))
async def events_manager(event):
    global mob_status
    global event_status
    global name
    if 'Mobs off' in event.raw_text:
        mob_status = False
        await client.send_message('me', 'Mobs off')
    elif 'Evento off' in event.raw_text:
        event_status = False
        await client.send_message('me', 'Evento off')
    elif 'Mobs on' in event.raw_text:
        mob_status = True
        await client.send_message('me', 'Mobs on')
    elif 'Evento on' in event.raw_text:
        event_status = True
        await client.send_message('me', 'Evento on')
    elif 'Name' in event.raw_text:
        nam = event.raw_text
        name = nam[5 : ]
        await client.send_message('ChatWarsAgentBot', '/name ' + name)
        await client.send_message('me', 'Ahora tu nombre es: ' + name)
    elif 'Lvl max' in event.raw_text:
        lvl = event.raw_text
        mob_lvl_max = int(lvl[8 : ])
        await client.send_message('me', 'Lvl Maximo establecido en: ' + str(mob_lvl_max))
    elif 'Lvl min' in event.raw_text:
        lvl = event.raw_text
        mob_lvl_max = int(lvl[8 : ])
        await client.send_message('me', 'Lvl Minimo establecido en: ' + str(mob_lvl_max))




@client.on(events.NewMessage)
async def mobs_REC(event):
    global mob_status
    global mob_lvl_max
    global mob_lvl_min
    if 'New Fight from' in event.raw_text:
        po = event.raw_text.find('lvl.')
        po = po + 4
        pos = po + 2
        text = event.raw_text
        lvl = int(text[po : pos])
        await mobs(lvl, event, mob_status, mob_lvl_max, mob_lvl_min)
    elif 'Link of the fight' in event.raw_text:
        await asyncio.sleep(0.5)
        btn = event.buttons[0][0]
        url = btn.url
        link_ubic = url.find('=')
        print(link_ubic)
        link = url[link_ubic:]
        print(link)
        await client.send_message('chtwrsbot', link)

async  def mobs(lvl,event, mob_status = True, mob_lvl_max = 35, mob_lvl_min = 25):
    if mob_status:
        if lvl < mob_lvl_max and lvl > mob_lvl_min:
            await asyncio.sleep(0.5)
            try:
                await event.click(0, 0)
            except:
                print(lvl)



@client.on(events.NewMessage)
async def CW_Evento_REC(event):
    global event_status
    await CW_Evento(event, event_status)

async def CW_Evento(event, event_status = True):
    if event_status:
        if 'Ready to embark on' in event.raw_text:
            await event.click(0, 0)
        elif 'You have some monsters.' and 'Deerhorn Castle should' in event.raw_text:
            await client.send_message('chtwrsbot', event.raw_text)


@client.on(events.MessageEdited)
async def edit_play_REC(event):
    global event_status
    await edit_play(event, event_status)

@client.on(events.NewMessage)
async def fix(event):
    if '/fix' in event.raw_text:
        await asyncio.sleep(2)
        chat_id = event.chat_id
        ms = await client.get_messages(chat_id)
        msg = ms[-1]
        if '🟢' + name in msg.raw_text:
            await asyncio.sleep(1)
            await edit_play(msg)
    elif 'Spooky war ongoing' in event.raw_text and '🟢' + name in event.raw_text:
        await asyncio.sleep(1)
        await edit_play(event)


async def edit_play(event, event_status = True):
    global name

    if event_status:
        if 'Spooky war ongoing' in event.raw_text:
            if '🟢' + name in event.raw_text:
                await asyncio.sleep(15)
                text = event.raw_text
                fichas_inicio = text.find('---')
                fichas_inicio = fichas_inicio + 3
                teto = text[fichas_inicio:]
                fichas_final = teto.find('---')
                fichas_final = fichas_final + fichas_inicio - 1
                texto = text[fichas_inicio: fichas_final]

                i = 0
                j = 0
                k = 0
                l = 0
                print(texto)
                for button in event.buttons[0]:
                    print(i)
                    print(button.text, 'Primer for\n \n \n')
                    if '🧠' in button.text and ('🧠' == texto[1] or '🧠' == texto[-1]):
                        print(texto[1], texto[-1], '1')
                        await event.click(0 , i)
                        print('cerebro')
                        return 0
                    i += 1
                for button in event.buttons[0]:
                    print(button.text, 'Segundo for\n \n \n')
                    print(j)
                    if '🎃' in button.text and ('🎃' == texto[1] or '🎃' == texto[-1]):
                        print(texto[1], texto[-1], '2')
                        await event.click(0, j)
                        print('calabaza')
                        break
                    j += 1
                for button in event.buttons[0]:
                    print(button.text, 'Tercer for\n \n \n')
                    print(k)
                    if '🫀' in button.text and ('🫀' == texto[1] or '🫀' == texto[-1]):
                        print(texto[1], texto[-1], '3')
                        await event.click(0, k)
                        print('Corazon')
                        break
                    k += 1
                for button in event.buttons[0]:
                    print(button.text, 'Cuarto for\n \n \n')
                    print(l)
                    if '💀' or '🦴' or '🩸' or '🦷' in button.text:
                        if '🧠' or '🎃' or '🫀' not in button.text:
                            await event.click(0, l)
                            print('Otro')
                            break
                    else :
                        print('Primer boton')
                        await event.click(0 , 0)
                        break
                    l += 1






async def castle():
    await asyncio.sleep(2)
    await client.send_message('chtwrsbot', '🏰Castle')
    await asyncio.sleep(2)
    ms = await client.get_messages('chtwrsbot')
    msg = ms[-1]
    await asyncio.sleep(2)
    if 'Day' in msg.raw_text:
        return 'Day'
    elif 'Evening' in msg.raw_text:
        return 'Evening'
    elif 'Morning' in msg.raw_text:
        return 'Morning'
    else:
        return 'Night'


async def quest():
    await asyncio.sleep(2)
    pto = await castle()
    i = 2
    print(pto)
    if pto == 'Night' :
        await client.send_message('chtwrsbot', '🗺Quests')
        await asyncio.sleep(2)
        ms = await client.get_messages('chtwrsbot')
        msg = ms[-1]
        await msg.click(0, 2)
        while i > 0:
            await asyncio.sleep(2)
            ms = await client.get_messages('chtwrsbot')
            msg = ms[-1]
            await msg.click(0, 2)
            i = i - 1
    else:
        await client.send_message('chtwrsbot', '🗺Quests')
        await asyncio.sleep(2)
        ms = await client.get_messages('chtwrsbot')
        msg = ms[-1]
        await msg.click(0,1)
        while i > 0:
            await asyncio.sleep(2)
            ms = await client.get_messages('chtwrsbot')
            msg = ms[-1]
            await msg.click(0, 1)
            i = i - 1

async def arena():
    hora = await castle()
    if hora != 'Night':
        await asyncio.sleep(2)
        await client.send_message('chtwrsbot', '▶️Fast fight')
        i = 2
        ms = await client.get_messages('chtwrsbot')
        msg = ms[-1]
        print(msg.raw_text)
        if 'You need to heal your' in msg.raw_text:
            return -1
        elif 'You are too busy with a different' in msg.raw_text:
            return -1
        elif 'You should heal up a bit' in msg.raw_text:
            return -1
        else:
            try:
                while i > 0:
                    await asyncio.sleep(1)
                    ms = await client.get_messages('chtwrsbot')
                    msg = ms[-1]
                    await msg.click(1, 1)
                    i = i -1
            except:
                return -1

async def intervene(event):
    await event.click(0, 0)
    await client.send_message('Me', 'Intervene cogido')



client.start()
client.run_until_disconnected()