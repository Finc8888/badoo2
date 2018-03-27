import vk
from vk1 import MyVkData

session = vk.AuthSession(app_id = MyVkData.APP_ID, user_login = MyVkData.LOGIN,\
                         user_password = MyVkData.GET_PASSWORD())
# session = vk.Session()
vk_api = vk.API(session, v='5.73')

friends = vk_api.friends.get(user_id = MyVkData.MY_USER_ID, fields = 'domain,photo')
#print(friends)

print("Количество моих друзей: {}".format(len(friends['items'])))

[print(friend) for friend in friends['items']]
