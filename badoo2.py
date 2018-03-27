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
groups = vk_api.groups.search(q = ','.join(INTERESTS), count = 10)
#sex = SEX,\
#age_from = AGE_FROM, age_to = AGE_TO,\
#fields = 'bdate,photo_big,domain')
values = groups['items']
print("Количество подходящих групп:\
{}".format(groups['count']))
groups_id = [j['id'] for j in values]
print(groups_id)
result =[]
for j in groups_id:
    person = vk_api.groups.getMembers(group_id = j, count = 10) 
    time.sleep(1)
    result.append(person)
print(result)
list_user_id = [i['items'] for i in result]
print(list_user_id)
full_user_id = []

    #[print("Имя:{}, страничка: {},\n фото:{}"\  .format(user['first_name'] +  user['last_name'],SITE + user['domain'],\
#user['photo_big']) ) for user in users['items'] ]
    #print(groups)


