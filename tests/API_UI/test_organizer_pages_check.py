import os

from dotenv import load_dotenv
from selene import have

load_dotenv()


def test_activity_page(mashroom_api):
    mashroom_api.open('')
    mashroom_api.element('//*[@id="app"]/div[1]/main/div/div/div/div/h1').\
        should(have.text('Мои мероприятия'))
    mashroom_api.element(
        '#app > div.v-application--wrap > main > div > div > div > div > div.row.mb-4.no-gutters > '
        'div.col-12.col-md.mr-6.col > div > div > div.v-slide-group__wrapper > div > div.v-tab.v-tab--active').\
        should(have.text('ТЕКУЩИЕ И ЗАПЛАНИРОВАННЫЕ'))
    mashroom_api.element(
        '#app > div.v-application--wrap > main > div > div > div > div > div.row.mb-4.no-gutters > '
        'div.col-12.col-md.mr-6.col > div > div > div.v-slide-group__wrapper > div > div:nth-child(3)').\
        should(have.text('АРХИВНЫЕ'))
    mashroom_api.element(
        '#app > div.v-application--wrap > main > div > div > div > div > div.row.mb-4.no-gutters > '
        'div.col.col-auto > button > span'). \
        should(have.text('НОВОЕ МЕРОПРИЯТИЕ'))
    mashroom_api.element(
        '#app > div.v-application--wrap > div:nth-child(1) > header > div > div.d-flex.align-center > span'). \
        should(have.text(os.getenv("LOGIN")))
    mashroom_api.element(
        '//*[@id="app"]/div/main/div/div/div/div/div[2]/div/div/div/div/div[1]/table/tbody/tr/td/div/div'). \
        should(have.text('Нажмите на кнопку "Новое мероприятие", чтобы создать мероприятие'))


def test_profile_page(mashroom_api):
    mashroom_api.open('/profile-settings/181')
    mashroom_api.element('//*[@id="app"]/div[1]/main/div/div/div/div/div[2]/div[1]/div/div[2]/div/div[2]').\
        should(have.text('НАСТРОЙКА ПРОФИЛЯ'))


def test_profile_page_tab_arch(mashroom_api):
    mashroom_api.open('/?tab=1')
    mashroom_api.element('#app > div.v-application--wrap > main > div > div > div > div > div.row.mb-4.no-gutters > '
                         'div.col-12.col-md.mr-6.col > div > div > div.v-slide-group__wrapper > div > '
                         'div.v-tab.v-tab--active').\
        should(have.attribute('aria-selected', "true"))


def test_profile_page_tab_live(mashroom_api):
    mashroom_api.open('/?tab=0')
    mashroom_api.element('#app > div.v-application--wrap > main > div > div > div > div > div.row.mb-4.no-gutters > '
                         'div.col-12.col-md.mr-6.col > div > div > div.v-slide-group__wrapper > div > '
                         'div.v-tab.v-tab--active').\
        should(have.attribute('aria-selected', "true"))


