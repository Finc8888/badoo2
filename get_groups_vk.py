import vk
from vk1 import MyVkData

session = vk.AuthSession(app_id = MyVkData.APP_ID, user_login = MyVkData.LOGIN,\
                         user_password = MyVkData.GET_PASSWORD())
# session = vk.Session()
vk_api = vk.API(session, v='5.73')
VV = 96490597

groups = vk_api.groups.get(user_id = 19, extended=1)

#print(groups)

groups_count = groups['count']
print('Количество групп : {}'.format(groups_count))

groups = groups['items']

[print(group['name']) for group in groups]
