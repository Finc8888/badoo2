import vk
from vk1 import MyVkData

session = vk.AuthSession(app_id = MyVkData.APP_ID, user_login = MyVkData.LOGIN,\
                         user_password = MyVkData.GET_PASSWORD())
# session = vk.Session()
vk_api = vk.API(session, v='5.73')

tema = "Python"
groups = vk_api.groups.search(q = tema, count = 30)

#print(groups)

groups_count = groups['count']
print('Количество групп с темой {} : {}'.format(tema,groups_count))

groups = groups['items']

[print(group['name']) for group in groups]
