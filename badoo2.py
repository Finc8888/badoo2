import vk
from vk1 import MyVkData
import time

session = vk.AuthSession(app_id = MyVkData.APP_ID, user_login = MyVkData.LOGIN,\
                         user_password = MyVkData.GET_PASSWORD())
vk_api = vk.API(session, v='5.73')

INTERESTS = ['английский',  'english']
SITE = 'vk.com/'
AGE_FROM = 23
AGE_TO = 33
SEX = 1
CITY = 119
groups = vk_api.groups.search(q = ','.join(INTERESTS), count = 20)

values = groups['items']
print("Количество подходящих групп:\
{}".format(groups['count']))
groups_id = [j['id'] for j in values]
#print(groups_id)
result =[]
for j in groups_id:
    person = vk_api.groups.getMembers(group_id = j, count = 10)
    time.sleep(1)
    result.append(person)
#print(result)
list_user_id = [i['items'] for i in result]
#print(list_user_id)
full_user_id = []
for i in list_user_id:
    for j in i:
        j = str(j)
        full_user_id.append(j)
        users2 = vk_api.users.get(user_ids = ','.join(full_user_id),\
        fields = "sex,city,bdate")
        time.sleep(1)

#print("users=",users2)
girl = [person for person in users2 if person["sex"] == SEX\
 and (person["city"])["id"] == CITY]
print(girl)
# print("Количество подходящих девушек: {}".format(len(users['items'])))
# try:
#     [print("Имя:{}, страничка: {},\n фото:{}"\
#     .format(user['first_name'] +  user['last_name'],SITE + user['domain'],\
#     user['photo_big']) ) for user in users['items'] ]
# except KeyError:
#     print("Ошибка")
