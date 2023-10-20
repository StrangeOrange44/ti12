import requests
from bs4 import BeautifulSoup
import emoji
from config import Tg_bot_Token
from aiogram import Bot, types, Dispatcher, executor
import wkeybord as Key
import os
carry_emojii=emoji.emojize(":dagger:")
mid_emojii=emoji.emojize(":bow_and_arrow:")
off_emojii=emoji.emojize(":shield:")
sup_emojii=emoji.emojize(":handshake:")
supp_emojii=emoji.emojize(":star:")
bot = Bot(Tg_bot_Token)
dp = Dispatcher(bot)
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply(f"Вам нужно выбрать регион:\n",
                        reply_markup=Key.mainMenu)
@dp.message_handler()
async def Get_data(message: types.Message):
        if message.text=="Америка":
            await message.reply(f"Вам нужно выбрать команду с ti12:\n",
                                reply_markup= Key.USMenu)
        elif message.text=="Южная Америка":
            await message.reply(f"Вам нужно выбрать команду с ti12:\n",
                                reply_markup= Key.SAMenu)
        elif message.text=="СНГ":
            await message.reply(f"Вам нужно выбрать команду с ti12:\n",
                                reply_markup=Key.EEUMenu)
        elif message.text=="Европа":
            await message.reply(f"Вам нужно выбрать команду с ti12:\n",
                                reply_markup=Key.WEUMenu)
        elif message.text=="Азия":
            await message.reply(f"Вам нужно выбрать команду с ti12:\n",
                                reply_markup=Key.AsiaMenu)
        if message.text=="Главное меню":
            await message.reply(f"Главное меню",
                                reply_markup=Key.mainMenu)
        if message.text!="Европа" and message.text!="Азия" and message.text!="СНГ" and message.text!="Южная Америка" and message.text!="Америка" and message.text!="Главное меню":
            req=requests.get(f"https://liquipedia.net/dota2/{message.text}")
            with open("project.html","w", encoding="UTF-8") as file:
                file.write(req.text)


            with open("project.html", encoding="UTF-8") as file:
                src=file.read()
            soup=BeautifulSoup(src,"lxml")
            ids=soup.find_all("td",class_="ID")
            players_urls=[]
            for id in ids:
                player_url="https://liquipedia.net"+id.find("a").get("href")
                players_urls.append(player_url)
            players_urls=players_urls[0:5]
            #print(*players_urls)
            Names=[]
            info=[]
            Info = []
            Nationality=[]
            Role=["Carry","Solo Middle","Offlaner", "Support","Full Support"]
            Prize=[]
            Nickname=[]
            for urls in players_urls:
                req = requests.get(urls)
                with open("project.html1", "w", encoding="UTF-8") as file:
                    file.write(req.text)

                with open("project.html1", encoding="UTF-8") as file:
                    src = file.read()
                soup = BeautifulSoup(src, "lxml")
                Nick = soup.find( class_="infobox-cell-2 infobox-description").find_next().text
                Names.append(Nick)
                if "Ілля Мулярчук" in Names:
                    Names[0] = Names[0].replace("Ілля Мулярчук", "Илья Мулярчук")
                if "Володимир Міненко" in Names:
                    Names[0] = Names[0].replace("Володимир Міненко", "Владимир Миненко")
                if "Дзмітрый Палішчук" in Names:
                    Names[4] = Names[4].replace("Дзмітрый Палішчук", "Дмитрий Палишчук")
                Age=soup.find_all( class_="infobox-cell-2 infobox-description")
                for age in Age:
                    age=age.find_next().text
                    info.append(age)
                Nickn=soup.find_all("p")
                for nick in Nickn:
                    nick=nick.find("b")
                    if nick!=None and nick.text!="Note:":
                        Nickname.append(nick.text)


            if len(info)==49 and info[0]=='Michael Vu':
                info1=[1,2,5,8,11,12,15,18,21,22,25,28,31,32,35,37,40,41,44,47]
                for i in info1:
                    Info.append(info[i])
                for i in range(0,20,4):
                    Nationality.append(Info[i][1::])
                for i in range(2,20,4):
                    Role.append(Info[i])
                for i in range(3,20,4):
                    Prize.append(Info[i])
            elif len(info)==49 and info[0]=='Антон Шкредов':
                info1=[2,6,9,12,16,19,22,26,29,32,36,38,41,45,47]
                for i in info1:
                    Info.append(info[i])
                for i in range(0,15,3):
                    Nationality.append(Info[i][1::])
                for i in range(1,16,3):
                    Role.append(Info[i])
                for i in range(2,16,3):
                    Prize.append(Info[i])
            elif len(info) == 49 and info[0] == 'Oliver Lepko':
                info1 = [1,5,8,11,15,17,21,25,28,31,35,37,41,45,47]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(1, 16, 3):
                    Role.append(Info[i])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])
            elif len(info) == 49 and info[0] == 'Crhistian Antony Savina Casanova'or info[0] == 'Guilherme Silva Costábile' or info[0] == 'David Nicho Flores':
                info1 = [1,5,8,11,15,18,21,25,27,30,34,37,40,44,47]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(1, 16, 3):
                    Role.append(Info[i])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])
            elif len(info) == 54 and info[0] == 'Ілля Мулярчук':
                info1 = [2, 6, 9,13,17,20,24,28,31,35,39,42,46,50,52]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(1, 16, 3):
                    Role.append(Info[i])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])
            elif len(info) == 54 and info[0] == '郭轩昂':
                info1 = [2, 6, 8,12,16,19,23,27,30,34,38,41,45,49,52]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(1, 16, 3):
                    Role.append(Info[i])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])
            elif len(info) == 53 and info[0] == 'Роман Кушнарев':
                info1 = [2, 6, 9,13,17,20,24,28,30,34,38,40,44,48,51]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(1, 16, 3):
                    Role.append(Info[i])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])
            elif len(info) == 53 and info[0] == '叶乃政':
                info1 = [2, 6, 9,13,17,20,23,27,30,34,38,41,44,48,51]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(1, 16, 3):
                    Role.append(Info[i])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])
            elif len(info) == 50 and info[0] == 'Artour Babaev':
                info1 = [1,5,8,11,15,17,20,24,27,30,34,37,41,45,48]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(1, 16, 3):
                    Role.append(Info[i])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])
            elif len(info) == 50 and info[0] == 'Алимжан Исламбеков':
                info1 = [2,6,9,12,16,18,21,25,27,31,35,38,42,46,48]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(1, 16, 3):
                    Role.append(Info[i])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])
            elif len(info) == 50 and info[0] == 'Айбек Токаев':
                info1 = [2,6,9,12,16,19,22,26,28,31,35,38,42,46,48]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(1, 16, 3):
                    Role.append(Info[i])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])
            elif len(info) == 51 and info[0] == 'หนึ่งนรา ธีรมหานนท์':
                info1 = [2,6,9,12,16,18,22,26,29,32,36,38,42,46,49]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(1, 16, 3):
                    Role.append(Info[i])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])
            elif len(info) == 48 and info[0] == "Enzo Gianoli O'Connor":
                info1=[1,5,7,10,14,16,20,24,27,30,34,37,40,44,46]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(1, 16, 3):
                    Role.append(Info[i])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])
            elif len(info) == 48 and info[0] == 'Héctor Antonio Rodríguez':
                info1 = [1, 5, 8, 11, 15, 17, 20, 24, 26, 29, 33, 36, 39, 43, 46]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(1, 16, 3):
                    Role.append(Info[i])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])
            elif len(info) == 48 and info[0] == 'Алексей Свиридов':
                info1 = [2, 6, 9, 12, 16, 18, 21, 25, 28, 31, 35, 37, 39, 43, 46]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(1, 16, 3):
                    Role.append(Info[i])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])
            elif len(info) == 55 and info[0] == 'Егор Григоренко':
                info1 = [2, 6, 9, 13, 17, 20, 24, 28, 31, 35, 39, 42, 46, 50, 53]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(1, 16, 3):
                    Role.append(Info[i])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])
            elif len(info) == 52 and info[0] == 'Илья Ульянов':
                info1 = [2, 6, 9, 13, 17, 19, 23, 27, 29, 33, 37, 39, 43, 47, 50]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(1, 16, 3):
                    Role.append(Info[i])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])
            elif len(info) == 56 and info[0] == '楼桢':
                info1 = [2, 6, 9, 13, 17,21,25,29,32,36,40,43,47,51,54]
                for i in info1:
                    Info.append(info[i])
                for i in range(0, 15, 3):
                    Nationality.append(Info[i][1::])
                for i in range(2, 16, 3):
                    Prize.append(Info[i])

            Carry=[Nickname[0], Names[0], Nationality[0], Role[0],Prize[0],players_urls[0]]
            Middle=[Nickname[1],Names[1],Nationality[1],Role[1],Prize[1],players_urls[1]]
            Offlaner=[Nickname[2],Names[2],Nationality[2],Role[2],Prize[2],players_urls[2]]
            soft_support=[Nickname[3],Names[3],Nationality[3],Role[3],Prize[3],players_urls[3]]
            Support=[Nickname[4], Names[4],Nationality[4],Role[4],Prize[4],players_urls[4]]
            dollar=emoji.emojize(f":heavy_dollar_sign:")
            await message.reply(f"Pos1:\n"
            f"Ник: {Nickname[0]}\n"
            f"Имя: {Names[0]}\n"
            f"Роль: {Role[0]}{carry_emojii}\n"
            f"Национальность: {Nationality[0]} \n"
            f"Призовые за всё время: {dollar}{Prize[0][1::]}\n"
            f"Ссылка на liquipedia: {players_urls[0]}\n"
            f">>>>>>>>>>>>>>>><<<<<<<<<<<<<<<\n"
            f"Pos2:\n"
            f"Ник: {Nickname[1]}\n"
            f"Имя: {Names[1]}\n"
            f"Роль: {Role[1]}{mid_emojii}\n"
            f"Национальность: {Nationality[1]}\n"
            f"Призовые за всё время: {dollar}{Prize[1][1::]}\n"
            f"Ссылка на liquipedia: {players_urls[1]}\n"
            f">>>>>>>>>>>>>>>><<<<<<<<<<<<<<<\n"
            f"Pos3:\n"
            f"Ник: {Nickname[2]}\n"
            f"Имя: {Names[2]}\n"
            f"Роль: {Role[2]}{off_emojii}\n"
            f"Национальность: {Nationality[2]}\n"
            f"Призовые за всё время: {dollar}{Prize[2][1::]}\n"
            f"Ссылка на liquipedia: {players_urls[2]}\n"
            f">>>>>>>>>>>>>>>><<<<<<<<<<<<<<<\n"
            f"Pos4:\n"
            f"Ник: {Nickname[3]}\n"
            f"Имя: {Names[3]}\n"
            f"Роль: {Role[3]}{sup_emojii}\n"
            f"Национальность: {Nationality[3]}\n"
            f"Призовые за всё время: {dollar}{Prize[3][1::]}\n"
            f"Ссылка на liquipedia: {players_urls[3]}\n"
            f">>>>>>>>>>>>>>>><<<<<<<<<<<<<<<\n"
            f"Pos5:\n"
            f"Ник: {Nickname[4]}\n"
            f"Имя: {Names[4]}\n"
            f"Роль: {Role[4]}{supp_emojii}\n"
            f"Национальность: {Nationality[4]}\n"
            f"Призовые за всё время: {dollar}{Prize[4][1::]}\n"
            f"Ссылка на liquipedia: {players_urls[4]}\n" )

if __name__ == '__main__':
    executor.start_polling(dp)