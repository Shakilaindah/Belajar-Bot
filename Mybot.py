import telebot
import mysql.connector

import mytoken


from datetime import datetime
TOKEN = mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)
myDb = mysql.connector.connect(host='localhost',user='root',database='db_belajarbott')
sql=myDb.cursor()
from telebot import apihelper
waktusekarang = datetime.now()

class Mybot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start', 'help'])
    def start(message):
        #photo = open('img/rpl.png', 'rb')
        #myBot.send_photo(message.from_user.id, photo)
        teks = mytoken.SAPA + "\n-- admin & developer @shakilaindah - SMK Taruna Bhakti -- "+"\n" \
                                "hari ini tanggal "+str(waktusekarang)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query = "select nipd,nama,kelas from tabel_siswaa"
        sql.execute(query)
        dataa = sql.fetchall()
        jmldata = sql.rowcount
        collectdata = ''
        if(jmldata>0):
            #print(data)
            no=0
            for x in dataa:
                no += 1
                collectdata = collectdata+ str(x)
                print(collectdata)
                collectdata = collectdata.replace('(', '')
                collectdata = collectdata.replace(')', '')
                collectdata = collectdata.replace("'", '')
                collectdata = collectdata.replace(",", '')

        else:
            print('data kosong')

        myBot.reply_to(message,str(collectdata))
print(myDb)
print("-- Bot sedang Berjalan --")
myBot.polling(none_stop=True)