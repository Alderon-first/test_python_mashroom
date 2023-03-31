import allure
from selene import have
from selene.support.shared import browser


class UserPage:
    def __init__(self):
        pass

    @allure.step("Открыть тестовую страницу")
    def open_user_testpage(self):
        browser.open('/test?theme=mashroom')

    @allure.step("Проверка: страница имеет заголовок 'Тестовая страница платформы'")
    def chek_title_user_testpage(self):
        browser.element(
            '#app > div > main > div > div > div.default-layout-section.pt-6.px-4.px-md-10.pb-md-6 > div').should(
            have.text("Тестовая страница платформы"))

    @allure.step("Открыть страницу виджета несуществующего мероприятия")
    def open_user_widget(self):
        browser.open('/?hash=test')

    @allure.step("Проверка: отображается текст 'Мероприятие не найдено'")
    def chek_title_user_widget(self):
        browser.element(
            '#pml-widget-fullscreen-wrapper > div.default-layout-block > div > '
            'div.grey--text.text--darken-3.not-found__wrapper > div.text-h4.mb-6.not-found__title').should(
            have.text("Мероприятие не найдено"))
