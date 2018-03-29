import vk
from vk1 import MyVkData
import time

SITE = 'vk.com/'
AGE_FROM = 23
AGE_TO = 33
SEX = 1
CITY = 119
INTERESTS = ['английский',  'english']

session = vk.AuthSession(app_id = MyVkData.APP_ID, user_login = MyVkData.LOGIN,\
                         user_password = MyVkData.GET_PASSWORD())
vk_api = vk.API(session, v='5.73')

def settings(site = SITE, age_from = AGE_FROM, age_to = AGE_TO,sex = SEX,
             city = CITY, interests = INTERESTS):
    """

    :return:
    """
    pass




def id_of__groups(dream = 0.5, amount_group = 10, amount_person = 80, report = False):
    """
    Получаем id групп с нужным интересом  с выбранной заддержкой для
    разгрузки сервера вк, нужным кол-во групп и кол-во людей в этих
    группах
    :return:[[person_id],[person_id],...[person_id]]
    """
    groups = vk_api.groups.search(q=','.join(INTERESTS), count=amount_group)
    values = groups['items']
    id_amount = groups['count']
    if report:
        print("Количество подходящих групп:{}".format(id_amount))

    #проверим что выбранное число груп не превышает существующее
    if amount_group not in range(0, id_amount + 1):
        amount_group = 10

    groups_id = [j['id'] for j in values]
    result =[]
    for j in groups_id:
        person = vk_api.groups.getMembers(group_id = j, count = amount_person)
        time.sleep(dream)
        result.append(person)
    return result


list_user_id = [i['items'] for i in id_of__groups()]
#print(list_user_id)
full_user_id = []
top = []
for i in list_user_id:
    for j in i:
        j = str(j)
        full_user_id.append(j)
        users2 = vk_api.users.get(user_ids = ','.join(full_user_id),\
        fields = "sex,city,bdate")
        time.sleep(0.5)

#print("users=",users2)
#print(users2[0]['city']['id'])
girl = []
amount = 0
for person in users2:
    if person["sex"] == SEX:
        try:
            if person["city"]:
                if person["city"]["id"] == CITY :
                    #girl.append(person)
                    print(person)
            else:
                pass
        except KeyError:
            amount += 1
print("Без города {} девушек".format(amount))
print("Поиск окончен")
#print(girl)

# print("Количество подходящих девушек: {}".format(len(users['items'])))
# try:
#     [print("Имя:{}, страничка: {},\n фото:{}"\
#     .format(user['first_name'] +  user['last_name'],SITE + user['domain'],\
#     user['photo_big']) ) for user in users['items'] ]
# except KeyError:
#     print("Ошибка")
