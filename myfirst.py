import vk
import random
import time

session=vk.Session(access_token="98de103612c0555f2e897712f495fa1298a22abc6a49b2d03b7bb6d0797b7ebb2561b502c4e0629646b8e")
vk_api = vk.API(session, v='5.62')
ass=vk_api.messages.getDialogs(count=10)
for msg in ass['items']:
           if 'chat_id' in msg['message']:
               print("Название беседы:",msg['message']['title'], "Чат-айди -",msg['message']['chat_id'])
chaterid=int(input("Введите чат где вы хотите выбрать пидора дня!\n Чат-айди: "))
a=vk_api.messages.getChat(chat_ids=chaterid)
a=a[0]["users"]
pidor= random.choice(a)
b="[id"+str(pidor)+"|Пидор дня]\nМои поздравления! \nДата(мск+1): "+time.strftime('%Y-%m-%d %H:%M:%S' )
print(b,"\n Дата(мск+1):",time.strftime('%Y-%m-%d %H:%M:%S' ))
goodman = "Лучший юзер дня"
vk_api.messages.send(chat_id=chaterid, message=b)
#vk_api.wall.post(message='hello world!',attachments="photo285056992_466257441")