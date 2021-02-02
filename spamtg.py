from telethon.sync import TelegramClient, events

#from pyotp import TOTP

#if input("Введи код из статьи: ") != TOTP("UC2UQZPN32334CZK").now():
#	exit(1)
#else:
#	print("Код правильный")

#SERGOPROXY TG:@sergey0804,darksploit:SergoProxy
print("'TG - spam' - скрипт написан SergoProxy, для спама в личных сообщения телеграм. \n Все вопросы и идеи в TG: @sergey0804")
print()
hashtg = input("Введите хэш аккаунта: ")
iptg = int(input("Введите ip приложения: "))
px = int(input("Введите количество сообщений: "))
idp = input("Введите id пользователя: ")
mes = input("Текст сообщения: ")

api_id = iptg
api_hash = hashtg

with TelegramClient('proxy', api_id, api_hash) as client:
	for i in range(px):
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		
#SERGOPROXY TG:@sergey0804,darksploit:SergoProxy
