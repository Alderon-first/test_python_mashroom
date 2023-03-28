import allure
from selene import be, have
from selene.support.shared import browser
import time
from test_python_mashroom.UI.model.data.user import user


class UserPage:
    def __init__(self):
        pass

    @allure.step("Открыть страницу зрителя только с чатом")
    def open_user_page_only_chat(self):
        browser.open('platform/?hash=SjSQNEEVtGDCzHUR&is-only-chat=true')

    @allure.step("Регистрация в чате")
    def open_chat_reg(self):
        time.sleep(2)
        browser.element('a.text-decoration-underline.link--text').click()
        time.sleep(2)
        browser.element("//div[@id='pml-widget-app']/div[3]/div/div/div[2]/span/form/div/div/span/div/div/div/div").click()
        browser.element('/html/body/vue-widget/div/div[3]/div/div/div[2]/span/form/div[1]/div/span/div/div/div[1]/div/input').clear()
        browser.element(
            '/html/body/vue-widget/div/div[3]/div/div/div[2]/span/form/div[1]/div/span/div/div/div[1]/div/input').should(be.blank).type(user.first_name)
        browser.element('/html/body/vue-widget/div/div[3]/div/div/div[2]/span/form/button').click()

    @allure.step("Отправка сообщения в чат")
    def send_message(self):
        browser.element(
            '/html/body/vue-widget/div/div[1]/main/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/form/div/div/div/div/div/textarea').clear()
        browser.element(
            '/html/body/vue-widget/div/div[1]/main/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/form/div/div/div/div/div/textarea').should(
            be.blank).type(user.message)
        browser.element(
            '/html/body/vue-widget/div/div[1]/main/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/form/div/button/span/span').click()

    @allure.step("Проверка: сообщение отправлено")
    def chek_message(self):
        browser.all('//*[@id="pml-widget-fullscreen-wrapper"]/div[2]/div/div/div[2]/div/div/div/div[1]').should(have.texts(user.first_name))
        browser.all('//*[@id="pml-widget-fullscreen-wrapper"]/div[2]/div/div/div[2]/div/div/div/div[1]').should(
            have.texts(user.message))



