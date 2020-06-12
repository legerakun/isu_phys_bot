import vk_api
import data
import random
#import time
from vk_api.longpoll import VkLongPoll, VkEventType
#from datetime import datetime

token = data.dt()
vk_session = vk_api.VkApi(token = token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

#Стадия разговора с ботом.
stage = 1

if stage == 1:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
           # print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
           # print('Текст сообщения: ' + str(event.text))
           # print(event.user_id)
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "привет":
                    stage = 1
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Приветствую вас! Выбери интересующий тебя пункт и отправь его цифру: \n\n1)О Профкоме ИГУ \n2)О нашем профбюро \n3)Материальная помощь \n4)Социальная стипендия \n5)Не нашел чего искал? Напиши пожелание! \n6)Нашел ошибку? Напиши ее сюда!', 'random_id': 0, 'attribute': "photo181707612"})
                elif response == "1" and stage == 1:
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Профком студентов ИГУ- Первичная профсоюзная организация студентов Иркутского государственного университета \n\nКонтакты:\n1️⃣Адрес: ул. Карла Маркса, 1, каб. 413\n2️⃣Адрес: ул. Нижняя набережная, 6, каб. 225 - в летний период не работает!\n📞 Телефон: 8 (3952) 33-44-55\n💬 Группа ВКонтакте- https://vk.com/profisu\n📲 Instagram.com/ppos_isu/ - @ppos_isu\n🤖 Бот Профкома студентов ИГУ, который мгновенно ответит на твой вопрос - https://vk.com/ppos_isu', 'random_id': 0})
                elif response == "2" and stage == 1:
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Мы- Профбюро Физического Факультета Иркутского Государственного Университета! \n\n😎 Председатель нашего профбюро: [sacomly|Волошенко Сергей] \n🏠 Адрес: ул.Бульвар Гагарина, 20, каб. 321', 'random_id': 0})
                elif response == "3" and stage == 1:
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Для получения материальной помощи необходимо ознакомиться с данным регламентом- https://vk.com/@profisu-novyi-reglament-po-materialnoi-podderzhke. Если появились вопросы обращайтесь к [sacomly|Волошенко Сергею].', 'random_id': 0})
                elif response == "4" and stage == 1:
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Для получения социальной стипендии ознакомьтесь с данной статьей- https://vk.com/@profisu-kak-poluchit-mat-pomosch. Если появились вопросы обращайтесь к [sacomly|Волошенко Сергею].', 'random_id': 0})
                elif response == "5" and stage == 1:
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Что вы хотели бы исправить/добавить в нашего бота?', 'random_id': 0})
                    stage = 2
                elif response == "6" and stage == 1:
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Опишите вашу проблему:', 'random_id': 0})
                    stage = 3
                else:
                    if stage == 1:
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Напиши цифру нужного пункта!', 'random_id': 0})
                    elif stage == 2:
                        vk_session.method('messages.send',{'user_id': event.user_id, 'message': 'Спасибо за отзыв!','random_id': 0})
                        stage = 1
                    elif stage == 3:
                        vk_session.method('messages.send',{'user_id': event.user_id, 'message': 'Спасибо! Мы исправим это в скором времени!', 'random_id': 0})
                        stage = 1