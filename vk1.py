#импортируем нужные модули
import vk

print("Библиотека vk установлена")
class MyVkData:
    #индентификатор моего пользователя  вконтакте
    MY_USER_ID = '372406084'
    #индентификатор Павла Дурова
    DUROV_USER_ID = '1'
    #общая ссылка для доступа к api
    API_URL = 'https://api.vk.com/method/'
    #логин пользователя вконтакте
    LOGIN = 'con8@mail.ru'
    #индентификатор приложения вконтакте
    APP_ID = '6419844'

    #мой пароль вконтакте
    @staticmethod
    def GET_PASSWORD():
        f = open('pass.txt', 'r')
        passw = f.read().rstrip()
        f.close()
        return passw

if __name__ == '__main__':
    passw = MyVkData.GET_PASSWORD()
    print(passw)
    print('end')

