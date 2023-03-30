from dotenv import load_dotenv
from selene import have
load_dotenv()



def test_profile(mashroom_api):
    mashroom_api.open('')
    mashroom_api.element('//*[@id="app"]/div[1]/main/div/div/div/div/h1').\
        should(have.text('Мои мероприятия'))


def test_profile(mashroom_api):
    mashroom_api.open('/profile-settings/181')
    mashroom_api.element('//*[@id="app"]/div[1]/main/div/div/div/div/div[2]/div[1]/div/div[2]/div/div[2]').\
        should(have.text('НАСТРОЙКА ПРОФИЛЯ'))






