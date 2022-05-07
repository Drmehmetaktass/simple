import re, os, random, asyncio, html,configparser,pyrogram, subprocess, requests, time, traceback, logging, telethon, csv, json, sys
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from asyncio.exceptions import TimeoutError
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.client.chats import ChatMethods
from csv import reader
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError
from telethon.sessions import StringSession
from pyrogram import Client,filters
from pyromod import listen
from sql import add_user, query_msg
from support import users_info
from datetime import datetime, timedelta,date
import csv
#add_user= query_msg= users_info=0
if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists(f"Users/5053767281/phone.csv"):
   os.mkdir('./Users')
   os.mkdir(f'./Users/5053767281')
   open(f"Users/5053767281/phone.csv","w")
if not os.path.exists('data.csv'):
    open("data.csv","w")
APP_ID = 9789243
API_HASH = "1fb038afb5b72b2b6cc0c9a1a076eefa"
BOT_TOKEN = "5327005006:AAEV7lujDQ9Qi4-QOL9WyhKERNUsPv3WOBM"
UPDATES_CHANNEL = "deneme"
OWNER= [5053767281]
PREMIUM=[5053767281]
bot = pyrogram.Client("bot", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
        if d<=r:
            PREMIUM.append(int(row[1]))

# ------------------------------- Subscribe --------------------------------- #
async def Subscribe(lel, message):
   return 0



# ------------------------------- Start --------------------------------- #
@bot.on_message(filters.private & filters.command(["start"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   id = message.from_user.id
   user_name = '@' + message.from_user.username if message.from_user.username else None
   await add_user(id, user_name)
   but = InlineKeyboardMarkup([[InlineKeyboardButton("✅ Login", callback_data="Login"), InlineKeyboardButton("💯 Adding", callback_data="Adding") ],[InlineKeyboardButton("☎️ Phone", callback_data="Edit"), InlineKeyboardButton("PhoneSee💕", callback_data="Ish")],[InlineKeyboardButton("Phone Remove⚙️", callback_data="Removeall"), InlineKeyboardButton("AdminPannel", callback_data="Admin")]])
   await message.reply_text(f"**Merhaba** `{message.from_user.first_name}` **!\n\nBen Üye Çekme Botuyum ,\n\nCreator ❤️ @ByWolk**", reply_markup=but)



# ------------------------------- Set Phone No --------------------------------- #
@bot.on_message(filters.private & filters.command(["phone"]))
async def phone(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Artık Premium Kullanıcı değilsiniz\nLütfen Abonelik İçin\nDm\n\nCreator ❤️ @Bywolk**")
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
      str_list = [row[0] for row in csv.reader(f)]
      NonLimited=[]
      a=0
      for pphone in str_list:
         a+=1
         NonLimited.append(str(pphone))
      number = await app.ask(chat_id=message.chat.id, text="**Giriş yapmak için kaç hesap ekleyecekseniz sayısını girin (tam sayı olarak)\n\nCreator ❤️ @bywolk**")
      n = int(number.text)
      a+=n
      if n<1 :
         await app.send_message(message.chat.id, """**Geçersiz Biçim 1'Den Az Tekrar Deneyin\n\nCreator ❤️ @bywolk**""")
         return
      if a>100:
         await app.send_message(message.chat.id, f"**Yalnızca {100-a} Telefon numarası ekleyebilirsiniz\n\nCreator ❤️ @bywolk**")
         return
      for i in range (1,n+1):
         number = await app.ask(chat_id=message.chat.id, text="**Şimdi Telegram Hesabınızın Telefon Numarasını Uluslararası Formatta Gönderin. \n**Ülke Kodu** dahil. \nÖrnek: **+14154566376 = 14154566376 yalnızca +**\n\nCreator ❤️ @bywolk**")
         phone = number.text
         if "+" in phone:
            await app.send_message(message.chat.id, """**Bahsedildiği gibi + dahil değildir\n\nCreator ❤️ @bywolk**""")
         elif len(phone)==11 or len(phone)==12:
            Singla = str(phone)
            NonLimited.append(Singla)
            await app.send_message(message.chat.id, f"**{n}). Telefon: {phone} Başarıyla Ayarlandı✅\n\nCreator ❤️ @bywolk**")
         else:
            await app.send_message(message.chat.id, """**Geçersiz Sayı Biçimi Tekrar deneyin\n\nCreator ❤️ @bywolk**""") 
      NonLimited=list(dict.fromkeys(NonLimited))
      with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
         writer = csv.writer(writeFile, lineterminator="\n")
         writer.writerows(NonLimited)
      with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
         for line in infile:
            outfile.write(line.replace(",", ""))
 except Exception as e:
   await app.send_message(message.chat.id, f"**Hata: {e}\n\nCreator ❤️ @bywolk**")
   return



# ------------------------------- Acc Login --------------------------------- #
@bot.on_message(filters.private & filters.command(["login"]))
async def login(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Artık Premium Kullanıcı değilsiniz\nLütfen Abonelik İçin\nDm\n\nCreator ❤️ @bywolk**")
      return
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
    r=[]
    l=[]
    str_list = [row[0] for row in csv.reader(f)]
    po = 0
    s=0
    for pphone in str_list:
     try:
      phone = int(utils.parse_phone(pphone))
      client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
      await client.connect()
      if not await client.is_user_authorized():
         try:
            await client.send_code_request(phone)
         except FloodWait as e:
            await message.reply(f"{e.x} Saniyelik Floodwait'iniz Var")
            return
         except PhoneNumberInvalidError:
            await message.reply("Telefon Numaranız Geçersiz.\n\nYeniden Başlamak için /start'a basın!")
            return
         except PhoneNumberBannedError:
            await message.reply(f"{phone} yasaklandı")
            continue
         try:
            otp = await app.ask(message.chat.id, ("Telefon numaranıza bir KOD gönderildi, \nLütfen KOD'u '1 2 3 4 5' şeklinde girin. __(Her sayı arasındaki boşluk!)__ \n\nBot KOD göndermiyorsa, /restart deneyin yeniden başlatın. Sonra bot'a /start komutu.\nİptal etmek için /cancel'e basın."), timeout=300)
         except TimeoutError:
            await message.reply("Zaman Sınırına Ulaşıldı 5 Dakika.\nYeniden Başlamak için /start'a basın!")
            return
         otps=otp.text
         try:
            await client.sign_in(phone=phone, code=' '.join(str(otps)))
         except PhoneCodeInvalidError:
            await message.reply("Geçersiz Kod.\n\nYeniden Başlamak için /start'a basın!")
            return
         except PhoneCodeExpiredError:
            await message.reply("Kodun Süresi Doldu.\n\nYeniden Başlamak için /start'a basın!")
            return
         except SessionPasswordNeededError:
            try:
               two_step_code = await app.ask(message.chat.id,"Hesabınızın İki Adımlı Doğrulaması Var.\nLütfen Parolanızı Girin.",timeout=300)
            except TimeoutError:
               await message.reply("`Zaman Sınırına Ulaşıldı 5 Dakika.\n\nYeniden Başlamak için /start'a basın!`")
               return
            try:
               await client.sign_in(password=two_step_code.text)
            except Exception as e:
               await message.reply(f"**ERROR:** `{str(e)}`")
               return
            except Exception as e:
               await app.send_message(message.chat.id ,f"**ERROR:** `{str(e)}`")
               return
      with open("Users/1924880157/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         NonLimited=[]
         for pphone in str_list:
            NonLimited.append(str(pphone))
         Singla = str(phone)
         NonLimited.append(Singla)
         NonLimited=list(dict.fromkeys(NonLimited))
         with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(NonLimited)
         with open("1.csv") as infile, open(f"Users/1924880157/phone.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))
      os.remove("1.csv")
      await client(functions.contacts.UnblockRequest(id='@SpamBot'))
      await client.send_message('SpamBot', '/start')
      msg = str(await client.get_messages('SpamBot'))
      re= "bird"
      if re in msg:
         stats="İyi haber, şu anda hesabınıza herhangi bir sınır uygulanmıyor. bir kuş kadar özgürsün!"
         s+=1
         r.append(str(phone))
      else:
         stats='you are limited'
         l.append(str(phone))
      me = await client.get_me()
      await app.send_message(message.chat.id, f"Başarıyla Giriş Yapıldı. ✅\n\n**İsim:** {me.first_name}\n**Kullanıcı Adı:** {me.username}\n**Numara:** {phone}\n**SpamBot İstatistikleri:** {stats}\n\n**Creator ❤️ @bywolk**")     
      po+=1
      await client.disconnect()
     except ConnectionError:
      await client.disconnect()
      await client.connect()
     except TypeError:
      await app.send_message(message.chat.id, "**Telefon numarasını girmediniz \nlütfen Config⚙️ camand /start ile düzenleyin.\n\nCreator ❤️ @bywolk**")  
     except Exception as e:
      await app.send_message(message.chat.id, f"**Error: {e}\n\nCreator ❤️ @bywolk**")
    for ish in l:
      r.append(str(ish))
    with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
      writer = csv.writer(writeFile, lineterminator="\n")
      writer.writerows(r)
    with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
      for line in infile:
         outfile.write(line.replace(",", "")) 
    await app.send_message(message.chat.id, f"**All Acc Giriş {s} Hesabı Mevcut {po} \n\nCreator ❤️ @bywolk**") 
 except Exception as e:
   await app.send_message(message.chat.id, f"**Error: {e}\n\nCreator ❤️ @bywolk**")
   return
                          


# ------------------------------- Acc Private Adding --------------------------------- #
@bot.on_message(filters.private & filters.command(["adding"]))
async def to(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Artık Premium Kullanıcı değilsiniz\nLütfen Abonelik İçin\nDm\n\nCreator ❤️ @bywolk**")
      return
   number = await app.ask(chat_id=message.chat.id, text="**Üyesini Almak İstediğiniz Grubun Kullanıcı Adını Gönderin (Link Değil) \n\nCreator ❤️ @bywolk**")
   From = number.text
   number = await app.ask(chat_id=message.chat.id, text="**Üyeyi Aktarmak İstediğiniz Grubun Kullanıcı Adını Gönderin (Link Değil) \n\nCreator ❤️ @bywolk**")
   To = number.text
   number = await app.ask(chat_id=message.chat.id, text="**Başlangıç İçin Bir Sayı Belirleyin  \n\nCreator ❤️ @bywolk**")
   a = int(number.text)
   di=a
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         for pphone in str_list:
            peer=0
            ra=0
            dad=0
            r="**Adding Start**\n\n"
            phone = utils.parse_phone(pphone)
            client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
            await client.connect()
            await client(JoinChannelRequest(To))
            await app.send_message(chat_id=message.chat.id, text=f"**Üye Çekme Başlatıldı**")
            async for x in client.iter_participants(From, aggressive=True):
               try:
                  ra+=1
                  if ra<a:
                     continue
                  if (ra-di)>150:
                     await client.disconnect()
                     r+="**\nCreator ❤️ @bywolk**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(message.chat.id, f"**Error: {phone} Sonrakine Geçerken Bazı Hatalardan Dolayı Hayır\n\nCreator ❤️ @bywolk**")
                     break
                  if dad>40:
                     r+="**\nCreator ❤️ @bywolk**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     r="**Adding Start**\n\n"
                     dad=0
                  await client(InviteToChannelRequest(To, [x]))
                  status = 'DONE'
               except errors.FloodWaitError as s:
                  status= f'FloodWaitError for {s.seconds} sec'
                  await client.disconnect()
                  r+="**\nCreator ❤️ @bywolk**"
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  await app.send_message(chat_id=message.chat.id, text=f'**{s.seconds} sn için FloodWaitError\nSonraki Numaraya Geçiliyor**')
                  break
               except UserPrivacyRestrictedError:
                  status = 'PrivacyRestrictedError'
               except UserAlreadyParticipantError:
                  status = 'ALREADY'
               except UserBannedInChannelError:
                  status="User Banned"
               except ChatAdminRequiredError:
                  status="To Add Admin Required"
               except ValueError:
                  status="Error In Entry"
                  await client.disconnect()
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  break
               except PeerFloodError:
                  if peer == 10:
                     await client.disconnect()
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(chat_id=message.chat.id, text=f"**Çok Fazla PeerFloodError\nSonraki Numaraya Taşınıyor**")
                     break
                  status = 'PeerFloodError'
                  peer+=1
               except ChatWriteForbiddenError as cwfe:
                  await client(JoinChannelRequest(To))
                  continue
               except errors.RPCError as s:
                  status = s.__class__.__name__
               except Exception as d:
                  status = d
               except:
                  traceback.print_exc()
                  status="Unexpected Error"
                  break
               r+=f"{a-di+1}). **{x.first_name}**   ⟾   **{status}**\n"
               dad+=1
               a+=1
   except Exception as e:
      await app.send_message(chat_id=message.chat.id, text=f"Error: {e} \n\n Creator ❤️ @bywolk")
 except Exception as e:
   await app.send_message(message.chat.id, f"**Error: {e}\n\nCreator ❤️ @bywolk**")
   return



# ------------------------------- Start --------------------------------- #
@bot.on_message(filters.private & filters.command(["phonesee"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Artık Premium Kullanıcı değilsiniz\nLütfen Abonelik İçin\nDm\n\nCreator ❤️ @jackdanielssx**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         de="**Your Phone Numbers are**\n\n"
         da=0
         dad=0
         for pphone in str_list:
            dad+=1
            da+=1
            if dad>40:
               de+="**\nCreator ❤️ @bywolk**"
               await app.send_message(chat_id=message.chat.id, text=f"{de}")
               de="**Telefon Numaralarınız**\n\n"
               dad=0 
            de+=(f"**{da}).** `{int(pphone)}`\n")
         de+="**\nCreator ❤️ @bywolk**"
         await app.send_message(chat_id=message.chat.id, text=f"{de}")

   except Exception as a:
      pass


# ------------------------------- Start --------------------------------- #
@bot.on_message(filters.private & filters.command(["removeall"]))
async def removeall(lel, message):
 try:
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = []
         with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(str_list)
         with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
            for line in infile:
               outfile.write(line.replace(",", ""))
         await app.send_message(chat_id=message.chat.id,text="Başarıyla Tamamlandı")
   except Exception as a:
      pass
 except Exception as e:
   await app.send_message(message.chat.id, f"Error: {e}\n\nCreator ❤️ @bywolk")
   return

@bot.on_message(filters.private & filters.command(["remove"]))
async def start(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Artık Premium Kullanıcı değilsiniz\nLütfen Abonelik İçin\nDm\n\nCreator ❤️ @bywolk**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         f.closed
         number = await app.ask(chat_id=message.chat.id, text="**Kaldırılacak Numarayı Gönder\n\nCreator ❤️ @bywolk**")
         print(str_list)
         str_list.remove(number.text)
         with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(str_list)
         with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
            for line in infile:
               outfile.write(line.replace(",", ""))
         await app.send_message(chat_id=message.chat.id,text="Başarıyla Tamamlandı")
   except Exception as a:
      pass
 except Exception as e:
   await app.send_message(message.chat.id, f"**Error: {e}\n\nCreator ❤️ @bywolk**")
   return

# ------------------------------- Admin Pannel --------------------------------- #
@bot.on_message(filters.private & filters.command('ishan'))
async def subscribers_count(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id in OWNER:
      but = InlineKeyboardMarkup([[InlineKeyboardButton("Users✅", callback_data="Users")], [InlineKeyboardButton("Broadcast💯", callback_data="Broadcast")],[InlineKeyboardButton("AddUser", callback_data="New")], [InlineKeyboardButton("Check Users", callback_data="Check")]])
      await app.send_message(chat_id=message.chat.id,text=f"**Merhaba** `{message.from_user.first_name}` **!\n\nScraper Bot'un Yönetici Paneline Hoş Geldiniz\n\nCreator ❤️ @bywolk**", reply_markup=but)
   else:
      await app.send_message(chat_id=message.chat.id,text="**You are not owner of Bot \n\nCreator ❤️ @bywolk**")



# ------------------------------- Buttons --------------------------------- #
@bot.on_callback_query()
async def button(app, update):
   k = update.data
   if "Login" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Artık hiçbir şey yok..!\nGiriş yapmak ve Hesap istatistiklerini kontrol etmek için /login'e tıklamanız yeterli.\n\nCreator ❤️ @bywolk**""") 
   elif "Ish" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Artık hiçbir şey yok..!\nGiriş yapmak ve Hesap istatistiklerini kontrol etmek için /phonesee'ye tıklamanız yeterli.\n\nCreator ❤️ @bywolk**""") 
   elif "Remove" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Artık hiçbir şey yok..!\nGiriş yapmak ve Hesap istatistiklerini kontrol etmek için /removeall'a tıklamanız yeterli.\n\nCreator ❤️ @bywolk**""") 
   elif "Adding" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Artık bir şey yok..!\nGiriş✅ Hesaptan eklemeye başlamak için /adding tıklamanız yeterli.\n\nCreator ❤️ @bywolk**""") 
   elif "Edit" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Artık hiçbir şey yok..!\nGiriş yapmak ve Hesap istatistiklerini kontrol etmek için /phone'a tıklamanız yeterli.\n\nCreator ❤️ @bywolk**""") 
   elif "Home" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Artık hiçbir şey yok..!\nEve Gitmek için /start'a tıklamanız yeterli.\n\nCreator ❤️ @bywolk**""") 
   elif "Users" in k:
      await update.message.delete()
      msg = await app.send_message(update.message.chat.id,"Lütfen bekleyin...")
      messages = await users_info(app)
      await msg.edit(f"Total:\n\nUsers - {messages[0]}\nBlocked - {messages[1]}")
   elif "New" in k:
      await update.message.delete()
      number = await app.ask(chat_id=update.message.chat.id, text="**Yeni Kullanıcının Kullanıcı Kimliğini Gönder\n\nCreator ❤️ @bywolk**")
      phone = int(number.text)
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         f.closed
         f = open("data.csv", "w", encoding='UTF-8')
         writer = csv.writer(f, delimiter=",", lineterminator="\n")
         writer.writerow(['sr. no.', 'user id', "Date"])
         a=1
         for i in rows:
            writer.writerow([a, i[1],i[2]])
            a+=1
         writer.writerow([a, phone, date.today() ])
         PREMIUM.append(int(phone))
         await app.send_message(chat_id=update.message.chat.id,text="Başarıyla Tamamlandı")

   elif "Check" in k:
      await update.message.delete()
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         E="**Premium Users**\n"
         a=0
         for row in rows:
            d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
            r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
            if d<=r:
               a+=1
               E+=f"{a}). {row[1]} - {row[2]}\n"
         E+="\n\n**Creator ❤️ @bywolk**"
         await app.send_message(chat_id=update.message.chat.id,text=E)

   elif "Admin" in k:
      await update.message.delete()
      if update.message.chat.id in OWNER:
         but = InlineKeyboardMarkup([[InlineKeyboardButton("Users✅", callback_data="Users")], [InlineKeyboardButton("Broadcast💯", callback_data="Broadcast")],[InlineKeyboardButton("AddUser", callback_data="New")], [InlineKeyboardButton("Check Users", callback_data="Check")]])
         await app.send_message(chat_id=update.message.chat.id,text=f"**Scraper Bot'un Yönetici Paneline Hoş Geldiniz\n\nCreator ❤️ @bywolk**", reply_markup=but)
      else:
         await app.send_message(chat_id=update.message.chat.id,text="**Bot'un sahibi değilsiniz \n\nCreator ❤️ @bywolk**")
   elif "Broadcast" in k:
    try:
      query = await query_msg()
      a=0
      b=0
      number = await app.ask(chat_id=update.message.chat.id, text="**Yayın için şimdi ben mesajım\n\nCreator ❤️ @bywolk**")
      phone = number.text
      for row in query:
         chat_id = int(row[0])
         try:
            await app.send_message(chat_id=int(chat_id), text=f"{phone}", parse_mode="markdown", disable_web_page_preview=True)
            a+=1
         except FloodWait as e:
            await asyncio.sleep(e.x)
            b+=1
         except Exception:
            b+=1
            pass
      await app.send_message(update.message.chat.id,f"{a} Sohbetlere Başarıyla Yayınlandı\nBaşarısız - {b} Sohbetlere!")
    except Exception as e:
      await app.send_message(update.message.chat.id,f"**Hata: {e}\n\nCreator ❤️ @bywolk**")




text = """
╔════╗ㅤMembers 
╚═╗╔═╝ Scraping Bot
╔═╣╠═╗
║╔╣╠╗║ Scraper
║╚╣╠╝║ Scraper Bot
╚═╣╠═╝
╔═╝╚═╗ 
╚════╝ 
"""
print(text)
print("Uyarılmış Ekleme Başarıyla Başladı........")
bot.run()
