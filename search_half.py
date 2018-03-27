import vk
from vk1 import MyVkData

session = vk.AuthSession(app_id = MyVkData.APP_ID, user_login = MyVkData.LOGIN,\
                         user_password = MyVkData.GET_PASSWORD())
vk_api = vk.API(session, v='5.73')

INTERESTS = ['Спорт', 'книги', 'стихи', 'английский']
SITE = 'vk.com/'
AGE_FROM = 23
AGE_TO = 33
SEX = 1
CITY = 119
users = vk_api.users.search(interests = ','.join(INTERESTS), city = CITY, sex = SEX,\
                            age_from = AGE_FROM, age_to = AGE_TO,\
                            fields = 'bdate,photo_big,domain')

print("Количество подходящих девушек: {}".format(len(users['items'])))
try:
    [print("Имя:{}, страничка: {},\n фото:{}"\
    .format(user['first_name'] +  user['last_name'],SITE + user['domain'],\
    user['photo_big']) ) for user in users['items'] ]
except KeyError:
    print("Ошибка")

