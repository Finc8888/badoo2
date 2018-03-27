import vk
from vk1 import MyVkData

session = vk.AuthSession(app_id = MyVkData.APP_ID, user_login = MyVkData.LOGIN,\
                         user_password = MyVkData.GET_PASSWORD(),\
                         scope = 'wall')
vk_api = vk.API(session, v='5.73')

MESSAGE = "The sky is the limit"
vk_api.wall.post(message = MESSAGE)
